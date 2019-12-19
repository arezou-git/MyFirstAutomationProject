from configparser import ConfigParser


class Config:

    def readConfigData(self, section, key):
        config = ConfigParser()
        config.read('../Files/ConfigFile/config.cfg')
        return config.get(section, key)