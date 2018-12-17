# -*- coding: utf-8 -*-
from common_imports import *
from selene.helpers import env

@pytest.mark.incremental
class Testpresetting():
    def test_base_url_string(self):
        assert pytest.config.getoption("platform") =="chrome"
    def test_env_url(self):
        assert env("SELENE_BASE_URL")=="https://www.etmall.com.tw"
    def test_or_func(self):
        a='a' or 'b'
        assert a=='a'
    def test_null_or_func(self):
        a=''or'b'
        assert a=='b'
