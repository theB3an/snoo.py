def get_machine_account_quota(ldap_connection, logger):
    logger.open("machine_account_quota.txt")
    try:
        search_filter = '(objectClass=*)'
        attributes = ['msDS-MachineAccountQuota']

        resp = ldap_connection.search(search_filter, attributes, searchScope=0)

        if resp and 'msDS-MachineAccountQuota' in resp[0]['attributes']:
            quota = resp[0]['attributes']['msDS-MachineAccountQuota'][0]
            print(f"[+] msDS-MachineAccountQuota: {quota}")
            logger.log(f"msDS-MachineAccountQuota: {quota}")
        else:
            print("[!] msDS-MachineAccountQuota not found.")
    except Exception as e:
        print(f"[!] Error retrieving msDS-MachineAccountQuota: {e}")

    logger.close()