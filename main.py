from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pyautogui as pg
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\LENOVO\\AppData\\Local\\Google\\Chrome\\User Data\\Default') # change the LENOVO with your user name 

PATH = "C:\Program Files (x86)\chromedriver.exe" # enter your chrome driver path

driver = webdriver.Chrome(PATH, options=options)
# driver.implicitly_wait(16)

driver.get("https://web.whatsapp.com/")

time.sleep(12)

meets_joined = [] # making this list to get the links of the joined lectures, so the program doesn't joins any of them again for a particular day


def link_checker(): # this function checks for the most recent link in the whatsapp
    user = driver.find_element_by_xpath('//span[@title="School Group"]') #change School Group with the user name or the name of your desired whatsapp group

    user.click()

    meet_links_list = driver.find_elements_by_partial_link_text("https://meet.google.com/")

    meet_link = meet_links_list[-1] # this slices the list of links and finds the most recent one

    if str(meet_link.text) in meets_joined: # made this if/else logic so if the link exists in joined lists it wouldnt join rather run function again after 2 min to check a new link
        time.sleep(80) 
        link_checker()
    else:
        meets_joined.append(meet_link.text)  # if a new link has came it would join the meet
        meet_link.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(10)
        switch_off_mic_cam()


def switch_off_mic_cam():  # this function turns off the cam and mic
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    time.sleep(3)
    join_meet()


def join_meet():  # this function joins the meeting and sends the greetings, as well as hangs up meeting after a specific time
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()

    time.sleep(3)

    # driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span').click()

    try:
        chat_btn = WebDriverWait(driver, 600).until(ec.presence_of_element_located((By.XPATH, '//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span'))) # the program will wait here till the host allows us to join meeting for maximum of 10 mins otherwise we will head back to whatsapp checking for new link
        chat_btn.click()

        time.sleep(2)

        if int(datetime.now().hour) < 12:
            pg.typewrite('Good Morning\n')
        if int(datetime.now().hour) > 12 and int(datetime.now().hour) < 18:
            pg.typewrite('Good Afternoon\n')
        else:
            pg.typewrite('Good Evening\n')

        time.sleep(20) # change the time with your total class time

        pg.typewrite('Thank You\n')

        time.sleep(4)

        driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]').click()

        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

        pg.hotkey('ctrl', 'w')

        driver.switch_to.window(driver.window_handles[0])

        link_checker()
    except:
        pg.hotkey('ctrl', 'w')

        driver.switch_to.window(driver.window_handles[0])

        link_checker()


link_checker()
switch_off_mic_cam()  # called the functions here according to a correct order
join_meet()














