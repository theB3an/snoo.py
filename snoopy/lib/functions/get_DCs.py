import socket


def get_domain_controllers(ldap_connection, logger, debug):
    logger.open("domain_controllers.txt")
    try:
        resp = ldap_connection.search(searchFilter="(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=8192))", attributes=['dNSHostName'])
        results = []

        for entry in resp:
            if debug:
                print(f"[DEBUG] {entry}")
                
            if "attributes" in entry:
                hostname = entry['attributes'][0]["vals"][0]
                results.append(str(hostname))
        print(f"[+] Found {len(results)} domain controllers")
        for hostname in results:
            ip = resolve_hostnames_to_ips([hostname])
            logger.log(f"{ip}")

    except Exception as e:
        print(f"[!] Error retrieving domain controllers: {e}")
        return []

    logger.close()

def resolve_hostnames_to_ips(hostnames):
    ip_mapping = {}
    for hostname in hostnames:
        try:
            ip_address = socket.gethostbyname(hostname)
            ip_mapping[hostname] = ip_address
        except socket.gaierror:
            ip_mapping[hostname] = "Resolution failed"
    return ip_mapping

