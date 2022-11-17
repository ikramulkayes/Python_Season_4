from cgitb import text
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
import pandas as pd
import bangla


os.environ["PATH"] += r"F:\selenium driver"

driver = webdriver.Chrome(ChromeDriverManager().install())
#url = f"https://www.wordproject.org/bibles/ben/{elm}/1.htm#0"
#driver.get("https://www.wordproject.org/bibles/ben/01/1.htm#0")

company_names_xpath1 = "/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[GG]/div/div[1]/div/div" #1 - 30
stock_2017_xpath = "/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[GG]/div/div[3]/div" #1 - 30
stock_2018_xpath = "/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[GG]/div/div[4]/div"
stock_2019_xpath = "/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[GG]/div/div[5]/div"
stock_2020_xpath = "/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[GG]/div/div[6]/div"
stock_2021_xpath = "/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[GG]/div/div[7]/div"


company_lst = []
stock_2017_lst = []
stock_2018_lst = []
stock_2019_lst = []
stock_2020_lst = []
stock_2021_lst = []
driver.get(url)
driver.implicitly_wait(5)
for k in tqdm(range(1,31,1)):
        url = f"https://www.investing.com/pro/DSE:SQURPHARMA/financials/cashflow_statement/"

        company_names_xpath1 = f"/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[{k}]/div/div[1]/div/div" #1 - 30
        stock_2017_xpath = f"/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[{k}]/div/div[3]/div" #1 - 30
        stock_2018_xpath = f"/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[{k}]/div/div[4]/div"
        stock_2019_xpath = f"/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[{k}]/div/div[5]/div"
        stock_2020_xpath = f"/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[{k}]/div/div[6]/div"
        stock_2021_xpath = f"/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div[1]/div[3]/div[{k}]/div/div[7]/div"
        elem = driver.find_elements(By.XPATH,company_names_xpath1)
        for gg in elem:
            company_lst.append(gg.text)

        elem2 = driver.find_elements(By.XPATH,stock_2017_xpath)
        for gg in elem2:
            stock_2017_lst.append(gg.text)

        elem3 = driver.find_elements(By.XPATH,stock_2018_xpath)
        for gg in elem3:
            stock_2018_lst.append(gg.text)

        elem4 = driver.find_elements(By.XPATH,stock_2019_xpath)
        for gg in elem4:
            stock_2019_lst.append(gg.text)

        elem5 = driver.find_elements(By.XPATH,stock_2020_xpath)
        for gg in elem5:
            stock_2020_lst.append(gg.text)

        elem6 = driver.find_elements(By.XPATH,stock_2021_xpath)
        for gg in elem6:
            stock_2021_lst.append(gg.text)

print(stock_2020_lst)
        
        
        