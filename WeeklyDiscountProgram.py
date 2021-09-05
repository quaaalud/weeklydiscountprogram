import numpy as np
import pandas as pd

### import weekly discount file
### sort to lists rep and company
### sum rep totals and company totals providing output


discounts = pd.read_excel (r"C:\Users\Dale\Desktop\pywip\discounts1.xlsx")
grouped1 = discounts.groupby("Submitted By")
grouped2 = (discounts.groupby("Seller Name")).sum()
aegis = grouped2.iloc[1]
nvps0 = grouped2.iloc[0]
nvps1 = grouped2.iloc[2:5].sum()
nvps = nvps1 + nvps0.sum()

print(aegis)
print(nvps)
print(grouped1.sum())
