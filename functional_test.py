from selenium import webdriver
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
		self.fail('Finish the test!')

		# The user is invited to enter a to-do item immediately
		# The user types in 'Buy peacock feathers' for some reason that I cannot fathom
		# The user hits enter.
		# The page updates
		# Page now lists "1: Buy peacock feathers" as an item in a to-do list
		# There is still a text box for entering another item.
		# The user enters: 'Use peacock feathers to make a fly'
		#
		# The page updates again.
		# Both items are present on the list.
		#
		# The site has generated a unique URL for the user.
		#
		# The user goes to the great user place in the sky. Browser quits.
		#


if __name__ == '__main__':
	unittest.main()