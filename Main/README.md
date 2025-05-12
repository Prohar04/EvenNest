# Django Project

This is a Django web application project.

## Setup

1. Ensure you have Python installed
2. Activate the virtual environment:
   ```
   .\venv\Scripts\activate
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

- `core/` - Main application directory
- `myproject/` - Project configuration directory
- `manage.py` - Django's command-line utility for administrative tasks