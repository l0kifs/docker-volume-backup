import os


class EnvVars:
    @staticmethod
    def source_dir() -> str:
        """
        Backup source directory.
        Requires that SOURCE_DIR environment variable is set.
        For example /var/jenkins_home
        :return:
        """
        value = os.environ.get('SOURCE_DIR')
        return value

    @staticmethod
    def backup_interval() -> int:
        """
        Backup interval in hours.
        Default value is 24 hours.
        :return:
        """
        value = os.environ.get('BACKUP_INTERVAL', '24')
        return int(value)

    @staticmethod
    def backups_number() -> int:
        """
        Number of backup files to store.
        Default value is 2.
        :return:
        """
        value = os.environ.get('BACKUPS_NUMBER', '2')
        return int(value)
