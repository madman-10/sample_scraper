from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup
import requests
import os

url = "https://www.amazon.in/BringUAll%C2%AE-Display-Connector-Honor-Board/dp/B09DXB371Y/ref=sr_1_2?dib=eyJ2IjoiMSJ9.oOokJHqu2ajhwSFxuguFT-zu9glTplme8spceMIwnHVj9QAUIyivQAWCu-BqA6wkSU18RUQ-wDMW36cvgOacGMy-GE1dURSLcAXMnZgPouKNggauNvtLJqVK4ehaxD__3mwUj1Vr3YkSq96FP-T1h6cT0tQIW2fsf4m45LzNK1ttQv2PtRyOYZCOlvBg4QgacS27iR3bXNzyjwiGM5NsQHjQzJj6G6hasp8Ej25t3Ys.9RdlTM-OQe6iqfKDJN6-iS32txZ6NsW0wvbn_3fgZwQ&dib_tag=se&keywords=40+pin+lcd+connector&qid=1736331080&sr=8-2"

driver = webdriver.Firefox()
web = driver.get(url=url)

sauce = BeautifulSoup(driver.page_source,'html.parser')

p_title = sauce.find('span', attrs={"id":'productTitle'})
title = p_title.string
print(title)

driver.quit()