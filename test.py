import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_failed_login_with_empty_password(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_a_failed_login_with_wrong_password(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_a_failed_login_with_empty_email_and_password(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_a_success_login(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_a_failed_signup_all_empty(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_a_failed_signup_empty_name(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("sanber@tes")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys("seleniumpython")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_a_failed_signup_empty_email(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("sanbertes")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys("seleniumpython")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_a_failed_signup_empty_password(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("sanbertes")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("sanber@tes")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()