#!/usr/bin/env python3

import os
import progressbar
import dns.resolver
import argparse

from alive_progress import alive_bar

#
# functions
#


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

def banner():

	print("""	


        ____  _   _______                          
       / __ \/ | / / ___/____ _      ______  __  __
      / / / /  |/ /\__ \/ __ \ | /| / / __ \/ / / /
     / /_/ / /|  /___/ / /_/ / |/ |/ / / / / /_/ / 
    /_____/_/ |_//____/ .___/|__/|__/_/ /_/\__, /  
                     /_/                  /____/   

	0.1 - 2023-04-02 - Initial release
    0.2 - 2023-06-03 - Rebranding...

    Features: DNS subdomain enumeration ( with a progress bar, yay!)

	TODOs:

	- Refine error handling
	- Output file / logging

	""")


#
# arguments
#

parser = argparse.ArgumentParser(
						prog="DirtyPony",
						description="Enumerates DNS records",
						epilog="by Techslave",
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--domain", required=True, help="Specify the domain for which the subdomains will be enumerated")
parser.add_argument("-n", "--nameserver", required=True, help="Specify the IP of the nameserver which should be used for enumeration")
parser.add_argument("-q", "--querytype", required=False, help="Specify the type of query (A/TXT/NS), queries for A/TXT/NS if not specified")
parser.add_argument("-w", "--wordlist", required=True, type=argparse.FileType('r'), help="Specify the the wordlist you want to use")


#
# script
#         

banner()

# check / load arguments
args = parser.parse_args()

# load subdomains from wordlist in lines
with open(args.wordlist.name) as wordlist:
	lines = wordlist.read().splitlines()
len_items = len(lines)

# go for it
testdomain = "."+args.domain
querytype = args.querytype

# if args.querytype:
#	querytype = args.querytype
# else:
#	querytype = ["A", "TXT", "NS"]

nameserver = args.nameserver


print("[-]"+"\t"+"Starting brute force subdomain enumeration with "+testdomain)

with alive_bar(len_items, title='Processing', bar='filling', spinner='waves2', enrich_print=False) as bar:
	for i in range(len(lines)):
			testquery = lines[i]+testdomain
			try:
				# set current query
				bar.text(testquery)
				# exec query
				retval = dns_query_specific_nameserver(query=testquery,qtype=str(querytype),nameserver=nameserver)
				print("[+]"+"\t"+"Line: " +str(bar.current)+"\t"+testquery+" "+querytype+" "+retval)
			except Exception as e:
				if "The DNS query name does not exist:" not in str(e):
					print("[!]"+"\t"+str(e))
				pass
			except KeyboardInterrupt:
				print("[!]"+"\tCtrl-C detected, aborting script")
				break
			else:
				pass
			finally:
				bar()
				pass

print("[-]"+"\t"+"Finished brute force subdomain enumeration with "+testdomain)	

