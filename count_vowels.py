text = "Python is awesome"
texts = "aeiouAEIOU"

count = 0
for char in text:
    if char in texts:
        count += 1

print(f"모음 개수 : {count}")