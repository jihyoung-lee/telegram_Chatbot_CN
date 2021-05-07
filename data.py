import urllib.request
from bs4 import BeautifulSoup
import datetime

# 현재시간
now = datetime.datetime.now()
nowdate = now.strftime('%Y%m%d')  # 시간형식 변경
nowdate2 = now.strftime('%Y年 %m月 %d日')
# api 요청

ServiceKey = 'servicekey'
pageNo = 1
numOfRows = 1
startCreateDt = int(nowdate)
endCreateDt = int(nowdate)  # 오늘시간으로 자동업데이트

url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={ServiceKey}&pageNo={pageNo}&numOfRows={numOfRows}&startCreateDt={startCreateDt}&endCreateDt={endCreateDt} '
r = urllib.request.urlopen(url)
result = r.read()
soup = BeautifulSoup(result, 'lxml-xml')

# 리스트


gubun_list = ["检疫", "济州", "庆南", "庆北", "全南", "全北", "忠北", "江原", "京畿", "世宗", "蔚山", "光州", "仁川", "大邱", "釜山", "首尔", "合计"]
defCnt_list = []  # 누적 확진자
incDec_list = []  # 신규 확진자

# column


defCnt = soup.find_all('defCnt')
incDec = soup.find_all('incDec')

for items in defCnt:
    defCnt_list.append(items.text)

for items in incDec:
    incDec_list.append(items.text)
