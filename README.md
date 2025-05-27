# Django Portfolio

This is a dynamic and modular personal portfolio project built with **Django**, **JavaScript**, and **Tailwind CSS**. It features editable sections including About, Education, Skills, Projects, Experience, Learning, Certificates, and Activities — all managed through API endpoints.

### 🔧 Key Features

- 🧑‍💼 Admin-authenticated CRUD operations via Django REST Framework (DRF)
- 📁 **Image upload and preview** functionality for Certificates and Activities
- 🖼️ View uploaded images in a new browser tab with one-click access
- 📚 Modular sections powered by reusable JSON-based API calls
- ⚡ Frontend rendered dynamically using vanilla JavaScript
- 💾 SQLite (default), easily swappable with PostgreSQL or MySQL

---

### 📸 Image Upload Highlights

- Activity and Certificate sections support file uploads
- Each uploaded image displays a **"View Image"** icon
- Clicking the icon opens the file in a **new browser tab**

---

### 🚀 Technologies Used

- Django 4.x
- Django REST Framework
- Tailwind CSS
- Vanilla JavaScript
- SQLite (default DB)
- HTML5 / Responsive Design

---

### 📦 Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/django-portfolio.git
cd django-portfolio
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate (Linux/macOS)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
