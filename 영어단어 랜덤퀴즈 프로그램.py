import random

dict_eng = {"apple": "사과", "peach": "복숭아", "mango": "망고",
            "spring": "봄", "winter":"겨울","tree":"나무"}
keys= list(dict_eng.keys())
random.shuffle(keys)

for i in keys:
    user_input=input(f"{i}의 뜻은? >>>")

    if user_input == keys:
        print("정답입니다.")
    else:
        print(f"틀렸습니다. 정답은 {dict_eng[i]}입니다.")
