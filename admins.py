import re
file = open('access.log', 'r')
list_ip = {}
for line in file.readlines():
	ips = list(re.findall(r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}', str))
	for ip in ips:
		mask = '.'.join(ip.split('.')[:-1])
		if mask not in list_ip.keys():
			list_ip[mask] = {}
		 list_ip[mask][ip] = 0

for mask, ips in list_ip.items():
	for ip in ips:
		print(ip)
