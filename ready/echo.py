# loading necessay libraries
import pandas as pd
import numpy as np
import csv
import os
import matplotlib.pyplot as plt

# definition of working directory
os.chdir('R:/Projects/2020081/Navigation/Water_Bottom_Picks_from_QC')

# definition of variables (seq & line)
seq = input('\n\n\n Enter 3 digit sequence number:')

# selecting the file and extracting the name
path = 'R:/Projects/2020081/Navigation/Water_Bottom_Picks_from_QC'
dirList = os.listdir(path)
for filename in dirList:
    if (filename[4:7] == seq) & (filename[16:] == 'csv'):
        line = str(filename)

# creating the data frame
df = pd.read_csv(line,header=None)

# producing the graph using matplotlib
fig = plt.figure(dpi=100,figsize=([15,5]))
axes1 = fig.add_axes([0.08,0.15,0.88,0.78])

axes1.grid()
axes1.plot(df[0],df[1])
axes1.set_xlabel('Shot point number',fontsize=20)
axes1.set_ylabel('Depth (m)',fontsize=20)
axes1.set_title(f'Seq {line[4:7]}',fontsize=20)

plt.figtext(0.1,0.30,f'Max: {df[1].max():5.2f}m',fontsize=15,backgroundcolor='w')
plt.figtext(0.1,0.25,f'Min: {df[1].min():8.2f}m',fontsize=15,backgroundcolor='w')
plt.figtext(0.1,0.20,f'N shots: {df[1].count():3.0f}',fontsize=15,backgroundcolor='w')

plt.show()