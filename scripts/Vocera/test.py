def test_py():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("URL")
    ## Login
    id_box = driver.find_element(By.NAME, "login")
    pass_box = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/div[3]") #?
    id_box.send_keys("e103471")
    pass_box.send_keys("Red9977")
    login_button.click()
    ## Navigate to Users tab
    users = driver.find_element(By.NAME, "users")
    users.click()
    driver.implicitly_wait(15)
    # Select appropriate user
    first_name = "Drew"
    last_name = "Meylan"
    uid = f'u-{first_name[0].lower()}{lastname.lower().replace(" ", "_")}'
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