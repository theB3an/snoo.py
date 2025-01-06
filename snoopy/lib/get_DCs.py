import socket


def get_domain_controllers(ldap_connection, logger):
    logger.open("domain_controllers.txt")
    try:
        search_filter = '(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=8192))'
        attributes = ['dNSHostName', 'operatingSystem']

        resp = ldap_connection.search(search_filter, attributes, searchScope=2)
        results = []

        if resp:
            for entry in resp:
                hostname = entry['attributes'].get('dNSHostName', ['Unknown'])[0]
                results.append(hostname)
            print(f"[+] Found {len(results)} domain controllers")
            for hostname in results:
                ip = resolve_hostnames_to_ips([hostname])
                logger.log(f"{hostname} - {ip}")
        else:
            print("[!] No domain controllers found.")
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

