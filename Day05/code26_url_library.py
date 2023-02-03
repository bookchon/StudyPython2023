# urllib 패키지 불러오기
from urllib.request import Request, urlopen

req = Request('https://wwww.naver.com')
res = urlopen(req)
print(res.status)
# 네이버 호출
# 웹사이트가 제대로 돌아가는지 알려주는 숫자가 200, 찾을수 없으면 404