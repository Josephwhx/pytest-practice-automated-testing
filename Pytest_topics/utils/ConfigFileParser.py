import configparser
from pathlib import Path

class ConfigFileParser():
    cfgFile = 'qa.ini'
    cfgFileDirectory = 'config'

    config = configparser.ConfigParser()


    def __init__(self, cfg=cfgFile):
        self.cfgFile = cfg
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDirectory).joinpath(self.cfgFile)
        self.config.read(self.CONFIG_FILE)

    def getGmailUrl(self):
        return (self.config['gmail']['url'])

    def getGmailUser(self):
        return (self.config['gmail']['user'])

    def getGmailPass(self):
        return (self.config['gmail']['pass'])
    
if __name__ == '__main__':
    config = ConfigFileParser()
    print(config.getGmailUser())