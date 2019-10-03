# ipconfiginfo
This scrip helps you with IP addres's information

## Uses

### With console
```bash
$ python3 configip.py <ip-address>/<mask-prefix>
```
### In python code

```python
from IpConfigInfo import IpConfigInfo

ip_with_prefix = '127.0.0.1/8'
ip_config = IpConfigInfo(ip_with_prefix)
#Now you can just print info
ip_config.get_pretty_info()

#Or get dictionary
dict_ip_config = ip_config.get_dict()

#Or get json string that you can send to client and parse it
json_string = ip_config.get_json()

```


