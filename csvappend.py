import os, csv, random

#a function that returns a random serial number and noise value for testing
def random():
	import random
	x = random.randint(10000,99999)
	serialnumber = "AUAA8340" + str(x)
	noiseRelEV2 = random.randint(1,20)
	return (serialnumber, noiseRelEV2)

#assigning variable names to the output of the random function
serialnumber, noiseRelEV2 = random()
#changing directory to location of log file
os.chdir(r"C:\Users\shaggart\Desktop\Python\CSV_files")
#putting variables into a dictionary that will be written to log file
row = [serialnumber, noiseRelEV2]
#opening logfile to append, assisnging a variable to the logfile writer and writing the row
with open("logfile.csv", "a", newline='') as logfile:
	writer = csv.writer(logfile)
	writer.writerow(row)


