FROM python:3.9-slim

# Install necessary packages
RUN pip install Flask mysql-connector-python

# Copy the Python script (assuming it's named app.py)
COPY app.py app.py

# Expose port 8080 (as we set in the Python script)
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]