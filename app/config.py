import os


class ConfigBase:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app():
        print("starting aplication...")


class DevelopmentConfig(ConfigBase):
    DEBUG = True
    ASSETS_DEBUG = True

    def __init__(self):
        super().__init__()
        print(
            "THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION."
        )
        self.SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL")


class TestingConfig(ConfigBase):
    TESTING = True
    WTF_CSRF_ENABLED = False

    def __init__(self):
        print(
            "THIS APP IS IN TESTING MODE.  \
                YOU SHOULD NOT SEE THIS IN PRODUCTION."
        )
        self.SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")


class ProductionConfig(ConfigBase):
    DEBUG = False
    USE_RELOADER = False

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class Config():
    def __new__(cls,environment='default'):
        config_classes = {
            "dev": DevelopmentConfig,
            "test": TestingConfig,
            "prod": ProductionConfig,
            "default": DevelopmentConfig,
        }
        # Escolher a classe de configuração com base no ambiente
        config_class = config_classes.get(environment)
        # Cria e retorna uma instância da classe de configuração selecionada
        return config_class()

        