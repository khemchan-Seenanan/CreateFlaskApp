#!/usr/bin/env python3
import os 
import platform
plt = platform.system()

def install():
    try:
        os.system("mkdir -p ~/bin_dir")
        os.system("cp createflaskapp code.py ~/bin_dir")
    except OSError:
        print(" \033[1;31;40m Couldn't INSTALL the createflaskapp command!!!!!")
    else:
        print(f" \033[2;33;40m ---- RUN THE FOLLOWING COMMAND!! ---- \n")
        print(" \033[1;32;40m createflaskapp command installed SUCCESSFULLY!!")
        if(plt == "Darwin"):
            print(" \033[1;33;40m RUN \033[1;36;40m echo 'export PATH=$PATH\":$HOME/bin_dir\"' >> ~/.bash_profile && source ~/.bash_profile \033[1;33;40m TO complete the installation\n")
        elif(plt == "Linux"):
            print(" \033[1;33;40m RUN \033[1;36;40m echo 'export PATH=$PATH\":$HOME/bin_dir\"' >> ~/.bashrc && source ~/.bashrc \033[1;33;40m TO complete the installation\n")
        
    
if __name__ == "__main__":
    install()