def main():
    score = 0
    i, j, k = [int(x) for x in raw_input().split()]
    for number in range(i, j + 1):
        if abs(number) % k - abs(int(str(number)[::-1])) % k == 0:
            score += 1
    print score


if __name__ == '__main__':
    main()
