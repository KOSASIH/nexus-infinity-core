# nexus_infinity_core_config_cisco.py
import cisco

# Define the interface configuration
interface_config = {
    "interface": "Ethernet1/1",
    "description": "My Ethernet Interface",
    "ip_address": "10.1.1.1/24",
    "shutdown": False,
}

# Configure the interface using the Cisco Python package
cisco.interface.configure(interface_config)
