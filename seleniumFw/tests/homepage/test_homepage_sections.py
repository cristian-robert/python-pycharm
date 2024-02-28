import pytest

from seleniumFw.src.pages.DemoQaHomepage import DemoQaHomepage


@pytest.mark.usefixtures("init_driver")
class TestHomepageSections:

    @pytest.mark.tcid02
    def test_homepage_sections(self):
        DemoQaHomepage(self.driver).check_all_elements_displayed()

    @pytest.mark.tcid03
    def test_homepage_sections_links(self):
        DemoQaHomepage(self.driver).click_element_and_check_link()
