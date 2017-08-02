from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Ma cuisine', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Ma cuisine', header_text)