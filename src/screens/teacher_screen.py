import time
import streamlit as st

from src.ui.base_layout import style_base_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.database.db import (
    check_teacher_exists,
    create_teacher,
    teacher_login,
)


def teacher_screen():

    style_base_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
        return

    if "teacher_login_type" not in st.session_state:
        st.session_state.teacher_login_type = "login"

    if st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    else:
        teacher_screen_register()


def teacher_dashboard():

    teacher_data = st.session_state["teacher_data"]

    c1, c2 = st.columns([8, 2])

    with c1:
        st.header(f"Welcome, {teacher_data['name']} 👋")

    with c2:
        if st.button("Logout", type="primary", use_container_width=True):
            st.session_state.pop("teacher_data", None)
            st.session_state.pop("user_role", None)
            st.session_state.pop("is_logged_in", None)
            st.session_state.teacher_login_type = "login"
            st.rerun()


def login_teacher(username, password):

    if not username or not password:
        return False

    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.teacher_data = teacher
        st.session_state.user_role = "teacher"
        st.session_state.is_logged_in = True
        return True

    return False


def teacher_screen_login():

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

    st.header("Login using password", text_alignment="center")

    st.space()
    st.space()

    teacher_username = st.text_input(
        "Enter Username",
        placeholder="Krishna",
        key="login_username",
    )

    teacher_pass = st.text_input(
        "Enter Password",
        type="password",
        placeholder="Enter Password",
        key="login_password",
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:

        if st.button(
            "Login",
            icon=":material/passkey:",
            width="stretch",
        ):

            if login_teacher(teacher_username, teacher_pass):

                st.toast("Welcome Back!", icon="👋")
                time.sleep(1)
                st.rerun()

            else:
                st.error("Invalid Username or Password")

    with btnc2:

        if st.button(
            "Register",
            type="primary",
            icon=":material/person_add:",
            width="stretch",
        ):

            st.session_state.teacher_login_type = "register"
            st.rerun()

def register_teacher(
    teacher_username,
    teacher_name,
    teacher_pass,
    teacher_pass_confirm,
):

    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are required!"

    if check_teacher_exists(teacher_username):
        return False, "Username already exists!"

    if teacher_pass != teacher_pass_confirm:
        return False, "Passwords do not match!"

    try:
        create_teacher(
            teacher_username,
            teacher_pass,
            teacher_name,
        )

        return True, "Teacher account created successfully!"

    except Exception as e:
        return False, str(e)


def teacher_screen_register():

    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge",
    )

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go back to home",
            type="secondary",
            key="registerbackbtn",
        ):
            st.session_state.login_type = None
            st.rerun()

    st.header(
        "Register your teacher profile",
        text_alignment="center",
    )

    st.space()
    st.space()

    teacher_username = st.text_input(
        "Enter Username",
        placeholder="Krishna",
        key="register_username",
    )

    teacher_name = st.text_input(
        "Enter Name",
        placeholder="Krishna",
        key="register_name",
    )

    teacher_pass = st.text_input(
        "Enter Password",
        type="password",
        placeholder="Enter Password",
        key="register_password",
    )

    teacher_pass_confirm = st.text_input(
        "Confirm Password",
        type="password",
        placeholder="Confirm Password",
        key="register_confirm_password",
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:

        if st.button(
            "Register Now",
            icon=":material/person_add:",
            width="stretch",
        ):

            success, message = register_teacher(
                teacher_username,
                teacher_name,
                teacher_pass,
                teacher_pass_confirm,
            )

            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    with btnc2:

        if st.button(
            "Login Instead",
            type="primary",
            icon=":material/login:",
            width="stretch",
        ):

            st.session_state.teacher_login_type = "login"
            st.rerun()