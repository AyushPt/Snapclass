import streamlit as st
import numpy as np

from src.ui.base_layout import style_base_dashboard, style_base_layout
from src.components.header import header_dashboard
from PIL import Image
from src.pipelines.face_pipeline import predict_attendance , get_face_embeddings , train_classifier
from src.database.db import get_all_students, create_student
import time 
from src.pipelines.voice_pipeline import get_voice_embedding



def student_dashboard():
    st.header('DASHBOARD HERE')


def student_screen():
    style_base_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go back to home",
            type="secondary",
            key="loginbackbtn",
        ):
            st.session_state.login_type = None
            st.rerun()

    st.header("Login using FaceID", text_alignment="center")
    st.space()
    st.space()

    show_registration = False
    
    photo_source = st.camera_input("Position Your Face in the centre")

    if photo_source:
        current_photo_id = getattr(photo_source, "file_id", getattr(photo_source, "id", None))

        # Only run heavy AI face detection when a new photo is taken
        if (
            st.session_state.get("last_photo_id") != current_photo_id
            or "last_scan_result" not in st.session_state
        ):
            img = np.array(Image.open(photo_source))
            with st.spinner("AI is scanning..."):
                detected, all_ids, num_faces = predict_attendance(img)
                st.session_state.last_photo_id = current_photo_id
                st.session_state.last_scan_result = (detected, all_ids, num_faces)
        else:
            detected, all_ids, num_faces = st.session_state.last_scan_result

        if num_faces == 0:
            st.warning('Faces not Found')
        elif num_faces > 1:
            st.warning('Multiple Faces Found')
        else:
            if detected:
                student_id = list(detected.keys())[0]
                all_students = get_all_students()
                student = next((s for s in all_students if s['student_id'] == student_id), None)

                if student:
                    st.session_state.is_logged_in = True
                    st.session_state.user_role = 'student'
                    st.session_state.student_data = student 
                    st.toast(f"Welcome Back {student['name']}")
                    time.sleep(1)
                    st.rerun()
                else:
                    # Stale model cache detected deleted student; refresh cache and show registration
                    train_classifier()
                    st.info('Face not recognized in database! You might be a new student')
                    show_registration = True
            else:
                st.info('Face not Recognized!! You might be a new student')
                show_registration = True
    else:
        st.session_state.pop("last_photo_id", None)
        st.session_state.pop("last_scan_result", None)

    if show_registration:
        with st.container(border=True):
            st.header('Register new Profile')
            new_name = st.text_input('Enter your Name', placeholder='E.g. Ayush Patel')

            st.subheader('Optional : Voice Enrollment')
            st.info("Enroll for your Voice only Attendance")


            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am Present, My Name is Ayush')
            except Exception:
                st.error('Audio Data Failed!')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating Profile...'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())


                            response_data = create_student(new_name, face_embeddings = face_emb, voice_embedding = voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.pop("last_photo_id", None)
                                st.session_state.pop("last_scan_result", None)
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0] 
                                st.toast(f'Profile Created! Hi {new_name}')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Could not capture your facial features for registration')  

                else:
                    st.warning('Please Enter Your Name')