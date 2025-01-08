def get_users_with_spns(ldap_connection, logger):
    logger.open("SPNs.txt")
    try:
        resp = ldap_connection.search(searchFilter="(&(objectCategory=person)(servicePrincipalName=*))", attributes=['sAMAccountName', 'servicePrincipalName'])
        count = 0

        if resp:
            for entry in resp:
                if "attributes" in resp:
                    user = entry['attributes'][0]["vals"][0]
                    spns = entry['attributes'][1]["vals"]
                    logger.log(f"  - {user}")
                    for spn in spns:
                        logger.log(f"      SPN: {spn}")
                    count=count+1
            
            print(f"[+] Users with SPNs configured: {count}")
        
        else:
            print("[!] No users with SPNs found.")
    except Exception as e:
        print(f"[!] Error retrieving users with SPNs: {e}")

    logger.close()