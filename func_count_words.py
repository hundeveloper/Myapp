def count_words(text):
    return len(text.split())

if __name__ == "__main__":
    text = "I love python"
    print("단어 수:", count_words(text))