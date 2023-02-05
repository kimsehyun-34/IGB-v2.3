from selenium import webdriver
import inspect, os, platform, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

def bot():
    print("++++ Created by 'Kim_sehyun_34' :) ++++")
    time.sleep(0.5)
    print()
    print("과도한 사용은 비추천 드립니다.")
    time.sleep(0.5)
    print()
    id = input('인스타id : ')
    pw = input('인스타pw : ')
    tag = input('작업태그 : ')
    cnt = int(input('작업횟수(숫자) : '))
    ff = int(input("작업할 방법 설정(인기피드=0 , 최신피드=1) 입력:"))

    if ff==0:
        print("작업할 피드: 인기피드")
    elif ff==1:
        print("작업할 피드: 최신피드")

    #CDV
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36')

    current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))

    if platform.system() == 'Windows':
        driver_path = os.path.join(current_folder, 'chromedriver.exe')
    else:
        driver_path = os.path.join(current_folder, 'chromedriver')

    driver = webdriver.Chrome(driver_path, options=options)
    driver.implicitly_wait(10)

    #이동
    driver.get('https://www.instagram.com/?hl=ko')
    print('로그인중....')
    time.sleep(3)

    #아이디
    id_input = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label')
    id_input.click()
    id_input.send_keys(insta_id) #아이디 입력

    #패스워드
    pw_input = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label')
    pw_input.click()
    pw_input.send_keys(insta_pw)
    time.sleep(random.uniform(1,3))

    #로그인 버튼 클릭
    login_btn = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]/button')
    login_btn.click()
    time.sleep(10)


    #이동
    time.sleep(random.uniform(2,3))
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))
    time.sleep(5)

    #최근피드 선택
    #게시물 첫번째 피드 선택
    if ff==1:
        first_feed = driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        first_feed.click()
        time.sleep(2)
    #게시물 인기 피드 선택
    if ff==0:
        first_feed = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div/div[1]/div[1]/a/div[1]/div[2]')
        first_feed.click()
        time.sleep(2)

    #좋아요 작업 - 입력한 횟수만큼 반복 작업
    for idx in range(insta_cnt):
        el_list = driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button')
        el_list.click()
        time.sleep(random.uniform(1,2))
        #다음피드
        nextFeed = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button')
        nextFeed.click()
        time.sleep(random.uniform(3,4))
    print('모든 작업 완료')
    driver.quit()

bot()
os.system('pause')
