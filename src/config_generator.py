
import input_handler as imp
def collect_user_input():

    config = {}
 
    config["hostname"] =imp.ask_non_empty("Enter Hostname :")

    config["interface"] = []

    while imp.ask_yes_or_no("Do you want to configure a interface :"):
        iface = {}
        iface["name"]= imp.ask_non_empty("Enter name of interfcae (g0/0):")
        iface["dhcp"]= imp.ask_yes_or_no("Do you want to configure dhcp :")
        
        if not iface["dhcp"]:
            iface["ip"] =imp.ask_non_empty("Enter IP address :")
            iface["mask"]=imp.ask_non_empty("Enter Subnet mask :")
        
        config["interface"].append(iface)

    config["connections"] =[]
    issh = {}
    issh["choice"] = imp.ask_choices("Choose remote connetions :", ["ssh","telnet"])
    if  issh["choice"]== "ssh":
        if config["hostname"] == "":
            print("Hostname requires for ssh")
            config["hostname"] = imp.ask_non_empty("Enter hostname :")
        else:
            
            issh["local"]= imp.ask_non_empty("Enter Local username :")
            issh["localpass"] = imp.ask_non_empty("Enter local username password")
            issh["domain"] = imp.ask_non_empty("Enter domain Name: ")
            issh["key"] = 2048 
    else: 
        issh["telnetpass"] = imp.ask_non_empty("Enter Telnet password")
    config["connections"].append(issh)
    return config 
def generate_config(cfg: dict)-> list:
    lines = []    
    lines.append("enable")
    lines.append("Conf t ")
    lines.append(f"hostname {cfg["hostname"]}")
    for iface in cfg["interface"]:
        if iface["dhcp"] :
            d = iface["dhcp"]
            lines.append(f"interface {d["name"]}")
            lines.append("ip address dhcp ")
            lines.append("no shutdown")
            lines.append("exit")
        else :
            lines.append(f"interface {d["name"]}")
            lines.append(f"ip address {d["ip"]} {d["mask"]}")
            lines.append(f"no shutdown ")
            lines.append("exit")
    for issh in cfg["connections"]:
        s = issh
        if s["choice"]=="ssh":
            lines.append(f"ip domain {s["domain"]}")
            lines.append(f"username {s["local"]} priviledge 15 secret {issh["localpass"]}")
            lines.append(f"crypto key generate rsa {s["key"]}")
            lines.append("line vty 0 3 ")
            lines.append("login local")
            lines.append("transport input ssh ")
            lines.append("exit")
        else:
            lines.append("line vty 0 3 ")
            lines.append(f"password {s["telnetpass"]}")
            lines.append("transport input telnet")
            lines.append("exit")
    return lines  
        
    

