import ifaddr
import ipaddress


def get_adapter_info():
    
    adapters = []

    adapter_data = ifaddr.get_adapters()
    
    for adapter in adapter_data:
        
        interface = ''
        ipv4 = ''
        subnet = ''
        broadcast = ''

        interface =  adapter.nice_name
        for ip in adapter.ips:
            if ip.is_IPv4:
                ipv4 = ip.ip
                subnet = ip.network_prefix
                broadcast = get_broadcast_address(ipv4, subnet)
        adapter_dict = {"interface": interface, "ipv4": ipv4, "subnet": subnet, "broadcast": broadcast}
        adapters.append(adapter_dict)

    return adapters

def get_broadcast_address(IP, MASK):

    addr = IP + '/' +  str(MASK)
    net = ipaddress.IPv4Network(addr, False)
    broadcast = format(net.broadcast_address)

    return broadcast
