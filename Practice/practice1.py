# practice1.py
'''
    입력 함수 : input(출력할 내용) : 입력된 값
        -> 기본적으로 입력된 값을 문자열 타입 리턴
        ex) name = input("이름 입력 : ")
'''

# 1. 이름, 성별, 나이, 키 입력받아 출력
#  * 출력 형식 : 이름: xxx, 성별: xx, 나이: xx, 키: xx.xxcm
name = input("이름 : ")
gender = input("성별 : ")
age = input("나이 : ")
height = input("키 : ")
print(f"이름 : {name}, 성별 : {gender}, 나이 : {age}, 키 : {height}cm")
print()

# 2. 두 정수 입력받아 합, 차, 곱, 몫, 나머지 계산 후 출력
n1 = input("첫번째 숫자 : ")
n2 = input("두번째 숫자 : ")
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)
print(n1 % n2)
print()


# 3. 영어 문자열 입력받아 앞 세 글자 출력
fruit = "orange"
print(fruit[0:3])
print()


# 4. 실수 2개 입력받아 합, 차, 곱, 나누기 출력
n1 = 3.14
n2 = 0.5
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)
print(n1 % n2)
print()

# 5. 두 수 입력받아 제곱과 제곱근 계산
n1 = 1241
n2 = 33
print(n1**3)
print(n2**-5)


# 6. 문자열 입력받아 대문자/소문자/글자 수 출력


# 7. 좋아하는 음식 3개 입력받아 리스트처럼 저장 후 출력


print("좋아하는 음식 리스트:" )
print("첫 번째 음식:" )
print("마지막 음식:" )
print("오름차순 정렬 : " )
print("내림차순 정렬 : " )
print()

# 8. 세 개의 숫자 입력받아 합과 평균 계산 후 출력


# 9. 문자열 입력받아 앞 3글자 + 뒤 2글자 합쳐서 출력


# 10. 문자열 입력받아 대문자로 변환 후, 앞 5글자만 출력
