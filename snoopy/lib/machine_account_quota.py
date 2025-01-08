def get_machine_account_quota(ldap_connection, logger):
    logger.open("machine_account_quota.txt")
    try:
        resp = ldap_connection.search(searchFilter="(objectClass=*)", attributes=['ms-DS-MachineAccountQuota'])

        if resp[0]["attributes"]:
            quota = resp[0]['attributes'][0]["vals"][0]
            print(f"[+] msDS-MachineAccountQuota: {quota}")
            logger.log(f"msDS-MachineAccountQuota: {quota}")
        else:
            print("[!] msDS-MachineAccountQuota not found.")
    except Exception as e:
        print(f"[!] Error retrieving msDS-MachineAccountQuota: {e}")

    logger.close()