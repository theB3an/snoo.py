from snoopy.lib.snoo import snoo
from snoopy.lib.logger import Logger
from snoopy import __version__
import argparse

def main():
    banner()
    args = parse_arguments()
    logger=Logger(args.output, args.verbose)
    Snoopy = snoo(args.domain_controller, args.username, args.password, logger, args.domain, args.All_Users, args.debug)
    Snoopy.run()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Query LDAP for msDS-MachineAccountQuota and users with SPNs configured.")
    parser.add_argument("-dc", "--domain-controller", required=True, help="Domain controller address (e.g. DC1, DC1.contoso.local)")
    parser.add_argument("-u", "--username", required=True, help="Username for LDAP authentication (e.g. jhammond, jhammond@contoso.local)")
    parser.add_argument("-p", "--password", required=True, help="Password for the specified user")
    parser.add_argument("-d", "--domain", required=False, help="Domain name (e.g. contoso.local)")
    parser.add_argument("-o", "--output", required=False, help="Output directory (default: ~/snoopy)")
    parser.add_argument("-A", "--All-Users", required=False, action='store_true', help="Retrieve list of all enabled users from Active Directory")
    parser.add_argument("-v", "--verbose", required=False, action='store_true', help="Enable verbose output")
    parser.add_argument("--debug", required=False, action='store_true', help="Enable debug output")
    return parser.parse_args()

def banner():
    banner = f'''
________  ________   ________  ________  ________  ___    ___ 
|\   ____\|\   ___  \|\   __  \|\   __  \|\   __  \|\  \  /  /|
\ \  \___|\ \  \\ \  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \/  / /
 \ \_____  \ \  \\ \  \ \  \\\  \ \  \\\  \ \   ____\ \    / / 
  \|____|\  \ \  \\ \  \ \  \\\  \ \  \\\  \ \  \___|\/  /  /  
    ____\_\  \ \__\\ \__\ \_______\ \_______\ \__\ __/  / /    
   |\_________\|__| \|__|\|_______|\|_______|\|__||\___/ /     
   \|_________|                                   \|___|/  v{__version__}    
                                                               
                                                @theB3an              
'''
    print(banner)

if __name__ == '__main__':
    main()