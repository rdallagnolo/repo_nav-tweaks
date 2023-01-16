# loading necessay libraries
import pandas as pd
import os

# definition of working directory
os.chdir('R:/Projects/2020081/Navigation/Water_Bottom_Picks_from_QC/Ebird depths')

# variables
fsp = int(input("\n\n\nEnter FSP: "))
lsp = int(input("\n\n\nEnter LSP: "))
depth = float(input("\n\n\nEnter depth: "))
no = input("\n\n\nEnter sequence number: ")             # used for final file name only
bird = input("\n\n\nEnter ebird number (ex:S1E33): ")   # used for final file name only

# set conditions for incrementing or decrementing shot points
s = 1
x = lsp + 1
if fsp > lsp:
    s = -1
    x = lsp - 1

# the list for shot points
st = list(range(fsp, x, s))

# the list for depth data
dt = []
for i in range(len(st)):
    dt.append(depth)

# concatenating the above lists to a data frame
df = pd.DataFrame(list(zip(st, dt)))

# exporting to csv
df.to_csv(f'Seq{no}_{bird}.csv',header=False,index=False)

# Exit message
print(f'\n\n\n DONE!!!  you can now import Seq{no}_{bird}.csv in Iris \n\n\n')