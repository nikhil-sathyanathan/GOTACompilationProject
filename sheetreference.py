import pandas as pd
import pyarray_to_html_table

url_init = input("Please input your URL link:\n")

SHEET_NAME = "AAPL"
index1 = len(url_init) - 1
slash1Found = False

while slash1Found == False:
    if url_init[index1] == "/":
        slash1Found = True
    else:
        index1 = index1-1

index2 = index1 - 1
slash2Found = False

while slash2Found ==False:
    if url_init[index2] == "/":
        SHEET_ID = url_init[index2+1:index1]
        slash2Found = True
    else:
        index2 = index2-1
        
        
url_post = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url_post)
arr = df.to_numpy()

arr = arr[:,1:]

print(pyarray_to_html_table.array2htmltable(arr))
