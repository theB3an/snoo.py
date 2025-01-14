from snoopy.lib.ldap import get_ldap_connection
from snoopy.lib.functions import *
    
class snoo:
    def __init__(self, domain_controller, username, password, logger, domain=None, allUsers=False):
        self.domain_controller = domain_controller
        self.password = password
        self.logger = logger
        self.allUsers = allUsers

        login = username.split('@')
        self.username = login[0]

        if domain == None:
            self.domain = login[1]
        else:
            self.domain = domain
        
        self.distinguishedName = ''
        domainParts = self.domain.split('.')
        for i in domainParts:
            self.distinguishedName += 'dc=%s,' % i
        self.distinguishedName = self.distinguishedName[:-1]

        

    def run(self):
        print("\n[+] Starting LDAP Connection to Domain Controller...")
        ldap_connection = get_ldap_connection(self.domain_controller, self.username, self.password, self.distinguishedName, self.domain)

        print("\n[+] Querying msDS-MachineAccountQuota...")
        machine_account_quota.get_machine_account_quota(ldap_connection, self.logger)

        print("\n[+] Querying users with SPNs...")
        get_SPNs.get_users_with_spns(ldap_connection, self.logger)

        print("\n[+] Querying for DCs...")
        get_DCs.get_domain_controllers(ldap_connection, self.logger)

        print("\n[+] Querying for Domain Admins...")
        get_DAs.get_domain_administrators(ldap_connection, self.logger, self.distinguishedName)

        print("\n[+] Querying ASRepRoastable Users...")
        get_ASREPRoast.get_asrep_roast(ldap_connection, self.logger)

        print("\n[+] Querying Password Policy...")
        get_PasswordPolicy.get_password_policy(ldap_connection, self.logger)

        print("\n[+] Querying Domain Trusts...")
        get_Trusts.get_domain_trusts(ldap_connection, self.logger)

        if self.allUsers:
            print("\n[+] Retrieve all enabled users...")
            get_AllUsers.get_all_users(ldap_connection, self.logger)