from network_tool.core.util import IPAddress, Mask, Subnet


def main():
    ip = IPAddress.ip_output()
    mask = Mask.mask_output()

    subnet = Subnet(ip, mask)

    print(subnet.build_output())
    subnet.write_to_file1("output_string.py")
    subnet.write_to_file2("output_string.py")
    subnet.write_to_file3("output_string.py")

if __name__ == "__main__":
    main()
