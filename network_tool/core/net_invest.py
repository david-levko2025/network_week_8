from network_tool.core.output_string import format_input_ip,format_subnet_mask,format_classful_status,format_network_address,format_broadcast_address,format_num_hosts,format_cidr_mask

def get_network_address(ip:str,mask:str):
    return get_broadcast_or_network_address(ip,mask,"0","0")

def get_broadcast_address(ip:str,mask:str):
    return get_broadcast_or_network_address(ip,mask,"1","255")

def get_broadcast_or_network_address(ip:str,mask:str,bit_value:str,byte_value:str):
    ip_parts = ip.split(".")
    new_address_parts = []
    bits_left = get_CIDR(mask)
    for part in ip_parts:
        binary = format(int(part),"08b")
        if bits_left >= 8:
            new_address_parts.append(str(part))  
            bits_left -= 8
        elif bits_left > 0:
            network_bin = binary[:bits_left] + f"{bit_value}" * (8 - bits_left)
            new_address_parts.append(str(int(network_bin,2)))
            bits_left = 0
        else:
            new_address_parts.append(f"{byte_value}") 
    return ".".join(new_address_parts)

def get_CIDR(mask:str):
    parts = mask.split(".")
    mask_in_binary = ""
    for part in parts:
        mask_in_binary += format(int(part),"08b")
    counter = 0
    for digit in mask_in_binary:
        if digit == "1":
            counter += 1
    return counter

def calculate_number_of_hosts(mask:str):
    cidr = get_CIDR(mask)
    res = (2 ** (32 - cidr)) -2
    return res

def type_of_class(mask:str):
    cidr = get_CIDR(mask)
    if cidr == 8:
        return "Class A"
    elif cidr == 16:
        return "Class B"
    elif cidr == 24:
        return "Class C"
    else:
        return "Classless"
    
def subnet_info(ip:str,mask:str):
    info = ""
    info += format_input_ip(ip)
    info += format_subnet_mask(mask)
    info += format_classful_status(type_of_class(mask))
    info += format_network_address(get_network_address(ip,mask))
    info += format_broadcast_address(get_broadcast_address(ip,mask))
    info += format_num_hosts(calculate_number_of_hosts(mask))
    info += format_cidr_mask(get_CIDR(mask))
    return info
