# 10문제씩 commit

# code up basic 100

# 1. 출력 ----- ----- ----- ----- ----- -----
# 6008
# print('print("Hello\\nWorld")')

# 2. 입출력 ----- ----- ----- ----- ----- -----
# 6009
# f = float(input())
# print(f)

# 6012 : 두 변수 입력(줄 바꿔 입력)
# i1 = input()
# i2 = input()
# print(i2)
# print(i1)

# 6014 : 반복 출력
# f = float(input())
# for i in range(3):
#     print(f)

# 6015 : 두 변수 입력(공백으로 구분 입력)
# a, b = input().split(" ")
# print("%s %s" % (b, a))

# 6017 : 똑같은 문장 '공백'주고 반복 출력 *
# s = input()
# print(s, s, s)
# print("%s %s %s" % (s, s, s))

# 6018 : 시간 입출력
# y, m, d = input().split(".")
# print("%s-%s-%s" % (d, m, y))

# 6019
# a, b = input().split("-")
# print("%s%s" % (a, b))

# 6021 : 5개 문자로 이루어진 단어 줄바꿔 출력
# a = input()

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# 6022
# s = input().split(" ")
# # print("%s%s" % (s[0], s[1]))
# print("%s" % (s[0]+s[1]))


# 3. 변환 ----- ----- ----- ----- ----- -----
# 1) 진수 변환
# 2) 데이터 타입 변환

# 6025 : 16진수로 입력
# a = int(input(), 16)
# print("{0:o}".format(a))

# 6030 : 영문자 입력, 10진수 변환 (ord => 문자를 숫자로 // chr => 숫자를 문자로)
# a = ord(input())
# b = chr(a+1)
# print(b)

# 6033 : 문자 입력 후 그 다음 문자 출력
# 사고 흐름 : '다음'이 키워드 => 순서 => 숫자 = 문자를 어떻게 숫자화하지?
# a = ord(input())
# b = chr(a+1)
# print(b)

# 6034 : 같은 문자 여러번 출력 **
# >> 원래 내 방식
# a, b = input().split(" ")
# b = int(b)
# for i in range(b):
#     print("{0}".format(a), end="")

# >> 간단한 방식
# a, b = input().split(" ")
# print(a*int(b))

# 3. 산술 연산 ----- ----- ----- ----- ----- -----
# 6038
# a, b = map(int, input().split(" "))
# print(a % b)

# 6042 : 반올림
# a = float(input())
# print(round(a, 2))

# 6047 : 비트시프트 연산(2배는 기본으로 깔고 드감) *
# a<<1 : a를 2배
# a>>1 : a를 1/2배
# a<<2 : a를 4배
# a, b = map(int, input().split())
# print(a << b)


# boolean을 다루는 예약어 : not, and, or
# 6048 : true -> false, false -> true "not" *
# >> 원래 내 방식
# a = int(input())
# if a == 0:
#     print(bool(1))
# else:
#     print(bool(0))

# >>간단한 방식
# a = bool(int(input()))
# print(not a)

# 6054
# a, b = map(int, input().split(" "))
# print(bool(a) or bool(b))
