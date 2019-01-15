# 구구단 만들기 - 최윤석

x = input("몇 단을 출력 하시겠습니까?")

for num in range(1, 10):
    print(x, "*", num, "=", int(x) * num)

# 구구단 만들기 - 마르코
# 1) 사용자로부터 몇 단을 출력할 지 받을 것
# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

dan = int(input("몇 단을 출력 하시겠습니까?"))
# 입력값은 사용자가 숫자를 입력해도 문자로 인식함.
for num in range(1, 10):
    print("{} * {} = {}".format(dan, num, dan * num))
