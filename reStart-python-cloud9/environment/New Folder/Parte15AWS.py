import os
import subprocess

os.system("ls")
print("\n")
subprocess.run(["ls"])
print("\n")
subprocess.run(["ls","-l"])
print("\n")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print("\n")
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])