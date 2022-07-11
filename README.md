# FURY.312
# 앙용하지 마세용 학습용으로 만든겁니다~ 잘못쓰면 인스타 밴먹어용~
1. chromedriver.exe 업데이트 (https://chromedriver.chromium.org/downloads)
2. IGB-v2.1.py 실행
----
- xpath 활용.
- py selenium 활용.
----
# V2.2
- 피드선택 xpath 변경, 편의기능 
 1. 최근피드 : (//*[@id="react-root"]/div/div/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]) -> ('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]')

 2. 인기피드 : ('//*[@id="react-root"]/div/div/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]') -> ('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')

 3. 다음피드 : (/html/body/div[6]/div[2]/div/div) -> ('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]')

----
V2.1 
- 로그인 이후 정보 확인 메시지 종료 기능 추가
- 크롬드라이버 업데이트, 코드 수정 (다음피드 XPath)
/html/body/div[6]/div[2]/div/div -> /html/body/div[6]/div[2]/div/div[2]
----
V2.0 
- 인기 또는 최신피드 선택가능 
- 사용자 편의기능 추가
----
V1.1 
- ChromeDriver 97.0.4692.71 버전 업데이트
- 다음피드 XPath 오류코드 수정. {처음작동시 오류발생}
/html/body/div[6]/div[1]/div/div/div[2] -> /html/body/div[6]/div[2]/div/div[2]
----
V1.0 
- ChromeDriver 96.0.4664.45 버전 기본 업로드


