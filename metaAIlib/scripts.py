from metaAIlib.resources import *

class myfunctions:
    def __init__(self):
        self.webdriverWait = WebDriverWait(self.driver, 10)
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--headless=new")
        self.driver = webdriver.Edge(options)

    def openbrowser(self):
        # Initialize the WebDriver
        self.driver.get('https://www.meta.ai/')
        sign_in = '(//*[@class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"])[1]'
        nav = '//*[@aria-label="Open navigation"]'
        nav1 = '//*[@aria-label="Open menu"]' 
        nav2 = '//*[@aria-label="Open Menu"]'
        profile = '//div[@aria-label="profile"]'
        array = [(By.XPATH,sign_in),(By.XPATH,nav),(By.XPATH,nav1), (By.XPATH,nav2), (By.XPATH,profile)]
        try:
            self.driver.execute_script("return document.readyState") == "complete"
            element = self.driver.find_element(By.XPATH,profile)
            if element.is_displayed():
                pass
            else:
                print("Element is not displayed")
        except NoSuchElementException:
            print("No such element")
            for by, value in array:
                try:
                    self.driver.execute_script("return document.readyState") == "complete"
                    element = self.driver.find_element(by, value)
                    if element.is_displayed():
                        element.click()
                        print(element)
                        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,sign_in)))
                        signin = self.driver.find_element(By.XPATH,sign_in)
                        self.driver.execute_script("arguments[0].scrollIntoView();", signin)
                        self.driver.execute_script(f"arguments[0].click();", signin)
                        pass
                    else:
                        print("Element is not displayed")
                        break
                except NoSuchElementException:
                    print("No such element")
        
    def instalogin(self, user="",password=""):
        iSignIn = self.driver.find_element(By.XPATH,'//*[contains(text(),"Log in with Instagram")]')
        iSignIn.click()
        keywords = "instagram"
        WebDriverWait(self.driver, 30).until(lambda d: keywords in d.current_url)
        self.driver.execute_script("return document.readyState") == "complete"
        login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        Pass = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        element_locator = (By.XPATH,login)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(element_locator))
        self.driver.find_element(By.XPATH,login).send_keys(user)
        self.driver.find_element(By.XPATH,Pass).send_keys(password)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        not_now = (By.XPATH,'//*[contains(text(),"Not now")]')
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(not_now))
        self.driver.find_element(By.XPATH,'//*[contains(text(),"Not now")]' or '//*[contains(text(),"Not Now")]').click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[contains(text(),"Log in as")]')))
        self.driver.find_element(By.XPATH,'//*[contains(text(),"Log in as")]').click()

    def fblogin(self, user="",password=""):
        fbSignIn = self.driver.find_element(By.XPATH,'//*[contains(text(),"Log in with Facebook")]')
        fbSignIn.click()
        user = '//*[@name="email"]'
        passw = '//*[@name="pass"]'
        keywords = "facebook"
        WebDriverWait(self.driver, 30).until(lambda d: keywords in d.current_url)
        self.driver.execute_script("return document.readyState") == "complete"
        element_locator = (By.XPATH,user)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(element_locator))
        self.driver.find_element(By.XPATH,user).send_keys(user)
        self.driver.find_element(By.XPATH,passw).send_keys(password)
        self.driver.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
        Continue = (By.XPATH,'//*[contains(text(),"Continue to Meta AI")]')
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(Continue))
            title = '//*[@title="Log in"]'
            self.driver.find_element(By.XPATH,title).click()
        except:
            pass

    def Input(self, prompt="", no_of_images="",directory=""):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="Ask Meta AI anything..."]')))
        input_field = self.driver.find_element(By.XPATH, '//*[@placeholder="Ask Meta AI anything..."]')
        input_field.send_keys(prompt)
        send = self.driver.find_element(By.XPATH,'//div[@aria-label="Send message"]' or '//button[@aria-label="Send message"]')
        send.click()
        if no_of_images == "":
            no_of_images = 1
        else:
            no_of_images = int(no_of_images)
        for n in range(no_of_images):
            img = f"(//img[@alt='Image generated by meta.ai'])[{n}]"
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,img)))
            print(self.driver.find_element(By.XPATH,img))
            img_url = self.driver.find_element(By.XPATH,img).get_attribute("src")
            img_data = requests.get(img_url).content
            if directory:
                with open(f"{directory}/image{n}.jpg", 'wb') as handler:
                    handler.write(img_data)
            else:
                with open(f"output/image{n}.jpg", 'wb') as handler:
                    handler.write(img_data)