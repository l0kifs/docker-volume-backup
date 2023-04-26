import configparser
import logging.config
import os
from datetime import datetime
from os import path
import tarfile
from dataclasses import dataclass
from time import sleep

current_dir = path.dirname(path.abspath(__file__))
logging_conf_file = path.join(current_dir, 'persistent_data', 'config', 'logging.conf')
config_ini_file = path.join(current_dir, 'persistent_data', 'config', 'config.ini')
backups_dir = path.join(current_dir, 'persistent_data', 'backups')

logging.config.fileConfig(logging_conf_file)
log = logging.getLogger(__name__)


def get_config():
    @dataclass
    class Config:
        source_dir: str
        number_of_backups: int
        backup_interval: int

    try:
        parser = configparser.ConfigParser()
        parser.read(config_ini_file)
        config = Config(
            source_dir=parser['Backup']['source_dir'],
            number_of_backups=int(parser['Backup']['number_of_backups']),
            backup_interval=int(parser['Backup']['backup_interval'])
        )
        return config
    except Exception:
        log.exception("Could not read config.ini", exc_info=True)
        raise Exception("Could not read config.ini")


def make_tarfile(output_filename, source_dir):
    try:
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        return output_filename
    except Exception:
        log.exception(f'Could not create tarfile "{output_filename}" from source "{source_dir}"', exc_info=True)
        raise Exception(f'Could not create tarfile "{output_filename}" from source "{source_dir}"')


def rotate_backups(number_of_backups: int):
    try:
        files = os.listdir(backups_dir)
        files = [file for file in files if file.endswith(".tar.gz")]
        files.sort(key=lambda x: datetime.strptime(x.replace('backup_', '').replace('.tar.gz', ''), "%Y-%m-%dT%H-%M-%S"))

        if len(files) >= number_of_backups:
            files_to_remove = len(files)-number_of_backups+1
            for i in range(files_to_remove):
                os.remove(os.path.join(backups_dir, files[i]))
                log.info(f"Removed {files[i]}")
    except Exception:
        log.exception("Could not rotate backups", exc_info=True)
        raise Exception("Could not rotate backups")


if __name__ == "__main__":
    config = get_config()

    while True:
        rotate_backups(config.number_of_backups)
        backup_name = f"backup_{datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S')}.tar.gz"
        output_filename = make_tarfile(path.join(backups_dir, backup_name), config.source_dir)
        sleep(config.backup_interval*60*60)
