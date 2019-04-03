# “类”所在文件

# coding: utf-8
import requests
import dctnry
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_mainwindow import Ui_MainWindow

class mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        self.date = 0

    # 根据按钮的状态，对date赋值
    def btnstate(self):

        if self.radioButton_tod.isChecked():
                self.date = 1
        elif self.radioButton_tom.isChecked():
                self.date = 2
        else:
                self.date = 3

    # 对city赋值，并跳转到文本输出函数
    def click_city(self):
        self.city = self.input_city.text()
        correct1, correct2 = '', ''
        # 对非法输出进行报错
        if self.city not in dctnry.city:
            self.city = '合肥'
            correct1 = '请输入正确城市名！当前默认城市： 合肥\n'
        self.citystr = dctnry.city.get(self.city)
        if self.date == 0:
            self.date = 1
            correct2 = '请确认已勾选日期！当前默认日期： 今天'
        correct = '  ' + correct1 + '  ' + correct2 + '\n'
        self.click_output(correct)

    # 文本输出函数
    def click_output(self, correct):
        txt = self.weather_txt(correct)
        self.output_text.setText(txt)

    # 查询函数
    def weather_txt(self, correct):
        Header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        url = 'http://www.weather.com.cn/weather/%s.shtml' % self.citystr
        page_html = requests.get(url, headers=Header)
        soup = BeautifulSoup(page_html.content, features='html.parser', from_encoding='UTF-8')
        data = self.condition_date(soup)
        return correct + data[0] + data[1] + data[2] + '\n' + data[3]

    # 返回具体城市日期天气信息
    def condition_date(self, soup):
        weather = soup.find('ul', 't clearfix')
        w_tag = weather.findAll('li')
        n = 1
        # 通过循环找到指定日期的信息
        for tag in w_tag:
            if n > self.date:
                break
            n += 1
            day = tag.find('h1').text
            temp = tag.find('p', 'tem').text
            aq = tag.find('p', 'wea').text
            wind = tag.find('p', 'win').find('i').text
        return day, temp, aq, wind

