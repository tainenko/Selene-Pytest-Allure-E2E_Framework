import pytest


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
class TestUserHandling(object):
    def test_login(self):
        pass

    def test_modification(self):
        assert 0

    def test_deletion(self):
        pass


def test_normal():
    pass