# nexus_infinity_core_config_eem.py
from cli import *

# Define the EEM applet
eem_applet = """
event manager applet my_applet
  event cli match "show clock"
  action 1 cli command "configure terminal ; vrf context myvrf"
"""

# Register the EEM applet
cli(eem_applet)
