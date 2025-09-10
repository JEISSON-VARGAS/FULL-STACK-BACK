import yaml

class Config:
    def __init__(self, config_file="application.yml"):
        with open(config_file, "r") as f:
            self.cfg = yaml.safe_load(f)

    def get_database_uri(self):
        db = self.cfg["database"]
        return f"{db['driver']}://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['name']}?ssl_ca=certificado.pem"

    def get_debug(self):
        return self.cfg["app"]["debug"]

    def get_port(self):
        return self.cfg["app"]["port"]
