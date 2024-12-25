# Patima Android App Backend

## Overview

The backend for the Patima Android app is built using Django and Django REST Framework (DRF). It handles API calls, user-based authentication, JWT token authentication, and interacts with a MySQL database. Additionally, the application includes a mail server for sending emails.

## Features

- **User-Based Authentication**: Secure user authentication.
- **JWT Token Authentication**: Token-based authentication for API security.
- **MySQL Database**: Robust database management.
- **Mail Server**: Email functionality for notifications and communications.

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django REST Framework (DRF)**: A powerful and flexible toolkit for building Web APIs.
- **MySQL**: A widely used open-source relational database management system.
- **JWT (JSON Web Tokens)**: For secure token-based authentication.

## Installation

### Prerequisites

- Python 3.8 or later
- MySQL 5.7 or later
- Node.js (for development dependencies)
- pipenv (for managing Python dependencies)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DumiduPramith/OnesandZeros-patima-backend-django.git
    cd patima-backend
    ```

2. **Set up a virtual environment and install dependencies**:
    ```bash
    pipenv install
    ```

3. **Configure .env file**


4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open a browser and navigate to `http://localhost:8000/`.

## Configuration

### Environment Variables

Create a `.env.prod` file in the root directory of the project and add the following environment variables:

```env
# Example .env file for Django project

# Email configuration
EMAIL_HOST_PASSWORD="your-email-host-password"
EMAIL_HOST_USER="your-email@example.com"

# Logging configuration
DJANGO_LOG_LEVEL="DEBUG"
DJANGO_LOG_FILE="django.log"

# Database configuration
DB_HOST="database-host"

# Django settings
SECRET_KEY="your-secret-key"
ALLOWED_HOSTS="your-allowed-hosts"

# File paths
RAW_IMAGE_SAVING_PATH="static/raw_images/"
PREDICTED_IMAGE_SAVING_PATH="static/predicted_images/"
PROFILE_PICTURE_SAVING_PATH="static/profile_pictures/"

```

## Contributing

We welcome contributions to the Patima Admin Panel. Please follow these steps to contribute:

1. **Fork the repository**:
    ```bash
    git fork https://github.com/DumiduPramith/OnesandZeros-patima-backend-django.git
    ```

2. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes and commit them**:
    ```bash
    git commit -m "Add your commit message here"
    ```

4. **Push to the branch**:
    ```bash
    git push origin feature/your-feature-name
    ```

5. **Create a pull request**: Describe your changes and submit the pull request.


## Contact

For any inquiries or issues, please contact us at dumidu42@gmail.com.
