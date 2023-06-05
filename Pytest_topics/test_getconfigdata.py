from utils.myconfigparser import *
from utils.ConfigFileParser import ConfigFileParser


config = ConfigFileParser('qa.ini')

def test_getgmailurl():
    print(getGmailUrl())


def test_getgmailUser():
    print(config.getGmailUser())