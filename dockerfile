From ubuntu:latest
MAINTAINER tony.ko@ehsn.com.tw
#update apt-get and install tools
Run apt-get update
Run apt-get install -y wget curl unzip vim git
#install python3、pip3 and dependent packages
Run apt-get install -y python3-pip
Run pip3 install pytest==3.5
Run pip3 install selene --pre
Run pip3 install pytest-rerunfailures
Run pip3 install pytest-env
Run pip3 install pytest-variables[yaml]
Run pip3 install git+https://github.com/Baidu-AIP/python-sdk.git@master
Run pip3 install PILLOW
#install pyvirtual
Run apt-get install -y xvfb
Run pip3 install pyvirtualdisplay
#install Chrome
Run curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
Run echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
Run apt-get -y update
Run apt-get -y install google-chrome-stable
#Install ChromeDriver
Run wget -N http://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
Run unzip chromedriver_linux64.zip
Run chmod +x chromedriver
Run mv -f chromedriver /usr/local/share/chromedriver
Run ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
Run ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
#Install Allure
Run apt-get install -y openjdk-8-jdk
Run curl -o allure-2.6.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.6.0/allure-2.6.0.tgz && tar -zxvf allure-2.6.0.tgz -C /opt/ && ln -s /opt/allure-2.6.0/bin/allure /usr/bin/allure && allure --version