from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_can_view_home_page_and_cv_page(self):
        # User navigates to homepage
        self.driver.get('http://localhost:8000/')

        # User notices the page title is Ravind Tumber
        self.assertIn('Ravind Tumber', self.driver.title)

        # User can navigate to the CV page by clicking on the CV nav-item
        self.driver.find_element_by_css_selector('a:nth-child(3)').click()
        # User is displayed with a CV
        self.assertIn('CV', self.driver.title)

if __name__ == '__main__':
    unittest.main()