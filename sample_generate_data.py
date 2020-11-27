#!/usr/bin/python

import pandas as pd

df = pd.DataFrame({'first name': ['your_name'], 'last name': ['your_name'], 'employee id': [202005], 'phone no': [223355], 'experience': [5]})

writer = pd.ExcelWriter('sample_xlsx1.xlsx', engine='xlsxwriter')

# write to sheet
df.to_excel(writer, index=False, sheet_name='Sheet1')

writer.save()

reader = pd.read_excel(r'sample_xlsx1.xlsx')
print reader

