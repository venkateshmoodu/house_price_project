# Use official Python image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy all project files into container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]