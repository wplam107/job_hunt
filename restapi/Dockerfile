# Pull official Python image
FROM python:3.7

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /app/backend

# Install Python dependencies
COPY requirements.txt /app/backend
RUN pip3 install --upgrade pip -r requirements.txt

# Add the rest of the code
COPY . /app/backend/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]