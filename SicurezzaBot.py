from selenium import webdriver
import getpass
import time

# richiede username e password
usr = input('Inserisci il tuo username:')
pwd = getpass.getpass("Insersci la tua password:")

# Apre il browser alla pagina di log in del registro
driver = webdriver.***inserisci browser***(executable_path='***inserisci qui percorso driver***')
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
