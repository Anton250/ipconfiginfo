import math, json



class IpConfigInfo():

        binary_address = ''
        binary_mask = ''
        binary_network = ''
        binary_host = ''
        binary_broadcast = ''
        binary_max_ip = ''
        binary_min_ip = ''
        addres = ''
        num_mask = ''
        mask = ''
        network = ''
        host = ''
        broadcast = ''
        max_ip = ''
        min_ip = ''
        count_of_ip = 0
        count_of_hosts = 0
        form = ' '
        def __init__(self, ip, form = ' '):
                addres = ip.split('/')
                self.form = form
                self.mask = addres[-1]

                if (int(self.mask) > 31 or int(self.mask) < 1):
                        exit('Error mask')

                range_of_mask = 32 - int(self.mask)
                self.count_of_ip = int(math.pow(2, range_of_mask))
                self.count_of_hosts = self.count_of_ip - 2


                addres.pop(-1)

                oct1, oct2, oct3, oct4 = addres[0].split('.')
                self.binary_address = f'{int(oct1):08b}{form}{int(oct2):08b}{form}{int(oct3):08b}{form}{int(oct4):08b}'
                self.addres = f'{oct1:8}{form}{oct2:8}{form}{oct3:8}{form}{oct4:8}'
                self.num_mask = '/' + self.mask

                nulls = int(self.mask) // 8

                nulls_o = int(self.mask) - nulls * 8 

                ones = ('1' * 8 if nulls != 0 else '1' * nulls_o)

                self.binary_mask = f'{ones:0<8}'

                for i in range(0, 3):
                        nulls -= 1
                        ones = '1' * 8 if nulls >0 else '1' * nulls_o
                        self.binary_mask = self.binary_mask + f'{form}{ones:0<8}'
                        if nulls == 0:
                                nulls_o = 0

                self.mask = self.get_ip_from_binary(self.binary_mask.split(form))

                self.binary_network = self.multiply_binary(self.binary_address.split(form), self.binary_mask.split(form))
                self.network = self.get_ip_from_binary(self.binary_network.split(form))


                binary_host_mask = self.reflection(self.binary_mask)

                self.binary_host = self.multiply_binary(self.binary_address.split(form), binary_host_mask.split(form))

                self.binary_broadcast = self.get_broadcast(
                        self.binary_network.split(form), self.multiply_binary(
                                self.reflection(
                                        self.binary_network
                                        ).split(form), binary_host_mask.split(form)
                                        ).split(form)
                        )
                self.host = self.get_ip_from_binary(self.binary_host.split(form))
                self.broadcast = self.get_ip_from_binary(self.binary_broadcast.split(form))
                max_ip = list(self.binary_network)
                max_ip[-1] = '1'
                self.binary_max_ip = ''.join(max_ip)
                min_ip = list(self.binary_broadcast)
                min_ip[-1] = '0'
                self.binary_min_ip = ''.join(min_ip)
                self.max_ip = self.get_ip_from_binary(self.binary_max_ip.split(form))
                self.min_ip = self.get_ip_from_binary(self.binary_min_ip.split(form))




        def multiply_binary(self, a, b):
                c = ''
        
                for i in range(0,len(a)):
                        if (isinstance(a, list)):
                                c += str(self.multiply_binary(a[i], b[i])) + (self.form if i != len(a) - 1 else '')
                        else:
                                c += str(int(a[i]) * int(b[i]))
                                
                return c

        def reflection(self, a):
                a = a.replace('1', '2')
                a = a.replace('0', '3')
                a = a.replace('2', '0')
                a = a.replace('3', '1')
                return a

        def get_ip_from_binary(self, binary):
                oct1, oct2, oct3, oct4 = binary
                return f'{int(oct1, 2):<8}{self.form}{int(oct2, 2):<8}{self.form}{int(oct3, 2):<8}{self.form}{int(oct4, 2):<8}'

        def get_broadcast(self, a, b):
                c = ''
        
                for i in range(0,len(a)):
                        if (isinstance(a, list)):
                                c += str(self.get_broadcast(a[i], b[i])) + (self.form if i != len(a) - 1 else '')
                        else:
                                inta, intb = int(a[i]), int(b[i])
                                c += str(inta + intb if ((inta == intb and inta != 1) or inta != intb) else 1)
                                
                return c
        def get_pretty_info(self):
                print(f'IP address:\n{self.addres}\n{self.binary_address}\n')
                print(f'Mask:\n{self.num_mask}\n{self.mask}\n{self.binary_mask}\n')
                print(f'Network:\n{self.network}\n{self.binary_network}\n')
                print(f'Host:\n{self.host}\n{self.binary_host}\n')
                print(f'Broadcast:\n{self.broadcast}\n{self.binary_broadcast}\n')
                print(f'Count of IP: {self.count_of_ip}\nMax hosts: {self.count_of_hosts}\n')
                print(f'Max IP:\n{self.max_ip}\n{self.binary_max_ip}\n')
                print(f'Min IP:\n{self.min_ip}\n{self.binary_min_ip}\n')

        def get_dict(self):
                return {
                        'binary_address' : self.binary_address,
                        'binary_mask': self.binary_mask,
                        'binary_network': self.binary_network,
                        'binary_host': self.binary_host,
                        'binary_broadcast': self.binary_broadcast,
                        'binary_max_ip': self.binary_max_ip,
                        'binary_min_ip': self.binary_min_ip,
                        'addres': self.addres,
                        'num_mask': self.num_mask,
                        'mask': self.mask,
                        'network': self.network,
                        'host': self.host,
                        'broadcast': self.broadcast,
                        'max_ip': self.max_ip,
                        'min_ip': self.min_ip,
                        'count_of_ip': self.count_of_ip,
                        'count_of_hosts': self.count_of_hosts
                }

        def get_json(self):
                return json.dumps(self.get_dict())



