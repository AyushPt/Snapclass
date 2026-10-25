# Snapclass 🎓

Smart Attendance & Classroom Management using Facial Recognition & Voice Verification.

---

## 🚀 Setup on a New Laptop

### 1. Clone the repository
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd Snapclass
```

### 2. Set up Python Virtual Environment (Python 3.10 - 3.12 recommended)
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note on dlib / face_recognition:**
> On Windows, `dlib-bin` or CMake + C++ Build Tools might be required if building from source. `dlib-bin` in `requirements.txt` provides prebuilt wheels for Python on Windows.

### 4. Configure Supabase Secrets
Create `.streamlit/secrets.toml` from the template:
```bash
# Windows
mkdir .streamlit
copy secrets.example.toml .streamlit\secrets.toml
```

Edit `.streamlit/secrets.toml` and add your Supabase credentials:
```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-key"
```

### 5. Run the Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.
