from selenium import webdriver
import inspect, os, platform, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

def bot():
    print("++++ Created by 'Kim_sehyun_34' :) ++++")
    print()
    insta_id = ['kim_sehyun_34']
    insta_pw = ['Do040304*']
    insta_cnt = int(input('작업횟수(숫자) : '))

    #C-DV
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

    #인스타그램 로그인 페이지로 이동
    driver.get('https://www.instagram.com/?hl=ko')
    print('로그인중....')
    time.sleep(5)

    #아이디 입력창을 찾아서 위에서 입력받은 아이디(insta_id)값 입력

    id_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label')
    id_input.click()
    id_input.send_keys(insta_id) #아이디 입력

    #패스워드 입력창을 찾아서 위에서 입력받은 패스워드(insta_pw)값 입력

    pw_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label')
    pw_input.click()
    pw_input.send_keys(insta_pw)
    time.sleep(1)

    #로그인 버튼 클릭

    login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login_btn.click()

    time.sleep(6)

    #작업할 해시태그 검색 결과 페이지로 이동
    driver.get('https://www.instagram.com/explore/tags/풍경/')
    time.sleep(5)

    #게시물 첫번째 피드 선택
    first_feed = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]')
    first_feed.click()
    time.sleep(2)

    #좋아요 작업 - 입력한 횟수만큼 반복 작업
    for idx in range(insta_cnt):
        xpath = "//article//section/span/button"
        el_list = driver.find_elements_by_xpath(xpath)
        el_list[0].click()
        time.sleep(1+random.random())
        xpath2 = "//a"
        el_list2 = driver.find_elements_by_xpath(xpath2)
        time.sleep(1)
        #다음피드
        nextFeed = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]')
        nextFeed.click()
        time.sleep(2+random.random()) 
    print('모든 작업 완료')
    driver.quit()

bot()


    
