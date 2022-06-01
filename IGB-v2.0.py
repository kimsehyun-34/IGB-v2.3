from selenium import webdriver
import inspect, os, platform, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

def bot():
    print("++++ Created by 'Kim_sehyun_34' :) ++++")
    print()
    id = int(input('인스타id : '))
    pw = int(input('인스타pw : '))
    tag = input('작업태그 : ')
    cnt = int(input('작업횟수(숫자) : '))
    ff = int(input("작업할 방법 설정(인기피드=0 , 최신피드=1) 입력:"))

    #CDV
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')

    current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))

    if platform.system() == 'Windows':
        driver_path = os.path.join(current_folder, 'chromedriver.exe')
    else:
        driver_path = os.path.join(current_folder, 'chromedriver')

    driver = webdriver.Chrome(driver_path, options=options)
    driver.implicitly_wait(10)

    driver.get('https://www.instagram.com/?hl=ko')
    print('로그인중....')
    time.sleep(5)

    #아이디

    id_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label')
    id_input.click()
    id_input.send_keys(id)

    #PW

    pw_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label')
    pw_input.click()
    pw_input.send_keys(pw)
    time.sleep(1)

    #로그인 버튼

    login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login_btn.click()

    time.sleep(4)

    #확인버튼
    oa_btn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div/div/section/div/button')
    oa_btn.click()
    time.sleep(3)

    #이동
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))
    time.sleep(5)

    #최근피드 선택
    if ff==1:
        first_feed = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]')
        first_feed.click()
        time.sleep(2)
    #인기피드 선택
    if ff==0:
        first_feed = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]')
        first_feed.click()
        time.sleep(2)

    for idx in range(cnt):
        xpath = "//article//section/span/button"
        el_list = driver.find_elements_by_xpath(xpath)
        el_list[0].click()
        time.sleep(1+random.random())
        xpath2 = "//a"
        el_list2 = driver.find_elements_by_xpath(xpath2)
        time.sleep(1)
        #다음
        nextFeed = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div')
        nextFeed.click()
        time.sleep(2+random.random()) 
    print('===========모든 작업 완료==============')
    time.sleep(2)
    driver.quit()

bot()


    
