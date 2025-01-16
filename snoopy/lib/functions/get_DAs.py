def get_domain_administrators(ldap_connection, logger, DN):
    logger.open("domain_administrators.txt")
    try:
        resp = ldap_connection.search(searchFilter=f"(&(objectCategory=group)(|(sAMAccountName=Domain Admins)(sAMAccountName=Enterprise Admins)(sAMAccountName=Administrators)))", attributes=['distinguishedName'])
        count = 0
        paths = []
        for entry in resp:
            if 'attributes' in entry:
                paths.append(str(entry['attributes'][0]["vals"][0]))

        conditions = [f"(memberOf={group_dn})" for group_dn in paths]
        query = f"(&(objectCategory=user)(|{''.join(conditions)}))"
        
        resp2 = ldap_connection.search(searchFilter=query, attributes=['sAMAccountName'])
        for entry2 in resp2:
            if 'attributes' in entry2:
                user = entry2['attributes'][0]["vals"][0]

                logger.log(user)
                count=count+1

        print(f"[+] Found {count} administrator accounts")

    except Exception as e:
        print(f"[!] Error retrieving Domain Admins: {e}")

    logger.close()