# practice5.py

'''
미니게임 모듈 만들기


[게임 종류]
1. 숫자 맞추기 게임
   - number_game.py 모듈
   - 함수명: play_number_game()
   - 기능:
       * 1~10 사이 랜덤 숫자를 생성
       * 사용자 입력을 받아 숫자를 맞추면 "정답!" 출력
       * 틀리면 "틀렸습니다. 정답은 X였습니다." 출력

       #
2. 가위바위보 게임
   - rps_game.py 모듈
   - 함수명: play_rps_game()
   - 기능:
       * 사용자 입력: "가위", "바위", "보"
       * 컴퓨터 랜덤 선택
       * 결과 출력 (이김, 짐, 비김)

3. 주사위 게임
   - dice_game.py 모듈
   - 함수명: play_dice_game()
   - 기능:
       * 사용자와 컴퓨터 각각 1~6 사이 랜덤 수 생성
       * 주사위 값 비교 후 결과 출력 (이김, 짐, 비김)

[main.py]
- 사용자에게 게임 선택 메뉴 표시
- 선택한 게임 모듈의 함수를 실행
- 0 입력 시 종료
- 잘못된 입력 처리


[패키지 구조]
mini_games/
    __init__.py
    number_game.py
    rps_game.py
    dice_game.py
main.py

'''