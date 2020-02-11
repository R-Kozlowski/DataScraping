import os, bs4, time, send2trash
from selenium import webdriver
import __future__


#open browser
url = 'http://bossafx.pl/fx/notowania/pliki-z-danymi/'
browser = webdriver.Chrome()
browser.get(url)
browser.minimize_window()

#delete old data file
send2trash.send2trash('E:\\DOKUMENTY\\PYTHON\\AUTOMAT FOREX\\EURUSD.txt')


plikiPrzedzialow = ['EURUSD_mst_M1.txt', 'EURUSD_mst_M5.txt','EURUSD_mst_M15.txt',
                     'EURUSD_mst_H1.txt','EURUSD_mst_H4.txt','EURUSD_mst_D1.txt',
                     'EURUSD_mst_W1.txt','EURUSD_mst_MN.txt']

# I am starting to download data for the M1 time interval item
interwal = 2



for j in range(len(plikiPrzedzialow)):

    # I mark 10 days back
    for i in range(1,10):
        #choosing date
        data = browser.find_element_by_xpath('//*[@id="dateSelect"]/option[' + str(i) + ']')
        type(data)
        data.click()

    #choosing currency
    waluta = browser.find_element_by_xpath('//*[@id="dane_intr"]/table/tbody/tr[1]/td[2]/select/option[49]')
    type(waluta)
    waluta.click()

    # choosing the time interval from the list
    tick = browser.find_element_by_xpath('//*[@id="time_period"]/option[' + str(interwal) + ']')
    type(tick)
    tick.click()

    # I confirm the txt file download button
    plik = browser.find_element_by_class_name('btnsFx')
    type(plik)
    plik.submit()

    time.sleep(10)

    # I refresh the browser, it shouldn't ask me to download another file
    odświerzam przeglądarkę żeby nie pytała czy pobrać kolejny plik
    browser.refresh()
    
    with open('C:\\Users\\radek\\Downloads\\' + plikiPrzedzialow[j], 'r') as f:
        dane = f.read()
              
    with open('E:\\DOKUMENTY\\PYTHON\\AUTOMAT FOREX\\EURUSD.txt', 'a') as g:
        g.write(dane)

    send2trash.send2trash('C:\\Users\\radek\\Downloads\\' + plikiPrzedzialow[j])
    print('pobrałem plik ' + str(plikiPrzedzialow[j]))
    
    interwal = interwal + 1

browser.close()

