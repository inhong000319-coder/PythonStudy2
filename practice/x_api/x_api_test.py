# * 사전 작업
#   X개발자 플랫폼에 회원 가입하여 API 키 발급

# * ============ 주의사항! 아래 정보는 github, cloud에 올리지 말 것!! ======================= *

# CONSUMER API KEY
CONSUMER_KEY='UDzcwyjd4dFgA9de02oAGQbCm'
CONSUMER_SECRET='9BZMM7j2THrplONSLUrXDcwmHvn17ZyG4ePOcqhIrfOVmtlEJO'

# ACCESS TOKEN
ACCESS_TOKEN='1993489777489068033-XNpYzBd0D5XlAMAlW3j9DaxQJqlyru'
ACCESS_SECRET='0Mk3ZSCHGierUBSn9YnES6BwlOemwEn9ZKCzkWW3dJ8tX'

# BEARER TOKEN
BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAIaK5gEAAAAA5y%2BiBUa8b4o7mljF6D2Ity44P1s%3DiBCXGr4YgWTZDXBFPLiSRWrh1JEEAWBNaEBjzlNC40OYFf5Ebg'
# * ============================================================================================ *

# * tweepy 라이브러리(모듈)
#   > pip install tweepy
import tweepy

# Client 객체 -> 기능(API)을 함수호출 방식으로 연동
def get_client_v1():
  return tweepy.Client(consumer_key=CONSUMER_KEY,
              consumer_secret=CONSUMER_SECRET,
              access_token=ACCESS_TOKEN,
              access_token_secret=ACCESS_SECRET)

# * 인증 계정 정보 조회 : get_me()
def get_user(client):
  response = client.get_me()
  print(response)
  username = response.data['username']
  print(f'인증 성공 : 계정명 - {username}')

# * 트윗 (작성) : create_tweet()
def create_tweet(client):
  response = client.create_tweet(text='집 마렵다.....')
  print(response)

'''
# 계정 조회, 트윗 작성 테스트
# client = get_client_v1()
# create_tweet(client)
# get_user(client)
'''
# ========================================================================

# Client 객체 생성 (Bearer token)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# * 최근 트윗(post) 검색 => search_recent_tweets()
keyword = '오늘은..'
option = ' -is:retweet lang:ko'     # 리트윗 제외, 한국어
response = client.search_recent_tweets(query='keyword+option', max_results=10)
print(response)
