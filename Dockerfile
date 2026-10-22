# 1. Base Image: Start from a minimal official Python Linux image
FROM python:3.11-slim

# 2. Working Directory: Create /app inside the container and switch to it
WORKDIR /app

# 3. Copy our app.py file into the container's /app folder
COPY app.py .

# 4. Inform Docker that the app listens on port 5000
EXPOSE 5000

# 5. The startup command when the container launches
CMD ["python", "app.py"]
