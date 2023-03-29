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
# Collect static files for Admin and Browsable API interfaces.
python src/manage.py collectstatic

# Setup containers.
docker-compose up --build

# Setup database.
docker exec flyjobs_web "./migrations.sh"
```

Then go to http://localhost/ to explore the API.
