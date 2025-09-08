numbers = []
total = 10

while True:
    num = int(input("숫자를 입력하시오: "))
    numbers.append(num)
    total += num

    if total > 50:
        break


print("입력된 숫자들:", numbers)
print("숫자의 개수:", len(numbers))
print("숫자의 합", total)