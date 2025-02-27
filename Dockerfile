FROM python:3.12-slim-bookworm

ARG APP_DIR=/usr/src/app

RUN apt-get update -y \
    && apt-get install libpq-dev gcc -y \
    && rm -rf /var/lib/apt/lists/*

# Create application directories and user
RUN mkdir -p ${APP_DIR} && \
    mkdir ${APP_DIR}/staticfiles \
    ${APP_DIR}/logs \
    && useradd --create-home appusr

# Make app as working directory
WORKDIR ${APP_DIR}

# Install requirements
COPY requirements.txt ${APP_DIR}
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN chown -R appusr:appusr ${APP_DIR}
USER appusr

# Copy rest of application
COPY . ${APP_DIR}

# Run the start script
CMD ["gunicorn", "-w", "4", "-b", ":8000", "restapi.wsgi"]
