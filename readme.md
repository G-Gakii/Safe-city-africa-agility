# Safe City API

Safe City is a Django REST Framework-based backend system designed to enhance city safety through user-generated reports and notifications. It provides endpoints for managing reports, user registration, notifications, and analytics.

## Features

- User registration and authentication
- Report creation, retrieval, updating, and deletion
- Notification system for unread alerts
- Analytics for user activity tracking

## Technologies Used

- Django & Django REST Framework
- PostgreSQL (or any preferred database)
- Django Filters for search functionality
- JWT-based authentication
- Docker (optional for containerization)

## Installation

1. **Clone the repository**

- git clone https://github.com/your-repo/safe-city.git
- cd safe-city

2. Set up the virtual environment

- python -m venv env
- source env/bin/activate # On Windows: `env\Scripts\activate`

3. Install dependencies

- pip install -r requirements.txt
- Run migrations: `python manage.py migrate`
- Create a superuser : `python manage.py createsuperuser`
- Run the server: `python manage.py runserver`
