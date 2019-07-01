from selenium import webdriver
import getpass
import time

# richiede username e password
usr = input('Inserisci il tuo username:')
pwd = getpass.getpass("Insersci la tua password:")

# Apre il browser alla pagina di log in del registro
driver = webdriver.Chrome(executable_path= 'C:\Program Files\chromedriver\chromedriver.exe')
driver.get('https://web.spaggiari.eu/col/app/default/corso.php?corso=sicstu&p=set&view=pre')

# inserisce lo username
usr_box = driver.find_element_by_id('login')
usr_box.send_keys(usr)

# inserisce la password
pwd_box = driver.find_element_by_id('password')
pwd_box.send_keys(pwd)

# clicca il pulsnte
login_button = driver.find_element_by_css_selector(".check-auth")
login_button.click()

# apre i video e lascia la pagina aperta a una durata superiore a quella del video, dove serve risponde alle domande
time.sleep(5)
url_video = 'https://web.spaggiari.eu/col/app/default/corso.php?view=vid&video=01.'
lezione_1 = ['01', '02', '03']
for n in lezione_1:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(400)
driver.get('https://web.spaggiari.eu/col/app/default/corso.php?view=tst&video=01.03')
time.sleep(5)
driver.find_element_by_css_selector('input.cb-test:nth-child(5)').click()

lezione_8 = ['04', '05']
for n in lezione_8:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(400)

lezione_2 = ['06']
for n in lezione_2:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(600)

driver.get('https://web.spaggiari.eu/col/app/default/corso.php?view=tst&video=01.06')
time.sleep(5)
driver.find_element_by_css_selector('input.cb-test:nth-child(8))').click()

lezione_3 = ['07', '09', '10']
for n in lezione_3:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(400)

driver.get('https://web.spaggiari.eu/col/app/default/corso.php?view=tst&video=01.10')
time.sleep(5)
driver.find_element_by_css_selector('input.cb-test:nth-child(5)').click()

lezione_9 = [ '11', '12.01', '12.02', '12.03', '13', '14']
for n in lezione_9:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(400)

driver.get('https://web.spaggiari.eu/col/app/default/corso.php?view=tst&video=01.14')
time.sleep(5)
driver.find_element_by_css_selector('input.cb-test:nth-child(11)').click()

lezione_10 = ['15', '16', '17']
for n in lezione_9:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(400)

lezione_4 = ['18']
for n in lezione_4:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(1000)

driver.get('https://web.spaggiari.eu/col/app/default/corso.php?view=tst&video=01.18')
time.sleep(5)
driver.find_element_by_css_selector('input.cb-test:nth-child(8)').click()

lezione_5 = ['19']
for n in lezione_5:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(160)

lezione_6 = ['20', '21', '22', '23', '24']
for n in lezione_6:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(630)

lezione_7 = ['25']
for n in lezione_6:
    driver.get(url_video + n)
    time.sleep(5)
    play_icon = driver.find_element_by_css_selector('html')
    play_icon.click()
    time.sleep(200)

# raggiunge il numero minimo di presenza online
time.sleep(300)

# risponde al test finale
time.sleep(15)
driver.get('https://web.spaggiari.eu/col/app/default/corso.php?view=tsf')

driver.find_element_by_css_selector('div.test-item:nth-child(5) > div:nth-child(1) > div:nth-child(2) > input:nth-child(5)')
driver.find_element_by_css_selector('div.test-item:nth-child(6) > div:nth-child(1) > div:nth-child(2) > input:nth-child(5)')
driver.find_element_by_css_selector('div.test-item:nth-child(7) > div:nth-child(1) > div:nth-child(2) > input:nth-child(11)')
driver.find_element_by_css_selector('div.test-item:nth-child(8) > div:nth-child(1) > div:nth-child(2) > input:nth-child(5)')
driver.find_element_by_css_selector('div.test-item:nth-child(9) > div:nth-child(1) > div:nth-child(2) > input:nth-child(11)')
driver.find_element_by_css_selector('div.test-item:nth-child(10) > div:nth-child(1) > div:nth-child(2) > input:nth-child(5)')
driver.find_element_by_css_selector('div.test-item:nth-child(11) > div:nth-child(1) > div:nth-child(2) > input:nth-child(11)')
driver.find_element_by_css_selector('div.test-item:nth-child(12) > div:nth-child(1) > div:nth-child(2) > input:nth-child(11)')
driver.find_element_by_css_selector('div.test-item:nth-child(13) > div:nth-child(1) > div:nth-child(2) > input:nth-child(8))')
driver.find_element_by_css_selector('div.test-item:nth-child(14) > div:nth-child(1) > div:nth-child(2) > input:nth-child(8)')

print('Hai finito congratulazioni :)')
