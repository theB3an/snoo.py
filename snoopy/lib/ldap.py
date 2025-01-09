from impacket.ldap import ldap
import sys

def get_ldap_connection(domain_controller, username, password, domain, distinguishedName):
    try:
        ldap_connection = ldap.LDAPConnection(f'ldap://{domain_controller}', baseDN=distinguishedName)
        ldap_connection.login(username, password, domain)
        return ldap_connection
    except Exception as e:
        print(f"[!] Failed to connect to LDAP server: {e}")
        sys.exit(1)