# nexus_infinity_core_config.py
from cli import *

# Define the configuration commands
commands = [
    "configure terminal",
    "vrf context myvrf",
    "interface Ethernet1/1",
    "  no shutdown",
    "  description My Ethernet Interface",
    "  ip address 10.1.1.1/24",
    "  no ip redirects",
    "  no ip unreachables",
    "  no ip proxy-arp",
    "  ip route-cache same-interface",
    "  ip icmp redirect",
    "  no shutdown",
]

# Execute the configuration commands
for command in commands:
    cli(command)
