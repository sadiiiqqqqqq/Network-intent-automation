# Network Intent Automation Tool
<br>
Python-based network automation tool that converts
user intent into router configurations and applies
them automatically.
<br>
------------------- FEATURES ----------------------<br>  
• Generate router configuration from user intent <br>
• Supports routing protocols <br>
• Automated CLI command generation <br>
• Works with GNS3 and physical routers <br>

# INSTALLATION:<br>
git clone https://github.com/username/network-intent-automation
cd network-intent-automation <br>
pip install -r requirements.txt

 # USAGE: <br>
python src/main.py

<br>
EXAMPLES <br>
$ python main.py 
<br>

Enter router hostname: R1 <br>
Enable OSPF? yes <br>
Enable DHCP? no <br>
<br>
Generated configuration: <br>
<br>
hostname R1<br>
router ospf 1<br>
 network 192.168.1.0 0.0.0.255 area 0
 