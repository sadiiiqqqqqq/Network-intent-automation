
import input_handler as imp
def collect_user_input():

    config = {}
    config["hostname"] =imp.ask_non_empty("Enter Hostname :")
    config["interface"]= []
    while imp.ask_yes_or_no("Do you want to configure a interface :"):
        iface = {}
        iface["name"]= imp.ask_non_empty("Enter name of interfcae (g0/0):")
        iface["dhcp"]= imp.ask_yes_or_no("Do you want to configure dhcp :")
        if not iface["dhcp"]:
            iface["ip"] =imp.ask_non_empty("Enter IP address :")
            iface["mask"]=imp.ask_non_empty("Enter Subnet mask:")
        config["interface"].append[iface]
    config["ssh"] = []
    choices = imp.ask_choices("Do you want to configure SSh", choice=["ssh","telnet"]):
        issh = {}
    if choices == "ssh":
        issh["local"]= imp.ask_non_empty("Enter Local username :")
        issh["localpass"] = imp.ask_non_empty("Enter local username password")
        issh["domain"] = imp.ask_non_empty("Enter ")
        
    else:
        issh["telnetpass"] = imp.ask_non_empty("Enter telnet password : ")
    config["ssh"].append[issh]
return config
      
