from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(LiveServerTestCase):
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
		user_1_test_strings = [
			'Buy peacock feathers',
			'Use peacock feathers to make a fly',
		]
		user_2_test_strings = [
			'Buy milk',
		]
		user1_correct_strings = [
			'1: Buy peacock feathers',
			'2: Use peacock feathers to make a fly',
		]
		user2_correct_strings = [
			'1: Buy milk',
		]

		print(user_1_test_strings[0])
		# Check out the homepage
		self.browser.get(self.live_server_url)

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
		inputbox.send_keys(user_1_test_strings[0])
		# The user hits enter.
		inputbox.send_keys(Keys.ENTER)

		# Check if the list URL is valid!
		user1_url = self.browser.current_url
		self.assertRegex(user1_url, '/lists/.+')
		
		# The page updates
		# Page now lists "1: Buy peacock feathers" as an item in a to-do list
		self.check_for_row_in_list_table(user1_correct_strings[0])


		# There is still a text box for entering another item.
		# The user enters: 'Use peacock feathers to make a fly'
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys(user_1_test_strings[1])

		# The user hits enter
		inputbox.send_keys(Keys.ENTER)

		# The page updates again.
		# Both items are present on the list.
		self.check_for_row_in_list_table(user1_correct_strings[1])

		# The site has generated a unique URL for the user.
		# The user goes to the great userspace in the sky.

		## Make sure no information from the previous user is corrupting the
		# new users experience (cookies etc) ##
		self.browser.quit()
		slef.browser = webdriver.Firefox()

		# A new user is spawned!
		# User visits the homepage
		# Check if there is not garbage left behind by the previous user.
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn(user_1_test_strings[0], page_text)
		self.assertNotIn(user_1_test_strings[1], page_text)

		# The user#2 is a boring man named Ted. Ted want's to buy milk because
		# he has nothing better to do. Get a hold of yourself Ted!
		inputbox.send_keys(user_2_test_strings[0])
		# The user hits enter.
		inputbox.send_keys(Keys.ENTER)

		# User#2 gets his own URL.
		user2_url = self.browser.current_url
		self.assertRegex(user2_url, '/lists/.+')
		self.assertNotEqual(user1_url, user2_url)

		# Check if there is no trace of the previous list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn(user_1_test_strings[0], page_text)
		self.assertNotIn(user_1_test_strings[1], page_text)

		# Check if we have User#2's stuff
		self.check_for_row_in_list_table(user2_correct_strings[0])

		# Ted snaps, quits his job and moves to the Peruvian jungle.
		# He is happy there.
		# The milks stays unbought.
		# All is well.

