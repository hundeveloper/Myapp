    #  (공식: 시 = 총초 //3600, 나머지초 = 총초 % 3600, 
    #      분 = 나머지초 // 60,  초 = 나머지초 % 60)

time = 12345

hour = time // 3600
hour_seconds = time % 3600
min = hour_seconds // 60
sec = hour_seconds % 60

print(f"{time}의 초는 {hour}시 {min}분 {sec}입니다.")