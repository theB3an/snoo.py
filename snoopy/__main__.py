from snoopy.lib.snoo import snoo
from snoopy.lib.logger import Logger
import argparse

def main():
    banner()
    args = parse_arguments()
    logger=Logger(args.output)
    Snoopy = snoo(args.domain_controller, args.username, args.password, args.domain, logger)
    Snoopy.run()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Query LDAP for msDS-MachineAccountQuota and users with SPNs configured.")
    parser.add_argument("-dc", "--domain-controller", required=True, help="Domain controller address (e.g., dc.example.com)")
    parser.add_argument("-u", "--username", required=True, help="Username for LDAP authentication (e.g., user@domain.com)")
    parser.add_argument("-p", "--password", required=True, help="Password for the specified user")
    parser.add_argument("-d", "--domain", required=True, help="Domain name (e.g., example.com)")
    parser.add_argument("-o", "--output", required=False, help="Output directory (default: ~/snoopy)")
    return parser.parse_args()

def banner():
    banner = '''
________  ________   ________  ________  ________  ___    ___ 
|\   ____\|\   ___  \|\   __  \|\   __  \|\   __  \|\  \  /  /|
\ \  \___|\ \  \\ \  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \/  / /
 \ \_____  \ \  \\ \  \ \  \\\  \ \  \\\  \ \   ____\ \    / / 
  \|____|\  \ \  \\ \  \ \  \\\  \ \  \\\  \ \  \___|\/  /  /  
    ____\_\  \ \__\\ \__\ \_______\ \_______\ \__\ __/  / /    
   |\_________\|__| \|__|\|_______|\|_______|\|__||\___/ /     
   \|_________|                                   \|___|/      
                                                               
                                                               
                                                @theB3an              
'''
    print(banner)

if __name__ == '__main__':
    main()