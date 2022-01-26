lock="""
    locked
비밀번호를 입력해 주세요

"""
unlock="""
    welcome!

"""
wrong_password="""
    locked
잘못된 비밀번호입니다.

"""

print(lock)
user_input=input("!! 잠금!! 비밀번호를 입력해 주세요>>>")

while user_input!='A1234!':
    print(wrong_password)
    user_input=input("잘못된 비밀번호입니다. 다시 입력하여 주세요 >>>")

print("!! 잠금이 해제되었습니다.!!")
print(unlock)
