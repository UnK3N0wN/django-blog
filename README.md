# Django Blog Project

A fun college project built using **Django** that allows users to create, manage, and explore blog posts through a clean and simple web interface.

This project includes blog management, categories, authentication, dashboards, and search functionality.

---

## Features

* User Registration & Login
* Create, Edit, and Delete Blog Posts
* Category Management
* Dashboard for Managing Content
* Search Functionality
* Responsive UI with Templates
* Media & Static File Handling
* Admin Panel Support
* Error Handling (404 Page)

---

## Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite3
* **Authentication:** Django Auth System

---

## Project Structure

```bash
blog/
│
├── blog_main/          # Main project settings and configuration
├── blogs/              # Blog application
├── dashboards/         # Dashboard and admin-related features
├── templates/          # HTML templates
├── static/             # CSS, JS, Images
├── media/              # Uploaded media files
├── manage.py
└── db.sqlite3
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```bash
http://127.0.0.1:8000/
```

---

## Dashboard Pages

The project includes dashboard pages for:

* Managing Posts
* Managing Categories
* Managing Users
* Viewing Personal Posts

---

## Screens Included

Some pages available in the project:

* Home Page
* Landing Page
* Blog Listing
* Search Page
* Login/Register
* Dashboard
* Add/Edit Posts
* Add/Edit Categories

---

## Future Improvements

* Add Rich Text Editor
* Add Likes & Comments System
* User Profile Pages
* Dark Mode
* REST API Integration
* Deployment on Render/Heroku/Vercel

---

## Learning Outcomes

This project helped in understanding:

* Django Project Structure
* MVC/MVT Architecture
* Authentication & Authorization
* CRUD Operations
* Template Rendering
* Static & Media File Management
* Database Handling with Django ORM

---

## Author

Made as a fun college project by a BCA student passionate about web development and backend technologies.

---

## License

This project is for educational and learning purposes.
