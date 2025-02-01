def get_machine_account_quota(ldap_connection, logger, debug):
    logger.open("machine_account_quota.txt")
    try:
        resp = ldap_connection.search(searchFilter="(objectClass=domain)", attributes=['ms-DS-MachineAccountQuota'])

        if debug:
            print(f"[DEBUG] {resp[0]}")

        quota = str(resp[0]['attributes'][0]["vals"][0])
        print(f"[+] Found Machine Account Quota")
        logger.log(f"msDS-MachineAccountQuota: {quota}")

    except Exception as e:
        print(f"[!] Error retrieving ms-DS-MachineAccountQuota: {e}")

    logger.close()