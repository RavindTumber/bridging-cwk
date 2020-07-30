from selenium import webdriver
from django.test import TestCase

import unittest

class FunctionalTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def login(self):
        self.driver.get('http://localhost:8000/accounts/login/')
        self.driver.find_element_by_id('username').send_keys('rst')
        self.driver.find_element_by_id('password').send_keys('rst')
        self.driver.find_element_by_id('loginBtn').click()

    def test_can_view_home_page_and_cv_page(self):
        # Navigate to the homepage
        self.driver.get('http://localhost:8000/')
        # See that the page title is a name
        self.assertIn('Ravind Tumber', self.driver.title)
        # User can navigate to the CV page by clicking on the CV nav-item
        self.driver.find_element_by_css_selector('a:nth-child(3)').click()
        # User is displayed with a CV
        self.assertIn('CV', self.driver.title)

    def test_cv_education(self):
        # Want to test that a user can login and add to the education model
        self.login()
        # User navigates to the CV page
        self.driver.get('http://localhost:8000/cv/')
        
        # User clicks on the 'Add Education' button
        self.driver.find_element_by_id('add_education').click()

        # User can see all of the fields and fill them in
        self.driver.find_element_by_id('id_name').send_keys('Test name')       
        self.driver.find_element_by_id('id_location').send_keys('Test location')
        self.driver.find_element_by_id('id_start_date').send_keys('2011')        
        self.driver.find_element_by_id('id_end_date').send_keys('2020')
        self.driver.find_element_by_id('id_description').send_keys('Test description')
        self.driver.find_element_by_id('save').click()

        # User should be redirected to the CV page where their education details will be displayed
        education = self.driver.find_element_by_id('education_1')

        # User realises that they have entered incorrect data and decide to edit it
        self.driver.find_element_by_id('edit_education_1').click()
        name = self.driver.find_element_by_id('id_name')
        name.clear()
        name.send_keys('Test update')
        self.driver.find_element_by_id('save').click()

if __name__ == '__main__':
    unittest.main()