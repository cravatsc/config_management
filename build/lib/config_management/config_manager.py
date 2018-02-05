class ConfigManager:
    config = {}

    def __init__(self, file):
        """Constructor for config manager"""
        self.read_file_to_dict(file)

    def read_file_to_dict(self, infile):
        with open(infile) as conf:
            for line in conf.read().splitlines():
                (key, value) = line.split('=')
                self.config[key] = value

    def get(self, key):
        return self.config.get(key)
