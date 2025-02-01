def get_domain_trusts(ldap_connection, logger, debug):
    logger.open("trusts.txt")
    try:
        resp = ldap_connection.search(searchFilter="(objectClass=trustedDomain)", attributes=['name','trustType','trustDirection'])
        count=0

        for entry in resp:
            if debug:
                print(f"[DEBUG] {entry}")
                
            if 'attributes' in entry:
                for attribute in entry["attributes"]:
                    property = str(attribute["type"])
                    value = attribute["vals"][0]
                    
                    if property == "trustType":
                        value = parse_trustType(int(value))
                    elif property == "trustDirection":
                        value = parse_trustDirection(int(value))

                    logger.log(f"{property}: {value}")

                count=count+1

        print(f"[+] Found {count} trusts")

    except Exception as e:
        print(f"[!] Error retrieving Domain Trusts: {e}")

    logger.close()

def parse_trustDirection(trustDirection):
    trust_dir = {
        0: 'Disabled',
        1: 'Inbound',
        2: 'Outbound',
        3: 'Bidirectional'
    }

    return trust_dir[trustDirection]

def parse_trustType(trustType):
    trust_type = {
        0: 'ParentChild',
        1: 'CrossLink',
        2: 'Forest',
        3: 'External',
        4: 'Unknown'
    }

    return trust_type[trustType]