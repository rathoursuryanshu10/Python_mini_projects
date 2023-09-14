import whois
domain_name=input("Enter the domain name:: ")
domain_info=whois.whois(domain_name)
for key ,value in domain_info.items():
    print(key," :: ",value)
