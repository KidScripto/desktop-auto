
'''
class users:

    def __init__(self, name, eid, email, cost_center, temp, phone, groups, depts):
        self.name =
    # General operations
'''

class User:
    # Init and destructors
    def __init__(self, name, eid, email, cost_center, temp, phone, groups, depts):
        self.name = name
        self.eid = eid
        self.email = email
        self.cost_center = cost_center
        self.temp = temp
        self.phone = phone
        self.groups = groups
        self.depts = depts
    
    def __del__(self):
        print(f'User {self.name} removed')
    
    # Generic functions
    def set_attr(self, attribute_name, new_value):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

         # change class instance within
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, new_value)
        else:
            print(f'Attribute {attribute_name} does not exist!')

        # make changes in Admin Console w/ Selenium
        ## Create Driver object
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        driver.get("URL")
        ## Login
        id_box = driver.find_element(By.NAME, "login")
        pass_box = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "/html/body/div[3]") #?
        id_box.send_keys("USERNAME")
        pass_box.send_keys("PASSWD")
        login_button.click()
        ## Open Appropriate Link
        if attribute_name == "name":
            # Make changes
            pass
        if attribute_name == "eid":
            # Make changes
            pass
        if attribute_name == "emial":
            # Make changes
            pass
        if attribute_name == "cost_center":
            # Make changes
            pass
        if attribute_name == "temp":
            # Make changes
            pass
        if attribute_name == "phone":
            # Make changes
            pass
        if attribute_name == "groups":
            # Make changes
            pass
        if attribute_name == "depts":
            # Make changes
            pass
        
        ## Terminate connection
        driver.quit()
    
    def remove_user(self):
        # Log into vocera admin and delete user
        
        # call destructor function
        del self

class devices:
    serial:str
    mac:str
    label:str=None
    status:str
    devtype:str
    site:str
    last_user:str
    last_location:str
    local_site:str
    ip_addr:str

class addressbook:
    name:str
    entry_type:str
    phone:str
    email:str
    pager:str
    site:str

def login(username, password):
    from selenium import driver
    from selenium.webdriver.common.by import By
    driver = webdriver.chrome
    driver.get("VOCERA_URL")
    id_box = driver.find_element(By.NAME, "login")
    pass_box = driver.find_elemenet(By.NAME, "password")
    login_button = driver.find_elemenet(By.XPATH, "/hmtl/body/div[3]")
    id_box.send_keys(username)
    pass_box.send_keys(password)
    login_button.click()

def add_user()

def remove_user(

# Generate user instances from CSV. Have to create the CSV with selenium by scraping the admin portal
def gen_instances(file):
    import csv
    persons = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            person.append(User(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7])) 
