
# HarmonyIT Django Project

HarmonyIT is a professional Django-based web application designed to showcase a company’s services and projects. It features a multi-page website including a homepage, an about page, a recommendations page with testimonials, and a contact page with an interactive form. The project is built using Django, Bootstrap, and custom CSS to deliver a modern, responsive user experience.

## Features

- **Multi-Page Layout:**  
  - **Home:** Displays an overview of services, client logos, and a call-to-action.
  - **About:** Provides detailed information about the company, its expertise, and its team.
  - **Recommendations:** Showcases testimonials and feedback from past projects and clients.
  - **Contact:** Includes a contact form that supports AJAX requests and saves submissions to the database.

- **Responsive Design:**  
  Uses Bootstrap and custom styles to ensure the site looks great on all devices.

- **Contact Form:**  
  A fully integrated form that uses Django’s forms and models to handle user inquiries and store them in the database.

- **templates/harmonyApp/**  
  Contains the HTML templates for each page (Home, About, Contact, and Recommendations).

- **forms.py**  
  Defines the `ContactForm` that is used on the Contact page.

- **models.py**  
  Contains the `Contact` model which stores user inquiries.

- **urls.py & views.py**  
  Handle the routing and logic for displaying pages and processing form submissions.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone [https://your-repository-url.git](https://github.com/gilos123/Hamrmony)
   cd harmonyIT
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   Ensure you have a `requirements.txt` file (include Django and other dependencies), then run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server:**

   ```bash
   python manage.py runserver
   ```

   Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Configuration

- **Settings:**  
  Adjust your project settings in `settings.py` (e.g., database configuration, static files settings, etc.).

- **Static Files & Templates:**  
  The project uses Django’s templating system and static files management. Ensure your static files are correctly collected if you deploy the project.


## Author

Developed by **gilos123**

