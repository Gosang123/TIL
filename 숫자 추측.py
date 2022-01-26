import random

card_image="""
 @@@@@@@@@@@@@@@@@@@@@@
 @@       ***        @@
 @@      *   **      @@
 @@          *       @@
 @@         *        @@
 @@        *         @@
 @@        *         @@
 @@                  @@
 @@        *         @@
 @@@@@@@@@@@@@@@@@@@@@@
"""

print(card_image)
print("카드 뒷면에 1~20 사이의 수가 있습니다. 어떤 숫자가 숨겨져 있을까요?")

card_num=random.randint(1,20)
user_guess=0
attempt=0

while card_num !=user_guess:
    user_guess=int(input("카드 뒷면의 수를 추측해 보세요~! >>>"))
    attempt +=1

    if card_num > user_guess:
        print("더 큰 수입니다.")
    elif card_num <user_guess:
        print("더 작은 수입니다.")

    print()
    
print(f"정답입니다.{attempt}번만에 맞혔습니다.")