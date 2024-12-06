from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFileUpload(TestCase):

    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_user_can_upload_pdf_file(self):
        self.browser = webdriver.Chrome()
        self.url = "localhost:8000"
        # go to the webpage
        self.browser.get(self.url)
        self.assertEqual("File Upload", self.browser.title)
        # find the file upload
        pdf_upload = self.browser.find_element(By.ID, "pdf_upload")
        submit = self.browser.find_element(By.ID, "submit")
        # upload the file
        pdf_upload.send_keys("functional_tests/invoice.pdf")
        submit.click()
        # verify that the file pops up in the window
        files = self.browser.find_elements(By.CLASS_NAME, "file")
        self.assertEqual(1, len(files))        

    def test_user_cannot_upload_non_pdf_file(self):
        pass