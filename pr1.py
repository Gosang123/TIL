print("체질량 지수 BMI를 확인해 보세요")

height = float(input("키를 입력하세요(단위: 미터) >>>"))
weight = float(input ("몸무게를 입력하세요>>> "))

# bmi = 몸무게 / 키 * 키
bmi = round(weight / height ** 2 ,1)
bmi_icon="ㅁ"
#163, 48
print("*" *20)
print("BMI 결과")


if bmi <18.5:
    print(bmi_icon)
    print("저체중입니다.")

elif bmi <25 :
    print(bmi_icon*2)
    print("정상입니다.")
elif bmi < 30:
    print(bmi_icon*3)
    print("경도 비만입니다.")
elif bmi <35:
    print(bmi_icon*4)
    print("중도 비만입니다.")

print("*" *20)
