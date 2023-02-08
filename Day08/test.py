import requests
from urllib.parse import quote, unquote, urlencode # 한글을 URLencode 변환하는 함수
import json

# staitionName 정류소 이름
def getDataPortalSearch(stationName, type):
    api_url = 'https://apis.data.go.kr/6260000/BusanTblBusinfoeqStusService/getTblBusinfoeqStusInfo'
    queryString = "?" + urlencode(
        {
            'servicekey' : 'yR+IgD8xUGGLPLv5yhXB/1N8mrSZZShOsMcBdKjRIHdtT2R1/DttqVn95bmWMWkbyEbcz/J8qqJaoq5sRLTbbw==',
            'pageNumber' : "1",
            'numOfRows' : '10',
            'resultType' : type,
            'stationLoc' : stationName 
        }
    )

    total_url = api_url + queryString
    response = requests.get(total_url, verify=False)
    print(response.text)

getDataPortalSearch('롯데백화점', 'json')