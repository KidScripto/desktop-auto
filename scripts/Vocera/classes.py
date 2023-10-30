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
        ## Create user in vocera?
    
    def __del__(self):
        print(f'User {self.name} removed')
    
    # Generic functions
    def set_val(self, attribute_name:str, new_value:str) -> None:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.chrome.options import Options


         # change class instance locally
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, new_value)
            # change class in Admin Console
            try:
                options = Options()
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
                # Select appropriate user
                uid = f'u-{self.first_name[0].lower()}{self.lastname.lower().replace(" ", "_")}'
                search_frame = driver.find_element(By.NAME, "searchlist")
                driver.switch_to.frame(search_frame)
                target = driver.find_element(By.XPATH, f'//*[@id="{uid}"]')
                actions = ActionChains(driver)
                actions.double_click(target).perform() # Opens edit user window
                # iFrame switch to DialogBox
                diaframe = driver.find_element(By.ID, "iframeDialog")
                driver.switch_to.frame(diaframe)
                ## Maybe swap again?
                diaframe2 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/iframe")
                driver.switch_to.frame(diaframe2)
                #----------------- Branch --------------------#
                if attribute_name == "first_name":
                    ## Maybe move DiaFrame2 iframe swap to here ?? and others...
                    #Make Changes in Admin Console
                    fname = driver.find_element(By.NAME, "firstname")
                    fname.clear()
                    fname.send_keys(new_value)
                    # Save Changes in Admin Console
                    save_button = driver.find_element(By.ID, "savebutton")
                    save_button.click()
                    # Make and save changes in SoT !!!
                    pass
                if attribute_name == "last_name":
                    # Make changes in Admin Console
                    lname = driver.find_element(By.NAME, "lastname")
                    lname.clear()
                    lname.send_keys(new_value)
                    # Save Changes in Admin Console
                    save_button = driver.find_element(By.ID, "savebutton")
                    save_button.click()
                    # Make and save changes in SoT !!!
                    pass
                    # Kill connection
                    driver.quit()
                if attribute_name == "eid":
                    pass
                if attribute_name == "email":
                    pass
                if attribute_name == "cost_center":
                    pass
                if attribute_name == "temp":
                    pass
                if attribute_name == "phone":
                    pass
                if attribute_name == "groups":
                    pass
                if attribute_name == "depts":
                    pass
            except Exception as err:
                print(f'Error encountered: {err}'
                return 1
        else:
            print(f'Attribute {attribute_name} does not exist!')
 
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

