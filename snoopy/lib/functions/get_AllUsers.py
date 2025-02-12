from impacket.ldap import ldap

def get_all_users(ldap_connection, logger, debug):
    logger.open("AllUsers.txt")
    try:
        pager = ldap.SimplePagedResultsControl(size=100)
        resp = ldap_connection.search(searchFilter="(&(objectCategory=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))", attributes=['sAMAccountName'], searchControls=[pager])
        count = 0

        for entry in resp:
            if debug:
                print(f"[DEBUG] {entry}")
                
            if 'attributes' in entry and entry['attributes'][0]:
                user = entry['attributes'][0]["vals"][0]

                logger.log(f"{user}")
                count=count+1

        print(f"[+] Found {count} enabled users")
    except Exception as e:
        print(f"[!] Error retrieving All Enabled Users: {e}")

    logger.close()