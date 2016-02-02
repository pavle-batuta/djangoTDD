from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(unittest.TestCase):
	"""Test case for a new visitor"""
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Check out the homepage
		self.browser.get('http://localhost:8000')

		# Page title and header should mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do'. header_text)

		# The user is invited to enter a to-do item immediately
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Enter a to-do item'
		)

		# The user types in 'Buy peacock feathers' for some reason that I cannot fathom
		inputbox.send_keys('Buy peacock feathers')

		# The user hits enter.
		inputbox.send_keys(Keys.ENTER)
		
		# The page updates
		# Page now lists "1: Buy peacock feathers" as an item in a to-do list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_id('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)

		# There is still a text box for entering another item.
		# The user enters: 'Use peacock feathers to make a fly'
		inputbox.send_keys('Use peacock feathers to make a fly')

		# The user hits enter
		inputbox.send_keys(Keys.ENTER)

		# The page updates again.
		# Both items are present on the list.
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)
		self.assertTrue(
			any(row.text == '2: Use peacock feathers to make a fly' for row in rows)
		)

		self.fail('Finish the test!')

		# The site has generated a unique URL for the user.
		#
		# The user goes to the great user place in the sky. Browser quits.
		#


if __name__ == '__main__':
	unittest.main()