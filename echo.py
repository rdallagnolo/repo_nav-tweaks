import pandas as pd
import numpy as np
import csv
import os
import matplotlib.pyplot as plt

os.chdir('/home/zeus/Documents/data_science/nav')

seq = input("Enter 3 digit sequence number: ")

path = '/home/zeus/Documents/data_science/nav'
dirList = os.listdir(path)
for filename in dirList:
    if (filename[4:7] == seq) & (filename[16:] == 'csv'):
        line = str(filename)
#        print(line)

df = pd.read_csv(line,header=None)

fig = plt.figure(dpi=100,figsize=([15,5]))
axes1 = fig.add_axes([0.08,0.15,0.88,0.78])

axes1.grid()
axes1.plot(df[0],df[1])
axes1.set_xlabel('Shot point number',loc='center',fontsize=20)
axes1.set_ylabel('Depth (m)',loc='center',fontsize=20)
axes1.set_title(f'Seq {line[4:7]}',loc='center',fontsize=20)

plt.figtext(0.1,0.55,f'Max: {df[1].max():5.2f}m',fontsize=15,backgroundcolor='w')
plt.figtext(0.1,0.50,f'Min: {df[1].min():8.2f}m',fontsize=15,backgroundcolor='w')
plt.figtext(0.1,0.45,f'N shots: {df[1].count():3.0f}',fontsize=15,backgroundcolor='w')

plt.tight_layout()
plt.show()''