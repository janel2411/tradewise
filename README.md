# TradeWise Web Application (By Koo Kai Ze and Janel Ng)

## Overview

TradeWise is a web application designed to provide users with a seamless experience for managing their accounts. This README file outlines the progress made on the project, including the implementation of the home page, user sign-up, and login functionalities.

## Features

### Home Page
- A visually appealing home page with a user-friendly interface.
- Displays a welcome message and options to sign up or log in.

### User Sign-Up
- A sign-up form that collects user information such as name, email, username, and password.
- Upon successful sign-up, user data is stored in the database.
- After signing up, users are redirected to the home page to log in with a success message indicating that the account has been created.

### User Login
- A login form that allows existing users (who have accidentally clicked to create a new account) to log in using their username and password.
- Upon successful login, users are redirected to a welcome page that displays a personalised greeting with their username.

## Implementation Details

### Home Page
- Implemented using HTML and CSS for a clean and modern look.
- Contains links to the sign-up and login pages.

### Sign-Up Form
- HTML form with fields for name, email, username, and password.
- Backend logic in Django to handle form submission and user creation.
- Uses Django's built-in User model to store user data in our MongoDB database.
- Includes form validation to ensure unique usernames and emails.
- Displays success messages using Django's messaging framework.

### Login Form
- HTML form with fields for username and password.
- Backend logic in Django to authenticate users and manage sessions.
- Upon successful login, redirects to a personalized welcome page.

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/tradewise.git
   cd tradewise

- Create an activate the virtual environemnt needed for Python: python3 -m venv tradewise_env source tradewise_env/bin/activate
- Install the necessary packages: pip install -r requirements.txt
- Run the migrations: python manage.py migrate
- Collect the static files needed: python manage.py collectstatic
- Run the development server: python manage.py runserver
- Access using: http://127.0.0.1:8000/

Folder Structure
templates/  Contains the HTML templates for the project.
- index.html - Home page template.
- signup.html - Sign-up form template.
- login.html - Login form template.

static/css/ - Contains the CSS files for styling.
- index.css - Stylesheet for the home page.
- signup.css - Stylesheet for the sign-up page.
- login.css - Stylesheet for the login page.
  
tradewise/ - Django project settings and configurations.
- urls.py - URL routing for the project.
- views.py - View functions for handling requests.

Future Enhancements for MS 1
- Have designed our content and lesson structure for Chapter 1. Will build the lesson platform.
- Will install the quiz for Chapter 1 and build the XP Points System.

