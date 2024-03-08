## Getting started

Dockerizing the APP inspired from <https://www.geeksforgeeks.org/profile-application-using-python-flask-and-mysql/>

# Local workstation - only UI works unless you've an mysql DB hosted on your local machine
flask run --host=0.0.0.0

# Build the docker image for the app/ui
docker build -t geeksprofile .

# For Docker container hosted on docker desktop to connect with DB hosted on local machine set the `MYSQL_HOST` as `host.docker.internal`
docker run -d -p 5000:5000 --name geeks-test -e DB_HOST=host.docker.internal geeksprofile

# Build the mysql database `geekprofile` docker image
cd database/
docker build -t geekprofile-db .

# if you want to connect to the db instance from local machine, expose the port
docker run -d -p 3306:3306 --name geek-db -e MYSQL_ROOT_PASSWORD=root geekprofile-db

# Otherwise, don't expose the port.
docker run -d --name geek-db -e MYSQL_ROOT_PASSWORD=root geekprofile-db

# How containers deployed on docker desktop communicate
```
By default, app container and db container will be in the bridge network.

There are two ways for a container hosted on Docker Desktop to communicate with MySQL
hosted on a different container in Docker Desktop:

1. Using the bridge network: By default, when you start a container on Docker Desktop, it is assigned to the bridge network. This network allows containers to communicate with each other and with the host machine. To communicate with MySQL, you will need to know the IP address of the MySQL container. You can get this by running the following command:
    
    `docker inspect <mysql_container_name>`

    Then spin up the app container with IP address as DB_HOST
    `docker run -d -p 5001:5000 --name geeks-test-1 -e DB_HOST=172.17.0.3 geeksprofile`

2. Using a user-defined network: You can also create a user-defined network and add both the MySQL container and the container that needs to communicate with MySQL to the network. This can be useful if you want to isolate the MySQL container from other containers on Docker Desktop. To create a user-defined network, run the following command:
    
    `docker network create geek-profile`

    Add both the app container and DB container to above network
    `docker network connect geek-profile <container_name>`

    Started another app container with host name as DB container name
        `docker run -d -p 5002:5000 --name geeks-test-2 -e DB_HOST=geek-db geeksprofile`
    and attached it to the same above network.

    Now, there are 2 app containers connected to single instance of mysql.
```

# Email API
    Build docker image for email server
        `docker build -t rajabops/emailserver .`
    Spin up a container hosting email server
        ` docker run -d -p 5011:5000 --name email-cont rajabops/emailserver

# 2 APIs and 1 Database architecture

    `2apis` is an updated frontend API(geeksprofile) that interacts with email server

    `docker run -d -p 5005:5000 --name 2apiscont -e EMAIL_SERVER=email-cont -e DB_HOST=geek-db 2apis`

    Connect all there containers(2 APIs and Database) into single network
        `docker network connect 2apis-network 2apiscont`



