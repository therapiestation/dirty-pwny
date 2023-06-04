# dirty-pwny
A personal project for scripts and tools
## dnspwny.py
Yet another DNS enumaration tool (with progress bar, yay!)
### Requirements
Execute the following command to install the necessary requirements for the script to run.
```
pip install -r requirements.txt
```
### Usage
The following parameters are currently supported:
```

        ____  _   _______                          
       / __ \/ | / / ___/____ _      ______  __  __
      / / / /  |/ /\__ \/ __ \ | /| / / __ \/ / / /
     / /_/ / /|  /___/ / /_/ / |/ |/ / / / / /_/ / 
    /_____/_/ |_//____/ .___/|__/|__/_/ /_/\__, /  
                     /_/                  /____/   
	
usage: DirtyPony [-h] -d DOMAIN -n NAMESERVER [-q QUERYTYPE] -w WORDLIST

Enumerates DNS records

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Specify the domain for which the subdomains will be enumerated (default: None)
  -n NAMESERVER, --nameserver NAMESERVER
                        Specify the IP of the nameserver which should be used for enumeration (default: None)
  -q QUERYTYPE, --querytype QUERYTYPE
                        Specify the type of query (A/TXT/NS), queries for A/TXT/NS if not specified (default: None)
  -w WORDLIST, --wordlist WORDLIST
                        Specify the the wordlist you want to use (default: None)

```
