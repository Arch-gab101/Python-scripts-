import ipaddress

def is_ip_in_subnet(ip, subnet):
    """
    Check if a given IP address is within a given subnet.

    Parameters:
    ip (str): The IP address to check.
    subnet (str): The subnet in CIDR notation.

    Returns:
    bool: True if the IP is in the subnet, False otherwise.
    """
    try:
        ip_obj = ipaddress.ip_address(ip)
        subnet_obj = ipaddress.ip_network(subnet, strict=False)
        return ip_obj in subnet_obj
    except ValueError as e:
        print(f"Error: {e}")
    
ip_to_check = "186.53.58.251"
subnet_to_check = "185.58.85.0/24"

if is_ip_in_subnet(ip_to_check, subnet_to_check):
    print(f"{ip_to_check} is in the subnet {subnet_to_check}")
else:
    print(f"{ip_to_check} is NOT in the subnet {subnet_to_check}")




