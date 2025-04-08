#"Hello"와 "World"를 연결하여 출력
text = "Hello" + " " + "World"
print(text)

#대문자로 변환
print(text.upper())

#World만 슬라이싱
print(text[6:]) 

#Python is fun을 공백 기준으로 나누기
sentence = "Python is fun"
print(sentence.split())

# abcdef 에서 짝수 인덱스(0,2,4) 문자 출력
word = "abcdef"
print(word[0::2])  # 0, 2, 4번째 인덱스

# 6. "Hello"를 3번 반복하여 출력
print("Hello" * 3)