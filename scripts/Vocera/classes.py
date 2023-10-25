

class users:

class devices:

class emails:

class department:

class addressbook:

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

