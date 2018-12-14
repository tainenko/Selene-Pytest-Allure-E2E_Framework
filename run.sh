#!/bin/bash
rm -rf report

mkdir -p report

rm -rf allure-report

py.test testcase/  --alluredir ./result/

allure generate ./result/ -o ./allure-report/ --clean