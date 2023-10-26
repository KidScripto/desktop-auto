import selenium
#Initial access
## Using chrome to access the web...
driver = webdriver.Chrome()
## Open the Website
driver.get("VOCERA_URL")

# Login to the Website
## Find userid field
id_box = driver.find_element_by_name("login") #Can do by name too
## Send information to id_box
id_box.send_keys("my_username")
## find password field
pass_box = driver.find_element_by_name("password") #Can do by name too
## Send password
pass_box.send_keys("my_password")
## Find Login button
login_button = driver.find_element_by_xpath("//a[@title='Login']")
## click login button
login_button.click()


# Extract Sidebar Links
status_monitor = driver.find_element_by_name("badgeStatus_link")
sites = driver.find_element_by_name("sites_link")
users = driver.find_element_by_name("users_link")
groups = driver.find_element_by_name("adgroups_link")
departments = driver.find_element_by_name("departments_link")
system = driver.find_element_by_name("system_link")
defaults = driver.find_element_by_name("defaults_link")
ad = driver.find_element_by_name("activedirectory_link")
locations = driver.find_element_by_name("locations_link")
email = driver.find_element_by_name("email_link")
telephony = driver.find_element_by_name("telephony_link")
reports = driver.find_element_by_name("reports_link")
maintenance = driver.find_element_by_name("maintenance_link")
address_book = driver.find_element_by_name("addressbook_link")
devices = driver.find_element_by_name("devices_link")
documentation = driver.find_element_by_name("adocumentation_link")

# Interact with Users...
users.click()

# RUN HEADLESS
options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get('URL')
driver.quit()



'''
https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
'''

