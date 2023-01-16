import pandas as pd

os.chdir('/home/zeus/Documents/data_science/nav/zDGPS')

fsp = int(input("\n\n\nEnter FSP: "))
lsp = int(input("\n\n\nEnter LSP: "))
depth = float(input("\n\n\nEnter depth: "))
no = input("\n\n\nEnter sequence number: ")
bird = input("\n\n\nEnter ebird number (ex:S1E33)")

s = 1
x = lsp + 1
if fsp > lsp:
    s = -1
    x = lsp - 1

st = list(range(fsp, x, s))

dt = []
for i in range(len(st)):
    dt.append(depth)

df = pd.DataFrame(list(zip(st, dt)))

df.to_csv(f'Seq{no}_{bird}.csv',header=False,index=False)
