import random
import string
from dataclasses import dataclass, field

@dataclass
class User:
    first_name:str = ''
    last_name:str = ''
    eid:str = ''
    email:str = ''
    cost_center:str = ''
    temp:bool = False
    phone:str = ''
    groups:str = ''
    depts:str = ''
    _search_str:str = field(init=False)

    def __post_init__(self) -> None:
        self.search_string = f'{self.name} {self.eid}'
    
    def __del__(self):
        print(f'User {self.name} removed')
    
    # Generic functions
    def set_val(self, attribute_name, new_value):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.action_chains import ActionChains

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
        ## Navigate to Users tab
        users = driver.find_element(By.NAME, "users")
        users.click()
        driver.implicitly_wait(15)
        ## Select Correct User
          ## Define name var
        tname = self.name.split(" ")
        name = tname[0][0].lower() + tname[1].lower()
          ## Select User
        frame = driver.find_element(By.NAME, "searchlist")
        driver.switch_to.frame(frame)
        target = driver.find_element(by.XPATH, f'//*[@id="u-{name}"]')
        actions = ActionChains(driver)
        actions.double_click(target).perform() ## Opens the Edit User window
        ## --------------------------------------------------------
        ## Open Appropriate Link
        ### iFrame switch to DialogBox
        diafram = driver.find_element(By.ID, "iframeDialog")
        driver.switch_to.frame(diafram)
        ### Maybe swap iFrame again?
        diafram2 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/iframe")
        driver.switch_to.frame(diafram2)
        ### Select link or Field
        if attribute_name == "name":
            fname = driver.find_element(By.NAME, "firstname")
            lname = driver.find_element(By.NAME, "lastname")
            fname.clear()
            lname.clear()
            fname.send_keys("NAME")
            lname.send_keys("NAME")
            ### Create Save Button attribute and Click it
            save_button = driver.find_elemenet(By.ID, "savebutton")
            save_button.click()
            ### Kill connection
            driver.quit() # Close webdriver session
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
@dataclass
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

@dataclass
class addressbook:
    name:str
    entry_type:str
    phone:str
    email:str
    pager:str
    site:str

'''
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
'''
# Generate user instances from CSV. Have to create the CSV with selenium by scraping the admin portal
def gen_instances(file):
    import csv
    persons = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            person.append(User(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7])) 

def generate_id() -> str:

