import selenium
#Initial access
## Using chrome to access the web...
driver = webdriver.Chrome()
## Open the Website
driver.get("VOCERA_URL")

# Login to the Website
## Find userid field
id_box = driver.find_element_by_id("LOGIN USERNAME FIELD ID") #Can do by name too
## Send information to id_box
id_box.send_keys("my_username")
## find password field
pass_box = driver.find_element_by_id("PASSWORD FIELD ID") #Can do by name too
## Send password
pass_box.send_keys("my_password")
## Find Login button
login_button = driver.find_element_by_name("LOGIN BUTTON NAME")
## click login button
login_button.click()


# Select users


'''
https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
'''

