import configparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\HP\\Desktop\\Testing\\CT17\\AutomationProject\\OrangeHRM\\Configuration\\config.ini")

class Readconfig():
    @staticmethod
    def geturl():
        url = config.get('common info', 'URL')
        return url

    @staticmethod
    def getemail():
        mail = config.get('common info', 'Email')
        return mail

    @staticmethod
    def getpassword():
        password = config.get('common info', 'Password')
        return password