rock='''
    바위
    ****
    ****
'''
scissor='''
    가위
    *     *
     *   *
      * *
       *
'''

paper='''
    보
    *******
    *******
    *******
    *******
'''
import random
app_off="아니오"

game_option = [rock, scissor,paper]
com_choice=random.randint(0,2)
while app_off=="아니오":
    user_choice=int(input("0:바위,1: 가위, 2: 보 >>>"))

    print("나의 선택: ")
    print(game_option[user_choice])

    print("컴퓨터 선택:")
    print(game_option[com_choice])

    if com_choice == user_choice:
        print("비겼습니다.")

    elif user_choice - com_choice == -1 or (user_choice ==2 and com_choice ==0):
        print("이겼습니다.")
    else:
        print("졌습니다.")
    app_off=input("프로그램을 종료하시겠습니까? 네/아니오 >>>")
    print("="*50)

print("프로그램을 종료하겠습니다.")
