# 네이버와 인터넷 통신을 하기 위한 기본 배달원 도구를 가져와.
import urllib.request

# 날짜와 시간을 계산하고 이쁘게 바꾸는 시계 도구를 가져와.
import datetime

# 복잡한 글자 데이터를 장부 형태로 다루는 양식 도구를 가져와.
import json

# 네이버 문을 열기 위한 내 전용 출입증 아이디야.
client_id = '8CKf6PDw5oABPgLkMLKW'

# 아이디가 진짜인지 증명하는 내 전용 비밀번호(암호)야.
client_secret = 'Mrru6P1PyW'

# 인터넷 주소를 받아서 네이버에 실제로 다녀오는 심부름꾼 함수야.
def getRequestUrl(url):

    # 주소와 신분증을 함께 담을 인터넷 편지봉투를 만들어.
    req = urllib.request.Request(url)

    # 편지봉투에 내 네이버 아이디 스티커를 딱 딱 붙여.
    req.add_header('X-Naver-Client-Id', client_id)

    # 편지봉투에 내 네이버 비밀번호 스티커도 같이 붙여.
    req.add_header('X-Naver-Client-Secret', client_secret)

    # 인터넷이 끊겨서 프로그램이 멈추는 걸 막는 안전장치를 켜.
    try:

        # 신분증을 붙인 봉투를 들고 네이버 서버 문을 똑똑 두드려.
        response = urllib.request.urlopen(req)

        # 네이버가 '연걸 성공(200)' 신호를 보냈는지 확인해.
        if response.getcode() == 200:

            # 잘 가동되고 있다고 검은 창에 현재 시간과 성공 메세지를 찍어.
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')

            # 컴퓨터 암호 언어로 된 데이터를 한글 문자열로 번역해서 돌려줘.
            return response.read().decode('utf-8')
        
    # 에러가 나면 프로그램이 꺼지지 않고 이쪽 방으로 튕겨와.
    except Exception as e:

        # 에러가 난 시간과 구체적인 원인을 화면에 띄워줘.
        print(f'[{datetime.datetime.now()}] Error: {e}')

        # 데이터 수집에 실패했으니 아무것도 없다고 'None'을 반환해.
        return None
    
# 검색어와 개수를 조합해서 네이버 전용 주문서 주소를 조립하는 함수야.
def getNaverSearch(node, srcText, start, display):

    # 네이버 검색창의 기본 인터넷 주소 기본 뼈대야.
    base = 'https://openapi.naver.com/v1/search'

    # 주소창에 '뉴스 결과'를 달라고 세부 경로('.json')를 붙여.
    node = f'/{node}.json'

    # 한글 검색어가 깨지지 않게 변환하고 몇 개를 가져올지 옵션을 조립해.
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    # 기본주소, 뉴스방 경로, 세부 옵션을 다 합쳐서 완벽한 인터넷 주소를 만들어.
    url = base + node + parameters

    # 방금 만든 주소를 들고 1단계 통신 심부름꾼에게 다녀오라고 시켜.
    responseDecode = getRequestUrl(url)

    # 심부름꾼이 빈손(None)으로 돌아왔는지 체크해.
    if responseDecode == None:

        # 실패했으니 다음 일을 못 하게 텅 빈값(None)을 돌려주고 끝내.
        return None
    
    else:

        # 기나긴 글자 데이터를 파이썬이 다루기 쉬운 '딕셔너리(장부)' 구조로 바꿔서 돌려줘.
        return json.load(responseDecode)
    
# 지저분한 데이터에서 제목, 링크, 날짜만 이쁘게 깍아내는 요정 함수야.
def getPostData(post, jsonResult, cnt):

    # 복잡한 덩어리에서 딱 '뉴스 제목'만 골라내 변소에 담아.
    title = post['title']

    # 뉴스 본문을 짧게 줄여놓은 '요약 내용'만 골라내 변수에 담아.
    description = post['description']

    # 뉴스를 처음 작성한 신문사의 '원본 링크' 주소를 골라내 담아.
    org_link = post['originallink']

    # 포털 사이트에서 볼 수 있는 '네이버 뉴스 링크' 주소를 골라내 담아.
    link = post['link']

    # 네이버가 준 영국식 날짜 글자를 컴퓨터 시계가 읽을 수 있게 번역해.
    pDate = datetime.datetime.strftime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')

    # 컴퓨터용 날짜를 우리가 읽기 편한 '년-월-일 시:분:초' 양식으로 리모델링해.
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    # 깔끔하게 가공한 뉴스 한 건을 최종 보물상자 리스트 가방에 쏙 집어넣어.
    jsonResult.append({
        'cnt': cnt,                    # 몇 번째 뉴스인지 매긴 번호표
        'title': title,                # 이쁘게 깎은 제목
        'description': description,    # 요약 설명
        'org_link': org_link,          # 원본 주소
        'link': link,                  # 네이버 주소
        'pDate': pDate                 # 리모델링한 한국실 날짜
    })


def main():
    
    # 수집 카테고리를 'news(뉴스)'로 정해서 표지판 변수에 둬.
    node = 'news'

    # 사용자에게 어떤 단어를 검색할지 키보드로 직접 입력받아.
    srcText = input('검색어 입력: ')

    # 수집한 뉴스 개수를 세어줄 카운터 숫자를 0으로 세팅해.
    cnt = 0

    # 뉴스가 쏟아져 들어올 텅 빈 최종 보물상자 바구니를 준비해.
    jsonResult = []

    # 반복문을 돌기 전에, 마중물 역할로 '1등부터 100개' 뉴스를 먼저 주문해 와.
    jsonResponse = getNaverSearch(node, srcText, 1, 100)

    # 데이터가 정상적으로 들어왔고 결과가 남아있는 동안 무한 반복을 가동해.
    while jsonResponse != None and jsonResponse['display'] != 0:

        # 네이버가 던져준 뉴스 100개 보따리에서 뉴스 1개씩 차례대로 꺼내서 돌려.
        for post in jsonResponse['items']:

            # 뉴스를 하나씩 꺼낼 때마다 번호표 숫자를 1씩 늘려줘.
            cnt += 1

            # 꺼낸 뉴스 1개를 3단계 요정에게 보내서 이쁘게 깎아 보물상자에 담아라 시켜.
            getPostData(post, jsonResult, cnt)

        # 100개를 다 담았으니 다음 페이지 (101등 뉴스)로 주소를 바꿔서 네이버를 다시 찔러.
        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

        print(f'jsonResult: {jsonResult}')

    # 더 이상 뉴스가 없으면 가방 통째로 내 하드디스크에 보관할 저장 파일을 만들어.
    with open(f'{srcText}_naver{node}.json', 'w', encoding='utf8') as f:

        # 가방 안의 파이썬 데이터를 메모장에 적을 수 있게 이쁜 텍스트 글로 변환해서 파일에 쾅 박아버려.
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        f.write(jsonFile)

# 이 파일이 주인공으로 직접 실행된 게 맞는지 확인하는 파이썬 전용 규칙이야.
if __name__ == '__main__':
    
    # 진짜 시동 스위치인 main() 함수를 호출해서 위 모든
    main()