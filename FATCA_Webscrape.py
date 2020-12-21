## Practice script for work. Simple webscrape.

import requests
import pandas as pd

url = 'https://home.treasury.gov/policy-issues/tax-policy/foreign-account-tax-compliance-act'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[0]
print(df)
df.to_csv("C:/Users/Jamie/OneDrive/Documents/Programming/Python and SQL/output.txt", index = None, header = False)
