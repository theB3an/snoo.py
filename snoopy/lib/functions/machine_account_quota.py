def get_machine_account_quota(ldap_connection, logger):
    logger.open("machine_account_quota.txt")
    try:
        resp = ldap_connection.search(searchFilter="(objectClass=domain)", attributes=['ms-DS-MachineAccountQuota'])

        quota = resp[0]['attributes'][0]["vals"][0]
        print(f"[+] ms-DS-MachineAccountQuota: {quota}")
        logger.log(f"msDS-MachineAccountQuota: {quota}")

    except Exception as e:
        print(f"[!] Error retrieving ms-DS-MachineAccountQuota: {e}")

    logger.close()