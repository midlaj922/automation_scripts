import openpyxl
import Utilities
# writing data
for i in range(1,7):
    for j in range(1,4):
        Utilities.write_data(r'C:\Users\MD. MIDELAJ\Desktop\SELENIUM\DDT\DDT.xlsx','Sheet1',i,j,)


 # reading data
path=r'C:\Users\MD. MIDELAJ\Desktop\SELENIUM\DDT\DDT.xlsx'
row=Utilities.get_row(path,'Sheet1')
col=Utilities.get_col(path,'Sheet1')

for i in range(1,7):
    for j in range(1,4):
        print(Utilities.read_data(r'C:\Users\MD. MIDELAJ\Desktop\SELENIUM\DDT\DDT.xlsx','Sheet1',i,j,),end='')
    print()
