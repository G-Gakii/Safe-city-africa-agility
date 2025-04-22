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

- git clone git@github.com:G-Gakii/Safe-city-africa-agility.git
- cd Safe-city-africa-agility

2. Set up the virtual environment:`python -m venv env`
3. activate virtial environment : `source env/bin/activate` # On Windows: `env\Scripts\activate`

4. Install dependencies:`pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser : `python manage.py createsuperuser`
7. Run the server: `python manage.py runserver`

## API Endpoints

### User Management

- `GET	/api/user/register/` Retrieve all registered users
- `POST	/api/user/register/` Register a new user
- `POST	/api/user/login/` Obtain authentication token
- `GET	/api/user/users/<int:pk>/` Retrieve user details
- `PUT	/api/user/users/<int:pk>/` Update user details
- `DELETE	/api/user/users/<int:pk>/` Delete a user

### Reports

- `GET	/api/report/` List all reports
- `POST	/api/report/` Create a new report
- `GET	/api/report/report/<uuid:pk>/` Retrieve a specific report
- `PUT	/api/report/report/<uuid:pk>/` Update a report
- `DELETE	/api/report/report/<uuid:pk>/` Delete a report

### Notifications

- `GET	/api/notifications/recent/` Retrieve recent unread notifications
- `GET	/api/notifications/all/` Retrieve all notifications with filtering
- `POST	/api/notifications/mark-read/<uuid:notification_id>/` Mark notification as read
- `GET	/api/notifications/unread-count/` Get the count of unread notifications

### Analytics

- `GET	/api/analytics/` Retrieve analytics with filtering by user or category

### Authentication

Most API endpoints require authentication using JWT. Obtain a token by logging in and include it in requests as:
http
Authorization: Bearer <your_token>

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit changes (git commit -m "Added a new feature").
4. Push to your fork (git push origin feature-branch).
5. Open a pull request.
