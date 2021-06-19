import pandas as pd

excel_header = ["Router Hostname", "IP address"]
data = [['hostaname 1', '1.1.1.1.1'],['hostname 2','2.2.2.2']]

df = pd.DataFrame(data,columns= excel_header)
writer = pd.ExcelWriter('FromPython.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name="router_list")
writer.save()
