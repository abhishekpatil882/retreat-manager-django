# Retreat Manager

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies: 'pip install -r requirements.txt'
4. Configure the PostgreSQL database in 'retreat_manager/settings.py'
5. Run migrations: 'python manage.py migrate'
6. Run the development server: 'python manage.py runserver'

## Environment Variables

- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_HOST
- DATABASE_PORT

## API Endpoints

- 'GET /api/retreats/'
- 'POST /api/book/'
