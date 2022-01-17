coffee="""
｡ﾟﾟ･｡･ﾟﾟ｡
ﾟ。    　｡ﾟ
　ﾟ･｡･ﾟ
⠀()_/)
⠀(｡ˆ꒳ˆ)⠀
ଫ/⌒づ♡

"""
menu="""
        커피 자판기
        -메 뉴-
    
    1:아메리카노 1,800원
    2:카페라뗴   2,700원
    3:핫초코     2,300원
"""

print(coffee)
print(menu)
print("="*45)

coffee_price=0
total_price=0
change =0

order=input("커피종류를 선택하세요. 번호 입력>>>")

if '1'<= order <='3':
    
    if order =='1':
        coffee_price=1800
    elif order =='2':
        coffee_price=2700
    elif order =='3':
        coffee_price=2300

    cups=int(input("몇 잔을 드릴까요? >>>"))
    total_price=coffee_price*cups

    received=int(input(f"총 금액은 {total_price}원 입니다. 돈을 투입해 주세요>>>>"))
    if received>=total_price:
        change=received-total_price
        print(f"{received}원을 받았습니다. 거스름돈은{change}원입니다.")
        #1,000원,500원, 100원
        #1000원 지폐: 3700//1000 500원 동전: 잔액(700)//500.
        
        change_1000=change//1000
        remain_1000=change%1000
        change_500=remain_1000//500
        remain_500=remain_1000%500
        change_100=remain_500//100

        print(f"1000원 지폐{change_1000}장,500원 동전{change_500}개,100원 동전{change_100}개")

    else:
        print("금액이 부족합니다. 주문이 취소되었습니다.")
else:
    print("잘못된 주문입니다. 다시 확인해 주세요.")