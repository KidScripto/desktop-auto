

class users:
    name:str
    eid:str
    email:str
    cost_center:str
    tmep:bool
    phone:str
    groups:list
    depts:list


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

