import pandas as pd
from openpyxl import load_workbook
from random import random, randint, choice, shuffle

# df = pd.DataFrame({
#    'Customer_Bkey': [random_el=choice(['demo1', 'demo2'])],
#    'Source_System_Name': [random_el=choice(['demo1', 'demo2'])]})

writer = pd.ExcelWriter('demoooo.xlsx', engine='xlsxwriter')
#df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
