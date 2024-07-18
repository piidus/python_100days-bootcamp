import ipaddress

def check_ip(address):
  try:
    ip = ipaddress.ip_address(address)
    if isinstance(ip, ipaddress.IPv4Address):
      return "IPv4"
    elif isinstance(ip, ipaddress.IPv6Address):
      return "IPv6"
  except ValueError:
    return "Invalid"

# Example usage
ip_address = "8.8.8.8"
result = check_ip(ip_address)
print(result)  # Output: IPv4
print(check_ip("1111.2222.3333.4444"))  # Output: Invalid
print(check_ip("866c:cf9d:2994:cd3b:55da:97e3:a5b4:a39b"))  # Output: IPv6
