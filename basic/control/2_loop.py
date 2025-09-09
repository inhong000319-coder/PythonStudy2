# 2_loop.py
import random
# 반복문
'''
    * 기본 구조

        for 변수명 in 반복가능한 객체:      #반복 가능한 객체 : 리스트, 튜플, 세트, 딕셔너리, 문자열
            반복할 내용

    * range 함수
        range(stop) : 0 부터 stop-1 씩 증가하는 숫자들을 생성(시컨스)
        range(start, stop) : start부터 stop-1까지 1씩 증가하는 시퀀스 생성
        range(stat, stop, step): stat부터 stop-1까지 step씩 증사하는 시퀀수 생성

        # * 1 ~ 10까지 출력


'''
'''
# * 1 ~ 10 까지 출력
for i in range(1, 11):
    print(i, end=" ")
print()

# * 리스트에 저장되어 있는 요소들을 출력
colors = ["빨간색", "검은색", "흰색"]
for c in colors:
print(colors)
'''

# while 문
'''
    * 기본 구조

        while 조건식:
            반복할 내용
'''
# * while 문을 사용하여 1 ~ 10 출력
'''
n = 1
while n <= 10:
    print(n, ned=" ")
    # n++ # 오류 발생
    # 

    # *while 문을 사용하여
    #      사용자 입력이 exit인 경우 종료
    #           그렇지 않으면 입력값 출력
'''
'''
while True:
    data = input("단어 입력하세요 (exit을 입력할 경우 종료): ")

    if data.lower() == 'exit':  # 파이썬에서는 문자열의 값 비교 가능
        print("프로그램 종료")
        break
    print(f"입력된 값 : {data}")

    # * 업앤다운 게임
    # 1 ~ 100 사이의 숫자 맞추기 게임
'''
'''
    ex) 정답 = 55
        사용자 : 20 up
        사용자 : 60 down
        ...
        사용자 : 55 정답
'''

print("*===== Up & Down ======*")
    
answer = random.randint(1, 100)

while True:
    
    #num = int(input("숫자를 입력하세요 : "))
    num = input("입력 : ")

    # isdigit() : 값이 정수로 되어있는지 아닌지 판별
    if not num.isdigit():
        print("숫자만 입력해주세요")
        continue

    num = int(num)

    if num == answer:
        print("정답입니다.")
        break
    elif num < answer:
        print("Up!")
    else:               # user < answer
        print("Down!")
    
    