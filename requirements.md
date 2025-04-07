# Quora-Lite Django Project

## 📘 Overview

**Quora-Lite** is a minimal, backend-focused Q&A platform inspired by Quora. It allows users to register, post questions, answer other users' questions, and like answers. The goal is to implement core functionality using Django, Django Forms

---

## ✅ Functional Requirements

### 1. User Authentication
- Register (username, email, password)
- Login
- Logout
- Use Django’s built-in auth system

### 2. Question Management
- Users can create new questions
- Each question has: `title`, `description`, `created_by`, `created_at`
- All questions visible to logged-in users
- List view of all questions (sorted newest first)

### 3. Answer Management
- Users can post answers to any question
- Each answer has: `content`, `question`, `answered_by`, `created_at`
- Multiple answers per question allowed
- Answers are displayed under respective questions

### 4. Likes
- Users can like any answer (once per answer)
- Track likes per answer
- Display total like count for each answer

### 5. Views & Pages
- Home: All questions (with links to detail pages)
- Question detail: Question + its answers + answer form
- New question page: Form to post a question
- Like button next to each answer (no JS needed — simple form POST)
- Register/Login/Logout pages

### 6. Optional API Support (Bonus)
- Expose REST API endpoints using Django REST Framework (DRF)
- Add interactive Swagger UI with `drf-yasg` or `drf-spectacular`

---

## ⚙️ Tech Stack

- **Backend**: Python, Django
- **API**: Django REST Framework (optional)
- **Frontend**: Basic Django templates (no styling required)
- **Database**:  PostgreSQL
- **Forms**: Django Forms
- **Auth**: Django built-in user model
- **API Docs**: Swagger/OpenAPI (`drf-yasg` or `drf-spectacular`)

---

## 🗂 Models Overview

### `User` 
| Field        | Type       |
|--------------|------------|
| username     | CharField  |
| email        | EmailField |
| password     | Password   |(encrypted)
| created_at   | DateTime   |
| icon         | ImageField |
| first_name   | CharField  |
| last_name    | CharField  |
| last_login   | DateTime   |


### `Question`
| Field        | Type       |
|--------------|------------|
| title        | CharField  |
| description  | TextField  |
| created_by   | FK → User  |
| created_at   | DateTime   |

### `Answer`
| Field        | Type        |
|--------------|-------------|
| question     | FK → Question |
| content      | TextField   |
| answered_by  | FK → User   |
| created_at   | DateTime    |
| like_count   | Integer     |


### `AnswerLike`
| Field        | Type         |
|--------------|--------------|
| answer       | FK → Answer  |
| liked_by     | FK → User    |
| liked_at     | DateTime     |

---

## 🚦 URL Endpoints

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Homepage – list all questions |
| `/questions/<id>/` | GET | View a question + its answers |
| `/questions/new/` | GET, POST | Create a new question |
| `/answers/<id>/like/` | POST | Like an answer |
| `/register/` | GET, POST | User registration |
| `/login/` | GET, POST | User login |
| `/logout/` | GET | User logout |

---