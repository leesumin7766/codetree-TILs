def check_multiples_of_3(numbers):
    for num in numbers:
        if num % 3 != 0:
            return 0
    return 1

# 5개의 숫자 입력 받기
numbers = [int(input()) for _ in range(5)]

# 모든 수가 3의 배수인지 판단
result = check_multiples_of_3(numbers)

# 결과 출력
print(result)