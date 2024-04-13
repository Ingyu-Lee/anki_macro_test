import requests 
from bs4 import BeautifulSoup 
import csv
from fake_useragent import UserAgent
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://dictionary.cambridge.org/ko/%EC%82%AC%EC%A0%84/%EC%98%81%EC%96%B4/hypocrisy" 

user_agent = UserAgent()
headers = {'User-Agent': user_agent.random}
res = requests.get(url, headers=headers)



res.raise_for_status() # 정상 200
soup = BeautifulSoup(res.text, "lxml")




# 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한
box = soup.find('div', attrs={"class": "entry-body"})
# 인기 급상승 영역에서 'a'태그 모두 찾아 변수 cartoons에 할당
word = box.find('span', attrs={"class": "hw dhw"})
grammar = box.find('span', attrs={"class": "pos dpos"})
pronunciation = box.find('span', attrs={"class": "ipa dipa lpr-2 lpl-1"})
meaning = box.find('div', attrs={"class": "def ddef_d db"})
# meaning_ = box.find('a', attrs={"class": "def ddef_d db"})
example = box.find('span', attrs={"class": "eg deg"})

print(word.contents)
print(grammar.contents)
print(pronunciation.contents)
print(meaning.contents)
print(example.contents)




# cartoonsBox = soup.find('ol', attrs={"class": "asideBoxRank"}) # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한
# cartoons = cartoonsBox.find_all('a') # 인기 급상승 영역에서 'a'태그 모두 찾아 변수 cartoons에 할당

# i = 1

# # 반복문으로 제목 가져오기(터미널 창 출력 및 엑셀 저장)
# for cartoon in cartoons: 
#   title = cartoon.get("title") 
#   print(f"{str(i)}위: {title}")
#   data = [str(i), title]
#   writer.writerow(data)
#   i += 1


# filename = "고양이 장난감.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(f)

# data = ["결과1", "결과2"] # [] 리스트 자료구조
# writer.writerow(data)

