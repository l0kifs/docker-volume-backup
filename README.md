# docker-volume-backup
## Setup
1. Build the Docker image using the following command:
    ```bash
    docker build -t backup-service .
    ```
    This command will build the Docker image based on the Dockerfile in the current directory 
    and tag it as backup-service.
2. Run the Docker container using the following command:
    ```bash
   docker run -d \
       --restart=unless-stopped \
       --volumes-from <backup_container_name> \
       -v <destination_path>:/app/persistent_data \
       backup-service
    ```
