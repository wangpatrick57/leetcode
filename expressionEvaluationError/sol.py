def to_11(n):
    digits = []
    ans = 0

    while n > 0:
        digits.append(n % 10)
        n //= 10

    for digit in reversed(digits):
        ans *= 11
        ans += digit

    return ans

def print_answer(sum, count):
    answers = []

    for _ in range(count - 1):
        answers.append(1)
        sum -= 1

    answers.append(sum)
    print(' '.join([str(e) for e in answers]))

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        stats = input().split(' ')
        sum = int(stats[0])
        count = int(stats[1])
        print_answer(sum, count)
