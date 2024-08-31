import os

class Config:
    def __init__(self):
        self.config = self._load_config()

    def _load_config(self):
        config = {}
        if os.path.exists('config.ini'):
            with open('config.ini', 'r') as f:
                for line in f:
                    key, value = line.strip().split('=')
                    config[key] = value
        return config

    def get_config(self, section, key):
        """
        Gets a configuration setting.

        :param section: The section of the configuration setting
        :param key: The key of the configuration setting
        :return: The value of the configuration setting
        """
        return self.config.get(f"{section}_{key}")

    def set_config(self, section, key, value):
        """
        Sets a configuration setting.

        :param section: The section of the configuration setting
        :param key: The key of the configuration setting
        :param value: The value of the configuration setting
        """
        self.config[f"{section}_{key}"] = value
        with open('config.ini', 'w') as f:
            for key, value in self.config.items():
                f.write(f"{key}={value}\n")

def get_config():
    return Config()
