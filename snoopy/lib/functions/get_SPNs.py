def get_users_with_spns(ldap_connection, logger, debug):
    logger.open("SPNs.txt")
    try:
        resp = ldap_connection.search(searchFilter="(&(objectCategory=person)(servicePrincipalName=*))", attributes=['sAMAccountName', 'servicePrincipalName', 'memberOf'])
        count = 0

        for entry in resp:
            if debug:
                print(f"[DEBUG] {entry}")
            groups=[]
            if "attributes" in entry:
                for attribute in entry['attributes']:
                    if "sAMAccountName" in str(attribute['type']):
                        user = attribute["vals"][0]
                    elif "memberOf" in str(attribute['type']):
                        groups = attribute["vals"]
                    elif "servicePrincipalName" in str(attribute['type']):
                        spns = attribute["vals"]
                    
                if any(s in str(groups) for s in ["Domain Admins", "Enterprise Admins", "Administrators"]):
                    logger.log(f"  - {user} - ADMIN!")
                else:
                    logger.log(f"  - {user}")
                    
                for spn in spns:
                    logger.log(f"      SPN: {spn}")
                count=count+1
            
        print(f"[+] Found {count} kerberoastable accounts")

    except Exception as e:
        print(f"[!] Error retrieving users with SPNs: {e}")

    logger.close()