# 🚀 Django Authentication System

A simple Django authentication system with user **Signup, Login, Logout**, and a protected **Dashboard** using Django's built-in authentication system.

## 📌 Features
- 🔑 User Signup & Login
- 🔓 User Logout
- 🔒 Protected Dashboard (only accessible when logged in)
- 🎨 Bootstrap-based responsive UI
- 🛠️ Admin panel for user management

## 🏗 Project Setup

1️⃣ **Clone the Repository**
```sh
git clone <your-repository-url>
cd <your-project-folder>
```

2️⃣ **Create & Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

4️⃣ **Run Migrations**
```sh
python manage.py migrate
```

5️⃣ **Create a Superuser (Admin Panel Access)**
```sh
python manage.py createsuperuser
```

6️⃣ **Run the Development Server**
```sh
python manage.py runserver
```

Visit **http://127.0.0.1:8000/signup/** to sign up.

## 🖥️ Admin Panel
Access the Django admin panel at **http://127.0.0.1:8000/admin/** and log in with the superuser credentials.

## 📂 Project Structure
```
myproject/
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   ├── views.py
│   ├── urls.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
├── manage.py
└── requirements.txt
```

## 🔧 Built With
- **Django** - Python Web Framework 🐍
- **Bootstrap** - Frontend Styling 🎨
- **SQLite** - Default Database 🗃️

## 📜 License
This project is open-source and free to use. 🚀

