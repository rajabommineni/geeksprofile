# Start from the mysql image on Docker Hub
FROM mysql:8
# The script to run when the container starts
ADD geekprofile.sql /docker-entrypoint-initdb.d
EXPOSE 3306

