import random
import time
math_art="""

   111              222             3333
    11             22  22          3   333 
    11                22              333   
    11               22               333
    11              22             3   333
1111111111       2222222222         3333 
"""

print("Welcome To\n!!! Math Quiz !!!")
print(math_art)

playing=True
score=0
count=0

start_time=time.time()
while playing:

    num1=random.randint(1,9)
    num2=random.randint(1,9)
    num3=random.randint(1,9)

    answer=num1*num2-num3
    user_input=int(input(f"{num1}x{num2}-{num3}= "))
    count +=1

    if answer==user_input:
        score+=1
        print(f"정답입니다. 현재 점수는 {score}입니다.")
    else:
        playing=False
        print(f"아쉽네요 정답은{answer}입니다.")

end_time=time.time()
print("="*50)
print(f"총 {count}문제를 {round(end_time-start_time)}초만에 해결하였습니다.")
print("Math Quiz가 종료되었습니다.")
