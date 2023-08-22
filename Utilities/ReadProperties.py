import configparser

config = configparser.RawConfigParser()
config.read("D:\\Software Testing\\TK PhpTravels\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get("common info", "Url")
        return url

    @staticmethod
    def get_email():
        email = config.get("common info", "Email")
        return email

    @staticmethod
    def get_pwd():
        pwd = config.get("common info", "Password")
        return pwd
