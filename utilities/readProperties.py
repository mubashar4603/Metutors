import configparser
config = configparser.RawConfigParser()
config.read("/home/mubashar4603/PycharmProjects/Metutors/Configurations/config.ini")
class ReadConfig():
    @staticmethod
    def getAppURL():
        url = config.get('common info', 'baseURL')
        return url
    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username
    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password