#!/usr/bin/env python3

import os
import progressbar
import dns.resolver
import argparse

from time import sleep

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
		___      __                               
	____/ (_)____/ /___  ______  ____  ____  __  __
	/ __  / / ___/ __/ / / / __ \/ __ \/ __ \/ / / /
	/ /_/ / / /  / /_/ /_/ / /_/ / /_/ / / / / /_/ / 
	\__,_/_/_/   \__/\__, / .___/\____/_/ /_/\__, /  
					/____/_/                /____/   


	0.1 - 2023-04-02 - Initial release

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

# go for it
testdomain = "."+args.domain
querytype = args.querytype

# if args.querytype:
#	querytype = args.querytype
# else:
#	querytype = ["A", "TXT", "NS"]

nameserver = args.nameserver

print("[-]"+"\t"+"Starting brute force subdomain enumeration with "+testdomain)

for i in progressbar.progressbar(range(len(lines)), redirect_stdout=True):

	testquery = lines[i]+testdomain

	try:
		retval = dns_query_specific_nameserver(query=testquery,qtype=str(querytype),nameserver=nameserver)
		print("[+]"+"\t"+testquery+" "+querytype+" "+retval)
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
		pass

print("[-]"+"\t"+"Finished brute force subdomain enumeration with "+testdomain)	