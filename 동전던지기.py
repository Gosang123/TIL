import random

head ="앞면"
fail ="뒷면"

print("동전 던지기 게임")

keep_playing="yes"

while keep_playing=="yes":
    computer = random.randint(0,1)
    choice =  int(input("앞면? 뒷면? 0:앞면, 1:뒷면 \n"))

    print("동전 결과:")
    if computer == 0:
        print(head)
    else:
        print(fail)

    print("나의 선택:")
    if choice ==0:
        print(head)
    else:
        print(fail)

    if computer == choice:
        print("적중")
    else:
        print("땡")
    keep_playing=input("계속 진행하시겠습니까? yes or no >>>").lower()
    print("="*45)

print("동전던지기 게임이 종료되었습니다. 좋은 하루 되세요!")
    

