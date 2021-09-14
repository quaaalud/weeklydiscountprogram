import numpy as np
import pandas as pd
#from pathlib import Path
#from copy import copy
#from typing import Union, Optional
#import openpyxl
#from openpyxl import load_workbook
#from openpyxl.utils import get_column_letter

### import weekly discount file
### sort to lists rep and company
### sum rep totals and company totals providing output


discounts = pd.read_excel (r"C:\Users\dludwinski\Desktop\wip\All Discounts 9.5.21 to 9.11.21.xlsx")
grouped1 = discounts.groupby("Submitted By")
grouped2 = (discounts.groupby("Seller Name")).sum()
aegis = grouped2.iloc[1]
nvps0 = grouped2.iloc[0]
nvps1 = grouped2.iloc[2:5].sum()
nvps = nvps1 + nvps0.sum()
print(aegis)
print(nvps)
print(grouped1.sum())
print(grouped2)

discount = discounts.sort_values("Seller Name", inplace=True)

discounts.to_excel(r"\\nvpsserver01.nvps.local\CS_ADMIN\Weekly Discount Log\All Discounts September.xlsx", sheet_name="9.5 to 9.11", index=False)
