def get_password_policy(ldap_connection, logger):
    logger.open("passwordpolicy.txt")
    try:
        resp = ldap_connection.search(searchFilter="(objectClass=domainDNS)", attributes=['minPwdLength','pwdProperties', 'lockoutThreshold', 'lockoutDuration', 'pwdHistoryLength'])

        for entry in resp:
            if "attributes" in entry:
                for attribute in entry["attributes"]:
                    property = str(attribute["type"])
                    value = str(attribute["vals"][0])

                    if property == "pwdProperties":
                        property = property.replace("pwdProperties", "pwdComplexity")
                    elif property == "lockoutDuration":
                        value = calculate_lockoutDuration(value)

                    logger.log(f"{property}: {value}")
    except Exception as e:
        print(f"[!] Error retrieving Password Policy: {e}")

    logger.close()

def calculate_lockoutDuration(duration):
    lockout = abs(duration) // 10_000_000
    return lockout
