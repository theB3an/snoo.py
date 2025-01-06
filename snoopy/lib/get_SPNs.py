def get_users_with_spns(ldap_connection, logger):
    logger.open("SPNs.txt")
    try:
        search_filter = '(&(objectClass=user)(servicePrincipalName=*))'
        attributes = ['cn', 'servicePrincipalName']

        resp = ldap_connection.search(search_filter, attributes, searchScope=2)

        if resp:
            print("[+] Users with SPNs configured:")
            for entry in resp:
                user = entry['attributes'].get('cn', ['Unknown'])[0]
                spns = entry['attributes'].get('servicePrincipalName', [])
                print(f"  - {user}")
                for spn in spns:
                    print(f"      SPN: {spn}")
        else:
            print("[!] No users with SPNs found.")
    except Exception as e:
        print(f"[!] Error retrieving users with SPNs: {e}")

    logger.close()