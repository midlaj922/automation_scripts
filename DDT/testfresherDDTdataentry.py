import Utilities
import openpyxl
import Utilities
# writing data
for i in range(1,6):
    for j in range(1,4):
        Utilities.write_data(r'C:\Users\MD. MIDELAJ\Desktop\SELENIUM\DDT\TestfreshDDT.xlsx','Sheet1',i,j,input(f"enter data {i,j}"))


 # reading data
path=r'C:\Users\MD. MIDELAJ\Desktop\SELENIUM\DDT\TestfreshDDT.xlsx'
row=Utilities.rows_count(path,'Sheet1')
col=Utilities.columns_count(path,'Sheet1')

for i in range(1,row+1):
    for j in range(1,col+1):
        print(Utilities.read_data(r'C:\Users\MD. MIDELAJ\Desktop\SELENIUM\DDT\TestfreshDDT.xlsx','Sheet1',i,j,),end=' ')
    print()
