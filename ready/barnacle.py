# loading necessary libraries
import os
import pandas as pd
import csv
from datetime import date

# Definition of working directory
os.chdir('R:/Projects/2020081/Navigation/Geospeedometer_Speed_Tension')

# Definition of Variables (seq & line_dir)
seq = input("Enter 3 digit sequence number: ")

path = 'R:/Projects/2020081/Navigation/Geospeedometer_Speed_Tension'
dirList = os.listdir(path)
for filename in dirList:
    if (filename[11:14] == seq) & (filename[36:] == 'csv'):
        line = str(filename)

line_dir = input("Enter line direction (for example 180): ")


# Reading the file and creating the data frame
# Original csv has empty rows  before the header..hence encoding is 'windows-1252'
# Refactoring column names
df = pd.read_csv(line, encoding='windows-1252', skiprows=[0,1,2,3], header=1)	    	    
df.columns=['Shot #', 'Time', 'V1 BSP m/s', 'V1WS1 Raw m/s', 'V1 CMG ｰ',					
			'NB1TN1 Raw Average Tension kg', 'NB2TN1 Raw Average Tension kg',
            'NB1TN2 Raw Average Tension kg', 'NB2TN2 Raw Average Tension kg']

# Summary statistics operation on the data frame
out = [df['V1 BSP m/s'].mean(),
	   df['V1 BSP m/s'].min(),
	   df['V1 BSP m/s'].max(),
       df['V1WS1 Raw m/s'].mean(),
       df['NB1TN1 Raw Average Tension kg'].mean(),
       df['NB1TN1 Raw Average Tension kg'].std(),
       df['NB1TN1 Raw Average Tension kg'].min(),
       df['NB1TN1 Raw Average Tension kg'].max(),
       df['NB2TN1 Raw Average Tension kg'].mean(),
       df['NB2TN1 Raw Average Tension kg'].std(),
       df['NB2TN1 Raw Average Tension kg'].min(),
       df['NB2TN1 Raw Average Tension kg'].max()]

# List of strings as output 
out2 = ['{:.4f}'.format(x) for x in out]			# formating number of decimals
out_h = [str(date.today().isocalendar()[1]),		# week number 
        date.today().strftime("%m-%d-%y"),			# today's date
        int(line[11:14]),line_dir+'°',0,]   		# seq number, heading, placeholder for excel formula
out_final = out_h + out2							# concatenating lists

# Writing to the final csv file
def write_to_csv(out_final):
     with open('nav_out.csv', 'a', newline='') as csvfile:
         writer = csv.writer(csvfile)
         writer.writerow(out_final)
write_to_csv(out_final)

# Exit message
print('\n\n\n DONE!!!  Check the nav_out.csv file \n\n\n')