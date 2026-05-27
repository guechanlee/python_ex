import urllib.request
import datetime
import json

client_id = '8CKf6PDw5oABPgLkMLKW'
client_secret = 'Mrru6P1PyW'

# NAVER에서 데이터 가져오는 녀석
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:                                  # 외부통신할때 꼭 사용 트라이 익셉트
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')
            # print(f'response data: {response.read().decode('utf-8')}')
            # decode란 바이트(byte) 코드를 문자열(string)로 변환하는 것.
            return response.read().decode('utf-8')
    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')
        return None

# NAVER에서 데이터 검색 하는 녀석

def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'   # news.json
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    url = base + node + parameters
    responseDecode =    getRequestUrl(url)

    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
 

    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })
  
def main():
    node = 'news'   # 크롤링 하는 대상
    srcText = input('검색어 입력: ')
    cnt = 0
    jsonResult = []     # 데이터 교환 형식

    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    # print(f'jsonResponse: {jsonResponse}')
    # print(f'jsonResponse total: {jsonResponse['total']}')
    # print(f'jsonResponse total 0: {jsonResponse['items'][0]}')
    # print(f'jsonResponse items 0 title: {jsonResponse['items'][0]['title']}')
    # print(f'jsonResponse items 0 description: {jsonResponse['items'][0]['description']}')

    while  jsonResponse != None and  jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)
            




        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

        print(f'jsonResult: {jsonResult}')

    # 파일로 저장(날씨_naver_news.json)
    with open(f'{srcText}_naver_{node}.json', 'w', encoding='utf8') as f:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)


if __name__ == '__main__':
    main()