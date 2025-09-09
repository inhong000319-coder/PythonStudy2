# practice4.py

# [1] 은행 계좌 클래스
#     BankAccount 클래스 정의
#     - 속성 : 계좌번호(account_number), 잔액(balance)
#     - 메소드 : 
#       * deposit(amount) : 입금. 잔액을 증가시킨다.
#       * withdraw(amount): 출금. 잔액을 감소시킨다. 
#                           단, 잔액이 부족하면 "잔액이 부족합니다." 출력한다.
#       * show_balance()  : 잔액 확인. 현재 잔액을 출력한다.


kim_bank = BankAccount("111-222", 1000)
kim_bank.deposit(500)           # 출력예) 500원 입금 완료. 현재 잔액: 1500원
kim_bank.withdraw(2000)         # 출력예) 잔액이 부족합니다.
kim_bank.show_balance()         # 출력예) 계좌 111-222 잔액: 1500원
# =====================================================================
# [2] 온라인 쇼핑몰 클래스
#     Product 클래스
#     - 속성 : 상품명(name), 가격(price), 재고(__stock)
#     - 메소드 :
#       * reduce_stock(quantity) : 구매 시 재고 감소
#       * add_stock(quantity) : 재고 추가
#       * get_stock() : 현재 재고 조회
#       * __str__() : 상품 정보 문자열로 반환

#     Cart 클래스
#     - 속성 : 담은 상품 목록(items) -> (Product 객체, 수량) 형태로 저장
#     - 메소드 :
#       * add_product(product, quantity) : 장바구니에 상품 추가
#       * remove_product(product_name) : 장바구니에서 상품 제거
#       * show_cart() : 장바구니 내역 출력
#       * total_price() : 장바구니 총액 계산

p1 = Product("노트북", 1200000, 5)
p2 = Product("마우스", 30000, 10)

cart = Cart()

cart.add_product(p1, 1)         # 출력예) 노트북 1개 장바구니에 추가
cart.add_product(p2, 2)         # 출력예) 마우스 2개 장바구니에 추가
cart.show_cart()                
'''
출력예)
장바구니 내역:
- 노트북 (1개) : 1200000원
- 마우스 (2개) : 60000원
총 금액: 1260000원
'''

cart.remove_product("마우스")   # 출력예) 마우스 장바구니에서 제거
cart.show_cart()
'''
출력예)
장바구니 내역:
- 노트북 (1개) : 1200000원
'''