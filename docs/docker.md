# Docker Setup and Usage

This document provides instructions for setting up and running the project in Docker.

## Prerequisites

- Docker installed on your machine. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

## Building the Docker Image

To build the Docker image for the project, run the following command in the root directory of the project:

```bash
docker build -t project-boilerplate .
```

This command will create a Docker image named `project-boilerplate` based on the Dockerfile in the root directory.

## Running the Docker Container

To run the Docker container, use the following command:

```bash
docker run -p 8000:8000 project-boilerplate
```

This command will start a Docker container from the `project-boilerplate` image and map port 8000 of the container to port 8000 on your host machine.

You can now access the application by navigating to `http://localhost:8000` in your web browser.

## Stopping the Docker Container

To stop the Docker container, you can use the `docker ps` command to find the container ID and then use the `docker stop` command:

```bash
# List running containers
docker ps

# Stop the container
docker stop <container_id>
```

Replace `<container_id>` with the actual container ID from the `docker ps` output.

## Removing the Docker Container

To remove the Docker container, use the `docker rm` command:

```bash
docker rm <container_id>
```

Replace `<container_id>` with the actual container ID.

## Removing the Docker Image

To remove the Docker image, use the `docker rmi` command:

```bash
docker rmi project-boilerplate
```

This command will remove the `project-boilerplate` image from your local Docker repository.

## Additional Docker Commands

Here are some additional Docker commands that may be useful:

- List all Docker images: `docker images`
- List all Docker containers (including stopped ones): `docker ps -a`
- View logs of a running container: `docker logs <container_id>`
- Execute a command inside a running container: `docker exec -it <container_id> <command>`

Replace `<container_id>` with the actual container ID and `<command>` with the command you want to execute.

## Docker Compose

If you have a `docker-compose.yml` file in your project, you can use Docker Compose to manage multi-container applications. Here are some common Docker Compose commands:

- Start all services defined in the `docker-compose.yml` file: `docker-compose up`
- Start all services in detached mode: `docker-compose up -d`
- Stop all running services: `docker-compose down`
- View logs of all services: `docker-compose logs`
- Execute a command inside a running service container: `docker-compose exec <service_name> <command>`

Replace `<service_name>` with the name of the service and `<command>` with the command you want to execute.

## Conclusion

This document provides a basic overview of how to set up and run the project in Docker. For more advanced usage and configuration options, refer to the [Docker documentation](https://docs.docker.com/).
