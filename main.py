import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Credentials & Constants
email = "ab@gmail.com"
password = "gth!132a"
text = "ric"
size = 20
timeout = 2

def scroll_down(driver,tb):
        driver.execute_script("arguments[0].scrollIntoView();", tb[-1])
        time.sleep(2)

#initialize web driver
def home():
    driver = webdriver.Chrome(
    executable_path="C:\\Users\\abalek\\Downloads\\chromedriver_win32\\chromedriver.exe")

    # driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    print("Website Entered")
    time.sleep(timeout)
    return driver


def login(driver, email, pw):
    time.sleep(timeout)
    email_field = driver.find_element(By.XPATH,'(//input[@id="outlined-basic"])[1]')
    email_field.send_keys(email)
    pw_field = driver.find_element(By.XPATH,'(//input[@id="outlined-basic"])[2]')
    pw_field.send_keys(pw)
    login_button = driver.find_element(By.XPATH, '//button[@type="button"]')
    login_button.click()
    
#Checking for Validity in names
def search(driver,text):
    time.sleep(timeout)
    search_field = driver.find_element(By.XPATH,'//input')
    search_field.send_keys(text)
    time.sleep(4)
    
    try:

        character_list = []
        tb = driver.find_elements(By.XPATH,'//div[@data-field="name"]/div[@class="MuiDataGrid-cellContent"]')
        
        character_list.extend([character.text for character in tb])

        while True:
            scroll_down(driver,tb)

            tb = driver.find_elements(By.XPATH,'//div[@data-field="name"]/div[@class="MuiDataGrid-cellContent"]')    
            
            character_list.extend([character.text for character in tb if character.text not in character_list])
            if len(character_list)==size:
                 break
        
        incorrect = 0

        for character in character_list:
            if text not in character.lower():
                incorrect +=1
        
        print("Valid Entries : ", size-incorrect)
        print("Incorrect : ", incorrect)

                     
        time.sleep(timeout)
    finally:
        pass

#Checking if sort is right
#First order is none, then on click ascending, then descending

def order(driver,text):
    time.sleep(timeout)
    search_field = driver.find_element(By.XPATH,'//input')
    search_field.send_keys(text)
    time.sleep(2)

    nh = driver.find_element(By.XPATH,'//div[@class="MuiDataGrid-columnHeaderTitleContainer"]')
    
    nh.click()
    nh.click() #descending
    time.sleep(2)

    name_heading = driver.find_element(By.XPATH,'//div[@aria-label="Name"]')
    order_by = name_heading.get_attribute('aria-sort')    

    #3 orders - none, ascending, descending
    
    try:

        character_list = []
        tb = driver.find_elements(By.XPATH,'//div[@data-field="name"]/div[@class="MuiDataGrid-cellContent"]')
        
        character_list.extend([character.text for character in tb])

        while True:
            scroll_down(driver,tb)

            tb = driver.find_elements(By.XPATH,'//div[@data-field="name"]/div[@class="MuiDataGrid-cellContent"]')    
            
            character_list.extend([character.text for character in tb if character.text not in character_list])
            if len(character_list)==size:
                 break
        
        temp_list = character_list

        print(character_list)
        print(temp_list)
        
        if order_by=='ascending':
            temp_list.sort()
            print(temp_list == character_list)
            if temp_list == character_list:
                
                print("Ascending Order Validated")
            else:
                print("Not in Ascending Order")
        
        if order_by=='descending':
            temp_list.sort(reverse=True)
            if temp_list == character_list:
                print("Descending Order Validated")
            else:
                print("Not in Descending Order")

                     
        time.sleep(timeout)
    finally:
        pass
     
    


#Run either search or order

website = home()
login(website,email,password)
print("User is Logged In")

print("Verifying Search")
search(website,text)

# print("Order Validation")
# order(website,"morty")



