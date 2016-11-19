def reversed_num(num):
    reverse = 0
    while num > 0:
        reminder = num%10
        reverse = (reverse * 10) + reminder
        num //= 10
    return reverse


def main():
    score = 0
    i, j, k = [int(x) for x in raw_input().split()]
    for number in range(i, j + 1):
        if abs(number) % k == abs(reversed_num(number)) % k:
            score += 1
    print score


if __name__ == '__main__':
    main()
