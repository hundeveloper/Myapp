# id_number_parser.py

id_number = "901212-1234567"

# 앞 6자리 추출 (생년월일)
birth = id_number[:6]
gender_code = id_number[7]

# 년도 판별
if gender_code in ['1', '2']:
    year_prefix = "19"
elif gender_code in ['3', '4']:
    year_prefix = "20"
else:
    year_prefix = "19"  # 기본값 처리 (예외 상황 대비)

year = year_prefix + birth[0:2]
month = birth[2:4]
day = birth[4:6]

print(f"{year}년 {month}월 {day}일")