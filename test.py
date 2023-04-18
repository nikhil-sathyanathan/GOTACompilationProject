import pandas as pd
import pyarray_to_html_table

SHEET_NAME = "AAPL"
url = input("Please input your URL link")
print(len(url))
index1 = len(url) - 1
slash1Found = False

while slash1Found == False:
    if url[index1] == "/":
        slash1Found = True
    else:
        index1 = index1-1

index2 = index1 - 1
slash2Found = False

while slash2Found ==False:
    if url[index2] == "/":
        SHEET_ID = url[index2+1:index1]
        slash2Found = True
    else:
        index2 = index2-1

url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

print (url)