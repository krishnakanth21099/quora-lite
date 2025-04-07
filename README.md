# Quora Lite - Q&A Platform

## Project Overview

Quora Lite is a lightweight Question and Answer platform built with Django, providing core Q&A functionality with user authentication, question posting, answering, and liking features.

## Features

- User Registration and Authentication
- Create, View, and Interact(answer) with Questions
- Post Answers to Questions
- Like Answers
- Responsive Design with Django Forms and HTML

## Prerequisites

- Python 3.8+
- pip (Python Package Manager)
- PostgreSQL

## Technology Stack

- Backend: Django 5.2
- Database: PostgreSQL
- Frontend: HTML, Bootstrap 5
- API Documentation: Swagger/ReDoc

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/krishnakanth21099/quora-lite.git
cd quora-lite
```

### 2. Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Configuration

1. Create a PostgreSQL database
2. Create a `.env` file in the project root with the following configurations:

```
SECRET_KEY=your_django_secret_key
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver {host}:{port}
```

## API Exploration

### API Documentation

Access API documentation: `http://{host}:{port}/api-docs/`

### API
Access API: `http://{host}:{port}/`

### Available Endpoints

1. **Authentication**
   - `/register/`: User registration
   - `/login/`: User login
   - `/logout/`: User logout

2. **Questions**
   - `/question/new/`: Create a new question (login required)
   - `/question/<pk>/`: View question details and post answers

3. **Answers**
   - `/answer/<answer_id>/like/`: Like/Unlike an answer (login required)

## Contact

Krishna Kanth Ravi Kumar - +91 9177858032 | krishnakanthr99@gmail.com

Project Link: [https://github.com/krishnakanth21099/quora-lite](https://github.com/krishnakanth21099/quora-lite)
