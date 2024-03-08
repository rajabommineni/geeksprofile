# Start from the python image on Docker Hub
FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app
EXPOSE 5000
# The script to run when the container starts
CMD ["flask", "run", "--host", "0.0.0.0"]

