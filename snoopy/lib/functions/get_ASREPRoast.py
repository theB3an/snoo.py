def get_asrep_roast(ldap_connection, logger, debug):
    logger.open("ASRepRoastable.txt")
    try:
        resp = ldap_connection.search(searchFilter="(userAccountControl:1.2.840.113556.1.4.803:=4194304)", attributes=['sAMAccountName'])
        count = 0

        for entry in resp:
            if debug:
                print(f"[DEBUG] {entry}")
                
            if 'attributes' in entry:
                user = entry['attributes'][0]["vals"][0]

                logger.log(f"  - {user}")
                count=count+1

        print(f"[+] Found {count} ASRepRoastable Users")
    except Exception as e:
        print(f"[!] Error retrieving ASREPRoastable Users: {e}")

    logger.close()