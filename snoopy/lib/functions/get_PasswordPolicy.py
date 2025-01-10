def get_password_policy(ldap_connection, logger):
    logger.open("passwordpolicy.txt")
    try:
        resp = ldap_connection.search(searchFilter="(objectClass=domainDNS)", attributes=['minPwdLength','pwdProperties', 'lockoutThreshold', 'lockoutDuration', 'pwdHistoryLength'])

        for entry in resp:
            if "attributes" in entry:
                for attribute in entry["attributes"]:
                    property = str(attribute["type"])
                    value = int(attribute["vals"][0])

                    if property == "pwdProperties":
                        property = property.replace("pwdProperties", "pwdComplexity")
                        value = str(parse_pwdProperties(value))
                    elif property == "lockoutDuration":
                        value = str(calculate_lockoutDuration(value))

                    value = str(value)
                    logger.log(f"{property}: {value}")

        print("[+] Successfully retrieved password policy")                    
    except Exception as e:
        print(f"[!] Error retrieving Password Policy: {e}")

    logger.close()

def calculate_lockoutDuration(duration):
    lockout = int((abs(duration) * 100) // 6e+10)
    return lockout

def parse_pwdProperties(pwdProperties):
    parser = []
    while pwdProperties:
        parser.append(pwdProperties % 2)
        pwdProperties //= 2
    
    parser = parser[::-1]
    if len(parser) != 8:
        for x in range(6-len(parser)):
            parser.insert(0, 0)
    values = "".join([str(v) for v in parser])
    if int(values[5]) == 1:
        return True
    else:
        return False
