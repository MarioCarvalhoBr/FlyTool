### 1. Basic Settings and Initialization
1. **`app/config.py`**: Global configuration file for the project.
2. **`app/__init__.py`**: Initializes the Flask application and configures extensions.
3. **`.env` and `.flaskenv`**: Files for environment variables necessary for configuration and local execution.

### 2. Data Models
4. **`app/models/__init__.py`**: Prepares the models package.
5. **`app/models/models.py`**: Defines the SQLAlchemy models for your database.

### 3. Forms
6. **`app/forms/__init__.py`**: Prepares the forms package.
7. **`app/forms/forms.py`**: Defines the Flask-WTF forms used for user data entry.

### 4. Routes and Controllers
8. **`app/routes/__init__.py`**: Prepares the routes package.
9. **`app/routes/auth.py`**: Implements routes for authentication (login, logout, registration).
10. **`app/routes/home.py`**: Routes for the home page and other routes related to main navigation.
11. **`app/routes/product.py`**: Routes for creating, viewing, editing, and deleting products.

### 5. Templates
12. **`app/templates/base.html`**: Base template for the site that includes common elements such as header, footer, and links to CSS/JS.
13. **`app/templates/index.html`**: Home page of the site.
14. **`app/templates/auth/login.html`**: Login page.
15. **`app/templates/auth/register.html`**: Registration page.
16. **`app/templates/product/add.html`**: Form for adding products.
17. **`app/templates/product/edit.html`**: Form for editing products.
18. **`app/templates/product/list.html`**: List of available products.
19. **`app/templates/user/settings.html`**: User settings page.

### 6. Static Resources
20. **`app/static/css/styles.css`**: CSS file for custom styling.
21. **`app/static/js/script.js`**: JavaScript scripts for interactive functionalities.

### 7. Utilities and Others
22. **`app/utils/helpers.py`**: Helper functions and utilities that can be used throughout the application.

### 8. Execution and Maintenance
23. **`run.py`**: Script to start the Flask server.
24. **`requirements.txt`**: List of dependencies to be installed with pip.
25. **`README.md`**: Basic documentation of the project.
26. **`LICENSE`**: License file for the project.
