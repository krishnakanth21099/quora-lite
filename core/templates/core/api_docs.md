# Quora Website API Documentation

## Authentication

### Login
- **URL**: `/login/`
- **Method**: `POST`
- **Form Data**:
  - `username`: User's username
  - `password`: User's password
- **Response**: Redirects to home page on success

### Register
- **URL**: `/register/`
- **Method**: `POST`
- **Form Data**:
  - `username`: Desired username
  - `email`: User's email
  - `password1`: Password
  - `password2`: Password confirmation
  - `first_name`: User's first name
  - `last_name`: User's last name
  - `icon`: User's profile icon
- **Response**: Redirects to home page on success

## Questions

### List Questions
- **URL**: `/`
- **Method**: `GET`
- **Response**: List of questions with their answer counts
- **Example Response**:
  ```json
  {
    "questions": [
      {
        "id": 1,
        "title": "Sample Question",
        "content": "Question content",
        "created_by": "username",
        "created_at": "2025-04-08T01:57:01+05:30",
        "answer_count": 5
      }
    ]
  }
  ```

### Create Question
- **URL**: `/question/new/`
- **Method**: `POST`
- **Authentication**: Required
- **Form Data**:
  - `title`: Question title
  - `content`: Question content
- **Response**: Redirects to question detail page

### View Question
- **URL**: `/question/<id>/`
- **Method**: `GET`
- **Parameters**:
  - `id`: Question ID
- **Response**: Question details with answers

## Answers

### Add Answer
- **URL**: `/question/<id>/`
- **Method**: `POST`
- **Authentication**: Required
- **Form Data**:
  - `content`: Answer content
- **Response**: Redirects to question detail page

### Like/Unlike Answer
- **URL**: `/answer/<id>/like/`
- **Method**: `POST`
- **Authentication**: Required
- **Parameters**:
  - `id`: Answer ID
- **Response**:
  ```json
  {
    "liked": true|false,
    "like_count": 42
  }
  ```
