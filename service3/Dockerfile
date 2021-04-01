# Use Python 3.6 or later as a base image
FROM python:3.7
# Copy contents into image
WORKDIR /app

COPY . .
# Install pip dependencies from requirements
RUN pip3 install -r requirements.txt
# Set YOUR_NAME environment variable
ENV YOUR_NAME="Kelvin"
# Expose the correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["python3", "app.py"]