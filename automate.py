import subprocess

for n in range(1,35):	
	this_command = "echo N="+str(n/10.0)+">> constants.py"
	subprocess.Popen(this_command.split())
	
	this_command = "echo python encoder.py --path testimg/emma.png >> output.txt"
	subprocess.Popen(this_command.split())

	this_command = 'echo ,  >> output.txt'
	subprocess.Popen(this_command.split())

	this_command = "echo python  img_sim.py>> output.txt"
	subprocess.Popen(this_command.split())

	this_command = 'echo \n  >> output.txt'
	subprocess.Popen(this_command.split())


