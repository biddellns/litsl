fromseleniumimportwebdriver
importunittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_display_home_page(self):
        self.browser.get('http://localhost:8000')

        # Edennil checks out the cool website for the LiTStarleague
        self.assertIn('LiTStarleague', self.browser.title)

        # Edinnil checks to see the list of players in LITSL.
        player_list = self.find_elements_by_id("player_list")
        assertTrue(player_list.size > 0)
        

    if __name__ == '__main__':
        unittest.main(warnings='ignore')


