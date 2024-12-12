# Artonia

## Overview
**Artonia** is a Django-based platform where users can attend workshops led by skilled instructors in art painting and macrame creation. The platform also allows users to showcase their creations, enabling them to share their artwork with others and sell them through a bidding system. Additionally, users can engage with the platform by liking shared content.

### Target Audience
The platform is designed for end-users, particularly those interested in art and craft activities such as painting and macrame creation.

## Technology Stack
The project uses the following technologies and libraries:
- **asgiref**: 3.8.1
- **Django**: 5.1.3
- **django-bootstrap5**: 24.3
- **django-crispy-forms**: 2.3
- **gunicorn**: 23.0.0
- **packaging**: 24.2
- **psycopg-binary**: 3.2.3
- **psycopg2**: 2.9.10
- **sqlparse**: 0.5.1
- **tzdata**: 2024.2

## Setup and Installation

### Prerequisites
Ensure you have the following installed on your system:
- **Python**: 3.11
- **Django**: 5.1.3
- **PostgreSQL**: A running instance of PostgreSQL database.

### Installation Steps
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/YordanDobrev/PythonWEB/tree/main/Artonia_v2
   cd artonia
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate   # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the PostgreSQL database in your Django settings file (`settings.py`). Update the `DATABASES` section with your database credentials:
   ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': config('DB_NAME'),
             'USER': config('DB_USER'),
             'PASSWORD': config('DB_PASSWORD'),
             'HOST': config('DB_HOST', default='localhost'),
             'PORT': config('DB_PORT', default='5432'),
         }
     }
   ```

5. Copy the `env.template` file and fill in the required information:
   ```bash
   cp env.template .env
   ```
   Ensure all necessary environment variables such as database credentials and secret keys are set correctly in the `.env` file.

6. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application by visiting `localhost:8000` in your web browser.

## Core Features
- **Workshops**: Users can browse and attend workshops hosted by instructors.
- **Artwork Sharing**: Users can share their Art Paintings and Macrame creations.
- **Bidding System**: Sell artwork to the highest bidder.
- **Like Functionality**: Engage with the platform by liking shared content.

## Dependencies
All dependencies are listed in the `requirements.txt` file:
```
asgiref==3.8.1
Django==5.1.3
django-bootstrap5==24.3
django-crispy-forms==2.3
gunicorn==23.0.0
packaging==24.2
psycopg-binary==3.2.3
psycopg2==2.9.10
sqlparse==0.5.1
tzdata==2024.2
```

## Usage
1. After starting the server, users can create an account or log in to access the features.
2. Admin users can manage workshops, artwork submissions, and user activities through the admin interface (`/admin`).

## Contribution Guidelines
- Contributions are welcome! Please fork the repository, make changes, and submit a pull request.
- Ensure your code follows PEP 8 standards and includes tests where applicable.

## License
This project is licensed under the MIT License.

## Contact Information
For questions, issues, or feedback, feel free to reach out via GitHub or email at petolisko1@gmail.com.

