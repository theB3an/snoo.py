from snoopy.lib.ldap import get_ldap_connection
from snoopy.lib.get_SPNs import get_users_with_spns
from snoopy.lib.machine_account_quota import get_machine_account_quota
from snoopy.lib.get_DCs import get_domain_controllers
from snoopy.lib.get_DAs import get_domain_administrators
from snoopy.lib.get_ASREPRoast import get_asrep_roast
from snoopy.lib.get_PasswordPolicy import get_password_policy
    
class snoo:
    def __init__(self, domain_controller, username, password, domain, logger):
        self.domain_controller = domain_controller
        self.username = username
        self.password = password
        self.domain = domain
        self.logger = logger
        
        self.distinguishedName = ''
        domainParts = domain.split('.')
        for i in domainParts:
            self.distinguishedName += 'dc=%s,' % i
        self.distinguishedName = self.distinguishedName[:-1]

        

    def run(self):
        print("\n[+] Starting LDAP Connection to Domain Controller...")
        ldap_connection = get_ldap_connection(self.domain_controller, self.username, self.password, self.domain, self.distinguishedName)

        print("\n[+] Querying msDS-MachineAccountQuota...")
        get_machine_account_quota(ldap_connection, self.logger)

        print("\n[+] Querying users with SPNs...")
        get_users_with_spns(ldap_connection, self.logger)

        print("\n[+] Querying for DCs...")
        get_domain_controllers(ldap_connection, self.logger)

        print("\n[+] Querying for Domain Admins...")
        get_domain_administrators(ldap_connection, self.logger, self.distinguishedName)

        print("\n[+] Querying ASREPRoastable Users...")
        get_asrep_roast(ldap_connection, self.logger)

        print("\n[+] Querying Password Policy...")
        get_password_policy(ldap_connection, self.logger)