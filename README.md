# ipconfiginfo
This scrip helps you with IP addres's information

## Uses

### With console
```bash
$ python3 configip.py 127.0.0.1/8
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

## Some helpful information

When you are creating IpConfigInfo object, you also can specify the form of output, i.e. separator in output between the octets.
Default is space.

For example:

With space ip will look like this: 127 0 0 1
With dot it will lool like this: 127.0.0.1

