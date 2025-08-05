# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /block/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 to the outside world
EXPOSE 8501

# Define environment variable
ENV PORT=8501

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
