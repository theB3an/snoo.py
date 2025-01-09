def get_asrep_roast(ldap_connection, logger):
    logger.open("ASREPRoastable.txt")
    try:
        resp = ldap_connection.search(searchFilter="(userAccountControl:1.2.840.113556.1.4.803:=4194304)", attributes=['sAMAccountName'])

        for entry in resp:
            if 'attributes' in entry:
                user = entry['attributes'][0]["vals"][0]

                logger.log(f"  - {user}")

    except Exception as e:
        print(f"[!] Error retrieving ASREPRoastable Users: {e}")

    logger.close()