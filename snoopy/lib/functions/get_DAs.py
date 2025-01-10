def get_domain_administrators(ldap_connection, logger, DN):
    logger.open("domain_administrators.txt")
    try:
        resp = ldap_connection.search(searchFilter=f"(&(objectCategory=user)(|(memberOf=cn=Domain Admins,ou=Groups,{DN})(memberOf=cn=Enterprise Admins,ou=Groups,{DN})(memberOf=cn=Administrators,ou=Groups,{DN})))", attributes=['sAMAccountName'])
        count = 0
        for entry in resp:
            if 'attributes' in entry:
                user = entry['attributes'][0]["vals"][0]

                logger.log(f"  - {user}")
                count=count+1

        print(f"[+] Found {count} administrator accounts")

    except Exception as e:
        print(f"[!] Error retrieving Domain Admins: {e}")

    logger.close()