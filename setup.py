import subprocess
import sys

def install_dependencies(requirements_file):
    with open(requirements_file, 'r') as file:
        requirements = file.read().splitlines()

    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        subprocess.run(['pip3', 'install', *requirements], check=True)
    elif sys.platform.startswith('win'):
        subprocess.run(['pip', 'install', *requirements], check=True)

requirements_file = './requirements.txt'
install_dependencies(requirements_file)
