from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import getcwd
from time import sleep
from django.urls import reverse


class TestFileUpload(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = f"{self.live_server_url}{reverse('add_file')}"
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_user_can_upload_pdf_file(self):
        # Test to try and upload a file, then display the file on the side of the screne under recent uploads
        # go to the webpage
        self.browser.get(self.url)
        self.assertEqual("File Upload", self.browser.title)
        self.assert_Files_Uploaded(0)
        # send the file
        self._submit_file(f"{getcwd()}/functional_tests/invoice.pdf")
        # verify that the file pops up in the window
        self.assert_Files_Uploaded(1)       

    def test_user_cannot_upload_non_pdf_file(self):
        # Test to try and upload a file, then display the file on the side of the screne under recent uploads
        # go to the webpage
        self.browser.get(self.url)
        self.assertEqual("File Upload", self.browser.title)
        # check that there are no files uploaded
        self.assert_Files_Uploaded(0)
        # try to save a txt file to the server
        self._submit_file(f"{getcwd()}/functional_tests/bad.txt")
        # assert the number of files remains the same
        self.assert_Files_Uploaded(0)

    def _submit_file(self, path):
        # find the file upload
        pdf_upload = self.browser.find_element(By.ID, "pdf_upload")
        submit = self.browser.find_element(By.ID, "submit")
        # upload the file
        pdf_upload.send_keys(path)
        submit.click()
        

    def assert_Files_Uploaded(self, x):
        # asserts that there are x files recetly uploaded
        files = self.browser.find_elements(By.CLASS_NAME, "file")
        self.assertEqual(x, len(files)) 


class TestOrderVeiwing(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = f"{self.live_server_url}{reverse('add_file')}"
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_veiw_uploaded_orders(self):
        # upload an invoice file
        self.browser.get(self.url)
        self._submit_file(f'{getcwd()}/functional_tests/invoice.pdf')
        # navigate to the orders page
        self.url = f"{self.live_server_url}{reverse('view_orders')}"
        self.browser.get(self.url)
        self.assertEqual("Orders", self.browser.title)
        # click the link to the order you want to view
        recent_order = self.browser.find_elements(By.CLASS_NAME, "order")[0]
        recent_order.click()
        # view the order date
        date = self.browser.find_element(By.ID, "order_date")
        self.assertEqual(date, "00/00/0000")
        # view the total price
        price = self.browser.find_element(By.ID, "order_price")
        self.assertEqual(date, "$00.00")
        # view the outages
        outages = self.browser.find_element(By.CLASS_NAME, "outage")
        self.assertEqual(len(outages), 4)
        # view the in stock
        instock = self.browser.find_element(By.CLASS_NAME, "instock")
        self.assertEqual(len(instock), 12)

    def _submit_file(self, path):
        # find the file upload
        pdf_upload = self.browser.find_element(By.ID, "pdf_upload")
        submit = self.browser.find_element(By.ID, "submit")
        # upload the file
        pdf_upload.send_keys(path)
        submit.click()
