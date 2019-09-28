from IpConfigInfo import IpConfigInfo
from sys import argv

ip = IpConfigInfo(argv[1])

ip.get_pretty_info()

