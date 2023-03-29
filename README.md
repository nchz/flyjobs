# Flyjobs

A simple Django project with basic concepts for a job posting platform.


## Dependencies

- Docker
- docker-compose


## Setup

Copy the `.env-template` file into a new one called `.env`.

To quickly try the API, use the start script:
```bash
./start.sh
```

To run a production like setup, use Docker:
```bash
# Setup containers.
docker-compose up --build

# Setup database.
docker-compose exec web ./migrations.sh

# Create admin user.
docker-compose exec web python manage.py createsuperuser

# Collect static files for Admin and Browsable API interfaces.
docker-compose exec web python manage.py collectstatic
```

Then go to http://localhost/ to explore the API.
