def get_all_users(ldap_connection, logger):
    logger.open("AllUsers.txt")
    try:
        resp = ldap_connection.search(searchFilter="(&(objectCategory=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))", attributes=['sAMAccountName'])
        count = 0

        for entry in resp:
            if 'attributes' in entry:
                user = entry['attributes'][0]["vals"][0]

                logger.log(f"{user}")
                count=count+1

        print(f"[+] Found {count} enabled users")
    except Exception as e:
        print(f"[!] Error retrieving All Enabled Users: {e}")

    logger.close()