# Django Coffee App

A simple Django project with a REST API for managing coffee entries. This project includes a public endpoint for listing all coffees and individual pages to view coffee details.

## Features

- **REST API**: List and retrieve coffee entries.
- **HTML Frontend**: Fetch and display coffee data using jQuery.
- **Detail View**: View detailed information about each coffee.
- **CSS Animations**: Smooth animations for a better user experience.

## Requirements

- Python 3.x
- Django 3.x or 4.x
- Django REST Framework

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/AhmedFathyMohamed10/Coffee-api-with-frontend-using-JQuery-to-fetch-the-apis.git
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Project Structure
``` coffee_project/
│
├── project/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── coffee/
├  ├── templates/
├    ├── index.html
│    └── coffee_details.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── migrations/
│
├── media/
│ ├── coffee_images/
│
├── static/
│ ├── css/
│ │ └── styles.css
│ ├── js/
│ └── script.js
│
├── manage.py
├── README.md
```

## Usage

### REST API

- **List Coffees:**
  ```bash
  GET /api/coffees/
### Frontend
Visit the home page at http://127.0.0.1:8000/ to view the coffee list.
Click on a coffee name to view its details.
