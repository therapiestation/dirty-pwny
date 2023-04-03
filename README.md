# dirty-pony
A personal project for scripts and tools
## dnspony.py
Yet another DNS enumaration tool
### Requirements
Execute the following command to install the necessary requirements for the script to run.
```
pip install -r requirements.txt
```
### Usage
The following parameters are currently supported:
```
       ___      __                               
  ____/ (_)____/ /___  ______  ____  ____  __  __
 / __  / / ___/ __/ / / / __ \/ __ \/ __ \/ / / /
/ /_/ / / /  / /_/ /_/ / /_/ / /_/ / / / / /_/ / 
\__,_/_/_/   \__/\__, / .___/\____/_/ /_/\__, /  
                /____/_/                /____/   

usage: DirtyPony [-h] -d DOMAIN -n NAMESERVER -q QUERYTYPE -w WORDLIST

Enumerates DNS records

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Specify the domain for which the subdomains will be enumerated (default: None)
  -n NAMESERVER, --nameserver NAMESERVER
                        Specify the IP of the nameserver which should be used for enumeration (default: None)
  -q QUERYTYPE, --querytype QUERYTYPE
                        Specify the type of query (A/TXT/NS) (default: None)
  -w WORDLIST, --wordlist WORDLIST
                        Specify the the wordlist you want to use (default: None)
```
