# 이메일 주소 입력 받기
email = input("이메일 주소를 입력: ")

print(f"이메일 주소: {email}")


if "@" in email and "." in email:
    print("유효함")
else:
    print("유효하지 않음")