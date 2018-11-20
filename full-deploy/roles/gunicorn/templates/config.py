# -*- coding: utf-8 -*-


class Config:
    SECRET_KEY = "hard to guess string"
    JSON_AS_ASCII = False

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG=True
    

class TestConfig(Config):
    DEBUG=True


class ProConfig(Config):
    DEBUG=False


config = {
    "dev": DevConfig,
    "testing": TestConfig,
    "production": ProConfig,
    "default": DevConfig,
}
