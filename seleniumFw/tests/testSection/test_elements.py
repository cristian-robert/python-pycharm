import pytest

from seleniumFw.src.pages.DemoQaElementsPage import DemoQaElementsPage
from seleniumFw.src.pages.DemoQaHomepage import DemoQaHomepage


@pytest.mark.usefixtures("init_driver")
class TestHomepageSections:

    @pytest.mark.tcid04
    def test_textbox_section(self):
        DemoQaHomepage(self.driver).go_to_elements_page()
        DemoQaElementsPage(self.driver).test_text_box()
        assert 1 == 2

    @pytest.mark.tcid05
    def test_checkbox_section(self):
        DemoQaHomepage(self.driver).go_to_elements_page()
        DemoQaElementsPage(self.driver).test_check_box()

