import argparse
import os
import subprocess
import code
import platform 

def banner():
    print("""\033[1;36;40m
 _____                    _          ______ _              _       ___                 _  _              _    _                
/  __ \                  | |        |  ___|| |            | |     / _ \               | |(_)            | |  (_)               
| /  \/ _ __  ___   __ _ | |_  ___  | |_   | |  __ _  ___ | | __ / /_\ \ _ __   _ __  | | _   ___  __ _ | |_  _   ___   _ __   
| |    | '__|/ _ \ / _` || __|/ _ \ |  _|  | | / _` |/ __|| |/ / |  _  || '_ \ | '_ \ | || | / __|/ _` || __|| | / _ \ | '_ \  
| \__/\| |  |  __/| (_| || |_|  __/ | |    | || (_| |\__ \|   <  | | | || |_) || |_) || || || (__| (_| || |_ | || (_) || | | | 
 \____/|_|   \___| \__,_| \__|\___| \_|    |_| \__,_||___/|_|\_\ \_| |_/| .__/ | .__/ |_||_| \___|\__,_| \__||_| \___/ |_| |_| 
    by Khemchan Seenanan                                                | |    | |                                             
                                                                        |_|    |_|                                             
    """)



def execute_command(cmd):
    os.system(cmd)

#function to get all the arguments the user specifies
def getArgs():
    parser = argparse.ArgumentParser(description='Create a flask project.')
    parser.add_argument('name',metavar='name_of_project' ,type=str , help='name of the project')
    args = parser.parse_args()
    return args


#function for making a directory 
def mkdir(name):
    try:
        os.mkdir(name)
    except OSError:
        print(f" \033[1;31;40m => A folder with the name {name} already exists!!!!")
        exit()
    else:
        print(f" \033[1;32;40m => Successfully created {name}!")


#function for creating a virtual environment
def create_virtual_environment(name):
    try:
        execute_command(f"python3 -m venv {name}/venv")

    except OSError:
        print(" \033[1;31;40m => ERROR: Failed to create virtual environment!!!")
    else:
        print(" \033[1;32;40m => Virtual Environment created successfully!!!")

#function for making a file
def touch(name, code):
    f = open(name, "w+")
    f.write(code)
    f.close()

#function that upgrades pip
def upgrade_pip(name):
    print("")
    print(" \033[1;35;40m ==== UPGRADING PIP ====\n")
    execute_command(f"{name}/venv/bin/pip install pip --upgrade")
    print("")
    print(" \033[1;32;40m **** Successfully upgraded PIP ****\n")

#function that installs flask  
def install_flask(name):
    print("")
    print(" \033[1;35;40m ==== INSTALLING FLASK ====\n")
    execute_command(f"{name}/venv/bin/pip install flask")
    print("")
    print(" \033[1;32;40m **** Successfully INSTALLED FLASK ****\n")





#main routine  
def main():
    banner()
    
    # collect Arguments and parse them
    arguments = getArgs()

    plt = platform.system()
    if(plt == "Linux"):
        execute_command("apt-get install python3-venv")
    else:
        print("Install python venv before beginin!!!")
        exit()

    # Create folder that houses the project
    mkdir(arguments.name)
    
    #creat the a virtual environment
    create_virtual_environment(arguments.name)

    #flask app entry point
    touch(f"{arguments.name}/run.py", code.run_code(arguments.name))

    #create folder that houses the project files
    mkdir(f"{arguments.name}/{arguments.name}")


    touch(f"{arguments.name}/{arguments.name}/__init__.py" , code.init_code(arguments.name))

    touch(f"{arguments.name}/{arguments.name}/views.py", code.views_code(arguments.name))

    mkdir(f"{arguments.name}/{arguments.name}/static")
    mkdir(f"{arguments.name}/{arguments.name}/static/CSS")
    touch(f"{arguments.name}/{arguments.name}/static/CSS/style.css", code.css_code())
    mkdir(f"{arguments.name}/{arguments.name}/static/IMAGES")
    mkdir(f"{arguments.name}/{arguments.name}/static/JAVASCRIPT")
    touch(f"{arguments.name}/{arguments.name}/static/JAVASCRIPT/script.js", code.js_code())

    mkdir(f"{arguments.name}/{arguments.name}/templates")
    mkdir(f"{arguments.name}/{arguments.name}/templates/public")
    touch(f"{arguments.name}/{arguments.name}/templates/public/index.html", code.index_code())
    mkdir(f"{arguments.name}/{arguments.name}/templates/public/base_templates")
    touch(f"{arguments.name}/{arguments.name}/templates/public/base_templates/public_base.html", code.base_code())

    upgrade_pip(arguments.name)
    install_flask(arguments.name)

    print("")
    print(f" \033[2;33;40m ---- RUN THE FOLLOWING COMMAND!! ---- \n")
    print(f" \033[1;36;40m source {arguments.name}/venv/bin/activate && export FLASK_APP={arguments.name}/run.py && export FLASK_ENV=development")
    print("")
    print(" \033[1;33;40m RUN \033[1;36;40m flask run \033[1;33;40m TO START THE SERVER\n")
    
    

    


if __name__ == "__main__":
    main()











    




