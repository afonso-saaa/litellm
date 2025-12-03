import yaml
from ldap3 import Server, Connection, ALL

class LdapAuth:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r") as f:
            cfg = yaml.safe_load(f)["ldap"]

        self.host = cfg["host"]
        self.port = cfg["port"]
        self.base_dn = cfg["base_dn"]
        self.domain_suffix = cfg["domain_suffix"]

        self.server = Server(self.host, port=self.port, get_info=ALL)

    def authenticate(self, username, password):
        """
        Autentica usando UPN
        """
        user_dn = f"{username}{self.domain_suffix}"

        try:
            conn = Connection(
                self.server,
                user=user_dn,
                password=password,
                auto_bind=True
            )
            conn.unbind()
            return True

        except Exception:
            return False


def ldap_login(username, password):
    auth = LdapAuth()
    return auth.authenticate(username, password)
