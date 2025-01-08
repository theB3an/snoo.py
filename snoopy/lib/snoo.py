from snoopy.lib.ldap import get_ldap_connection
from snoopy.lib.get_SPNs import get_users_with_spns
from snoopy.lib.machine_account_quota import get_machine_account_quota
    
class snoo:
    def __init__(self, domain_controller, username, password, domain, logger):
        self.domain_controller = domain_controller
        self.username = username
        self.password = password
        self.domain = domain
        self.logger = logger

    def run(self):
        print("\n[+] Starting LDAP Connection to Domain Controller...")
        ldap_connection = get_ldap_connection(self.domain_controller, self.username, self.password, self.domain)

        print("\n[+] Querying msDS-MachineAccountQuota...")
        get_machine_account_quota(ldap_connection, self.logger)

        print("\n[+] Querying users with SPNs...")
        get_users_with_spns(ldap_connection, self.logger)