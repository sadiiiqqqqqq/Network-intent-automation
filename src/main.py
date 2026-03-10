import config_generator as cg 
import input_handler as ip 
import router_executor as r
print("test")

cfg = cg.collect_user_input()
commands = cg.generate_config(cfg)
port = ip.ask_non_empty("Enter GNS3 socket No.")
r.apply_gns3(commands,port)






