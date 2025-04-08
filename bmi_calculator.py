# 2)  질문: 사용자로부터 체중(kg)과 키(cm)를 입력받아 BMI를 계산하세요. 
#      (공식: BMI = 체중(kg) / (키(m)²))
#      파일명: bmi_calculator.py
#    실행: python bmi_calculator.py
#    결과: 체중(kg): 70
#    키(cm): 175
#               BMI: 22.9


cm = int(input("키를 입력하세요 : "))    
kg = int(input("몸무게를 입력하세요 : "))    

bmi = (kg/cm/cm)*10000 
print("결과: 체중(kg):", kg)
print("키(cm):", cm)
print("BMI: ", bmi)
