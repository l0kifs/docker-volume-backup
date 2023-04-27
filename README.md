# docker-volume-backup
## Setup
1. Clone repository
    ```bash
   git clone --no-local https://github.com/l0kifs/docker-volume-backup.git
    ```
2. Move to `src` directory
    ```bash
   cd docker-volume-backup/src/
    ```
3. Build the Docker image using the following command:
    ```bash
    docker build -t backup-service .
    ```
    This command will build the Docker image based on the Dockerfile in the current directory 
    and tag it as backup-service.
4. Run the Docker container using the following command:
    ```bash
   docker run -d \
       --restart=unless-stopped \
       --name=backup-service \
       --volumes-from <backup_container_name> \
       -v <destination_path>:/app/persistent_data \
       -e SOURCE_DIR=<backup_source_path> \
       -e BACKUP_INTERVAL=24 \
       -e BACKUPS_NUMBER=2 \
       backup-service
    ```
   Set the environment variables. All variables described in the `env_vars.py` file
