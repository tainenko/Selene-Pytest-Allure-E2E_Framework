import pytest, os, webbrowser, pathlib

"""
example arguments:
--allure_severities=minor,trivial
--alluredir allure-report
"""
pytest.main()

os.popen("allure generate allure-report -o target")

# for local tests in IDEA only
try:
    webbrowser.open("http://localhost:63343/" + os.path.relpath(os.getcwd(), "..") + "/target/index.html")
except:
    pass

