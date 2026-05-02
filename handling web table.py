import time
import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
# to print all the data in a table
tabledata=driver.find_element("xpath","//table[@name='BookTable']")
print(tabledata.text,end=' ')


# print table data without heading
row=driver.find_elements('xpath',"//table[@name='BookTable']/tbody/tr")
col=driver.find_elements('xpath',"//table[@name='BookTable']/tbody/tr/th")

for i in range(2,len(row)+1):
    for j in range(1,len(col)+1):
        data=driver.find_element('xpath',f"//table[@name='BookTable']/tbody/tr[{i}]/td[{j}]")
        print(data.text)
        print()


# print all the book with price
row=driver.find_elements('xpath',"//table[@name='BookTable']/tbody/tr")
col=driver.find_elements('xpath',"//table[@name='BookTable']/tbody/tr/th")
for i in range(2,len(row)+1):
        book=driver.find_element('xpath',f"//table[@name='BookTable']/tbody/tr[{i}]/td[1]")
        price=driver.find_element('xpath',f"//table[@name='BookTable']/tbody/tr[{i}]/td[4]")
        print(book.text,price.text)

# to print the book of author amith
row=driver.find_elements('xpath',"//table[@name='BookTable']/tbody/tr")
col=driver.find_elements('xpath',"//table[@name='BookTable']/tbody/tr/th")
for i in range(2,len(row)+1):
    author=driver.find_element('xpath', f"//table[@name='BookTable']/tbody/tr[{i}]/td[2]").text
    if author=="Amit":
       book=driver.find_element('xpath',f"//table[@name='BookTable']/tbody/tr[{i}]/td[1]")
       print(book.text)

