#!/usr/bin/env python3
import os
import progressbar
import dns.resolver

from time import sleep


def dns_query_specific_nameserver(query="inlanefreight.htb", nameserver="10.129.42.195", qtype="A"):
    """
    Query a specific nameserver for:
    - An IPv4 address for a given hostname (qtype="A")
    - An IPv6 address for a given hostname (qtype="AAAA")
    
    Returns the IP address as a string
    """
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [nameserver]
    answer = resolver.resolve(query, qtype)
    if len(answer) == 0:
        return None
    else:
        return str(answer[0])

print("""	
       ___      __                               
  ____/ (_)____/ /___  ______  ____  ____  __  __
 / __  / / ___/ __/ / / / __ \/ __ \/ __ \/ / / /
/ /_/ / / /  / /_/ /_/ / /_/ / /_/ / / / / /_/ / 
\__,_/_/_/   \__/\__, / .___/\____/_/ /_/\__, /  
                /____/_/                /____/   

""")

# load subdomains from wordlist in lines
with open('/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt') as wordlist:
	lines = wordlist.read().splitlines()

# go for it
testdomain = ".inlanefreight.htb"
querytype = "A"

print("[-]"+"\t"+"Starting brute force subdomain enumeration with "+testdomain)

for i in progressbar.progressbar(range(len(lines)), redirect_stdout=True):

	testquery = lines[i]+testdomain
	
	try:
		retval = dns_query_specific_nameserver(query=testquery,qtype=querytype)
		print("[+]"+"\t"+testquery+" "+querytype+" "+retval)
	except Exception as e:
		if "The DNS query name does not exist:" not in str(e):
			print("[!]"+"\t"+str(e))
		pass
	else:
		pass
	finally:
		pass

print("[-]"+"\t"+"Finished brute force subdomain enumeration with "+testdomain)	