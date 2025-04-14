def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

if __name__ == "__main__":
    start = 10
    end = 50
    print("소수 리스트:", find_primes(start, end))