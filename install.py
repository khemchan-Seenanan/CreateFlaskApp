import os 

def install():
    os.system("mkdir -p ~/bin_dir")
    os.system("cp createflaskapp code.py ~/bin_dir")
    os.system("export PATH=$PATH':$HOME/bin_dir'")
    
if(__name__ == "__main__"):
    install()