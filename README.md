# 📝 Django Blog Project

A simple blog application built with Django, designed to list and manage blog posts with a clean admin interface and a public-facing homepage.

## 🚀 Features

- Create, update, and delete blog posts via Django Admin
- Public-facing list view for blog posts
- Responsive design with HTML & CSS
- Git version controlled
- Easily extendable for future features (e.g., comments, tags, categories)

---

## 📂 Project Structure

```
blog_project/
├── blog/               # Main Django app for blog logic
├── blog_project/       # Django project settings and config
├── static/             # Static files (CSS, images, etc.)
├── templates/          # HTML templates
├── manage.py
├── README.md
├── requirements.txt
```

---

## 🧱 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```

### 2. Create and activate a virtual environment

```bash
# For venv:
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# OR using Poetry:
poetry install
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create superuser for admin

```bash
python manage.py createsuperuser
```

### 6. Start development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to see the blog.

---

## 👩‍💻 Admin Panel

Access the admin interface at:

```
http://127.0.0.1:8000/admin/
```

Use your superuser credentials to log in and manage blog posts.

---

## 🎯 Development Milestones (Week 1 Plan)

| Day | Focus |
|-----|-------|
| ✅ Day 1 | Project setup + Git initialized |
| ✅ Day 2 | Blog app created + Routing configured |
| ✅ Day 3 | Blog post model + Admin interface |
| ✅ Day 4 | List view + Template rendering |
| ✅ Day 5 | Code review + README documentation |

---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x
- HTML5 + CSS3 (custom styles)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Author

Built by Zoltan.  
Feel free to fork, contribute, or reach out with suggestions!