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

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		test_strings = [
			'Buy peacock feathers',
			'Use peacock feathers to make a fly',
		]
		correct_strings = [
			'1: Buy peacock feathers',
			'2: Use peacock feathers to make a fly',
		]
		print(test_strings[0])
		# Check out the homepage
		self.browser.get('http://localhost:8000')

		# Page title and header should mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# The user is invited to enter a to-do item immediately
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Enter a to-do item'
		)

		# The user types in 'Buy peacock feathers' for some reason that I cannot fathom
		inputbox.send_keys(test_strings[0])
		# The user hits enter.
		inputbox.send_keys(Keys.ENTER)
		
		# The page updates
		# Page now lists "1: Buy peacock feathers" as an item in a to-do list
		self.check_for_row_in_list_table(correct_strings[0])


		# There is still a text box for entering another item.
		# The user enters: 'Use peacock feathers to make a fly'
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys(test_strings[1])

		# The user hits enter
		inputbox.send_keys(Keys.ENTER)

		# The page updates again.
		# Both items are present on the list.
		self.check_for_row_in_list_table(correct_strings[1])

		self.fail('Finish the test!')

		# The site has generated a unique URL for the user.
		#
		# The user goes to the great user place in the sky. Browser quits.
		#


if __name__ == '__main__':
	unittest.main()