import pytest
from flow.bussiness_flow import LoginFlow


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        login_flow = LoginFlow(self.driver)
        login_flow.login_with_account('demo', 'mode')
        assert 'Welcome Page' in self.driver.title





