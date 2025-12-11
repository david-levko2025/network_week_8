# utils.py

class IPAddress:
    def __init__(self, ip: str):
        self.ip = ip
        self.octets = list(map(int, ip.split(".")))

    def to_binary(self):
        return "".join(format(o, "08b") for o in self.octets)
    
    def ip_output():
        ip = input("Enter IP: ")
    
#Representation of the mask in CIDR
    def get_class(self):
        first = self.octets[0]
        if 0 <= first <= 127:
            return "A"
        if 128 <= first <= 191:
            return "B"
        if 192 <= first <= 223:
            return "C"
        return "D/E"

    def __str__(self):
        return self.ip



class Mask:
    def __init__(self, mask: str):
        self.mask = mask
        self.octets = list(map(int, mask.split(".")))
        self.binary = self.to_binary()
        self.prefix_ = self.prefix()

    def to_binary(self):
        return ".".join(format(o, "08b") for o in self.octets)

    def prefix(self):
        return self.binary.replace(".", "").count("1")

    def __str__(self):
        return self.mask


    def mask_output():
        cidr_str = input("Enter Mask length (CIDR): ")



class Subnet:
    def __init__(self, ip: IPAddress, mask: Mask):
        self.ip = ip
        self.mask = mask
        self.prefix = mask.prefix_

        self.network = self.calculate_network()
        self.broadcast = self.calculate_broadcast()


#calculate all

    def calculate_network(self):
        ip_bin = self.ip.to_binary()
        net_bin = ip_bin[:self.prefix] + "0" * (32 - self.prefix)
        return ".".join(str(int(net_bin[i:i+8], 2)) for i in range(0, 32, 8))

    def calculate_broadcast(self):
        ip_bin = self.ip.to_binary()
        bc_bin = ip_bin[:self.prefix] + "1" * (32 - self.prefix)
        return ".".join(str(int(bc_bin[i:i+8], 2)) for i in range(0, 32, 8))
  
    def usable_hosts_count(self):
        if self.mask >= 31:
            return 0
        return (2 ** (32 - self.mask)) - 2


    # def cidr_to_mask_int(self, mask):
        #     return (0xFFFFFFFF << (32 - mask)) & 0xFFFFFFFF

    def build_output(self):
        return f"""
IP Address:      {self.ip}
Mask:            {self.mask} (/ {self.prefix})
Class:           {self.ip.get_class()}
Binary Mask:     {self.mask.binary}
Network Adress:         {self.network}
Broadcast Adress:       {self.broadcast}
Usable Hosts:  {self.usable_hosts_count()}
"""

    

    def write_to_file1(self, filename="subnet_info_192.168.10.130_214309734.txt"):
        text = self.build_output()
        with open(filename, "w") as f:
            f.write(text)
        print(f"Results saved to {filename}")

    def write_to_file2(self, filename="subnet_info_172.16.45.200_214309734.txt"):
        text = self.build_output()
        with open(filename, "w") as f:
            f.write(text)
        print(f"Results saved to {filename}")

    def write_to_file3(self, filename="subnet_info_10.50.200.7_214309734.txt"):
        text = self.build_output()
        with open(filename, "w") as f:
            f.write(text)
        print(f"Results saved to {filename}")


