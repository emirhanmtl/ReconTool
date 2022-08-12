import os

banner = '''


                                Welcome to my ReconTool
                                
                                
                                Twitter: emirhanmtl
                                GitHub:  emirhanmtl




'''

print(banner)

input_domain = input("Please enter the domain (Example = tesla.com): ")

command =  "curl -s https://crt.sh/\?q\=%25.{domain}\&output\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | httpx -status-code -o subs.txt"


os.system(command.format(domain = input_domain))
