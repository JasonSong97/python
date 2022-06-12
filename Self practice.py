# 2022년 5월 31일
# 1
# a = int(input("첫번쨰 값을 입력해주세요"))
# b = int(input("두번쨰 값을 입력해주세요"))

# sum = 0

# for i in range(a, b+1):
#     sum += i

# print(a, "부터", b, "까지의 합은 ", sum, "입니다.")


# #2
# from calendar import c
# from datetime import datetime
# birthDay = input("태어난 생년월일을 입력해주세요 : YYYYMMDD")

# year = int(birthDay[0:4])
# month = int(birthDay[4:6])
# day = int(birthDay[6:8])
# print(year, "/", month, "/", day)
# now = datetime.now()

# curYear = now.year
# curMonth = now.month
# curDay = now.day

# KoreanAge = curYear - year + 1
# age = curYear - year

# birthMonthDay = month  * 100 + day
# curMonthDay = curMonth * 100 + curDay

# if curMonthDay < birthMonthDay :
#     age -= 1

# print("한국나이는 ", KoreanAge, "이고, 만 나이는 ", age, "입니다." )

# = getAge(int(birthDay))

# 2022년 6월 2일

# 년도 4자리수 무작위로 받기
# 받은 값 4로 나누기          #받은값 100나누기                #받은값 400으로 나누기
# 4로 나누어 떨어지면         #0으로 떨어지면 윤년 x            #나누어 떨어져야함
# 윤년

# 년도 입력
# a b c
# 교집합

# year = int(input("연도를 입력하세요"))

# a = year % 4
# b = year % 100
# c = year % 400

# if a == 0 and c == 0 or b != 0 :
#     print("윤년")
# else :
#     print("윤년이 아닙니다")

# 2022년 6월 3일

# 무작위 금액 한가지
# 나눠서 거스름돈 주는것
# 조건 : 최소 수량
# 23만 7천 7백원
# 10만원 2
# 1만 3
# 5천 1
# 1천 2
# 500 1
# 100 2
# # 10만원 5만원 1만원 5천원 1천원 5백원 1백원 10원
# 큰금액 순서대로 줄것

# money = int(input("거스름돈을 말해주세요, 단 1원짜리는 없습니다"))

# import math

# a1 = (money) / 100000
# b1 = (math.trunc(a1))
# c1 = (money) % 100000

# if c1 != 0 :
#     a2 = (c1) / 50000
#     b2 = (math.trunc(a2))
#     c2 = (c1) % 50000
#     if c2 != 0 :
#         a3 = (c2) / 10000
#         b3 = (math.trunc(a3))
#         c3 = (c2) % 10000
#         if c3 != 0 :
#             a4 = (c3) / 5000
#             b4 = (math.trunc(a4))
#             c4 = (c3) % 5000
#             if c4 != 0 :
#                 a5 = (c4) / 1000
#                 b5 = (math.trunc(a5))
#                 c5 = (c4) % 1000
#                 if c5 != 0 :
#                     a6 = (c5) / 500
#                     b6 = (math.trunc(a6))
#                     c6 = (c5) % 500
#                     if c6 != 0 :
#                         a7 = (c6) / 100
#                         b7 = (math.trunc(a7))
#                         c7 = (c6) % 100
#                         if c7 != 0 :
#                             a8 = (c7) / 50
#                             b8 = (math.trunc(a8))
#                             c8 = (c7) % 50
#                             if c8 != 0 :
#                                 a9 = (c8) / 10
#                                 b9 = (math.trunc(a9))
#                                 print("10만원",b1,"장, 5만원권",b2,"장, 1만원",b3,"장, 5천원",b4,"장, 1천원",b5,"장, 500원",b6,"개, 100원",b7,"개, 50원",b8,"개, 10원",b9,"개 입니다")
#                             else :
#                                 print("10만원",b1,"장, 5만원권",b2,"장, 1만원",b3,"장, 5천원",b4,"장, 1천원",b5,"장, 500원",b6,"개, 100원",b7,"개, 50원",b8,"개 입니다")
#                         else :
#                             print("10만원",b1,"장, 5만원권",b2,"장, 1만원",b3,"장, 5천원",b4,"장, 1천원",b5,"장, 500원",b6,"개, 100원",b7,"개 입니다")
#                     else :
#                         print("10만원",b1,"장, 5만원권",b2,"장, 1만원",b3," 장, 5천원",b4,"장, 1천원",b5,"장, 500원",b6,"개 입니다")
#                 else :
#                     print("10만원",b1,"장, 5만원권",b2,"장, 1만원",b3,"장, 5천원",b4,"장, 1천원",b5," 장 입니다")
#             else : 
#                 print("10만원",b1,"장, 5만원권",b2,"장, 1만원",b3,"장, 5천원",b4,"장 입니다")
#         else :
#             print("10만원",b1,"장, 5만원권",b2,"장, 1만원",b3,"장 입니다")
#     else :
#         print("10만원",b1,"장, 5만원권",b2,"장 입니다")
# else :
#     print("10만원", b1,"장 입니다")

money = int(input("거스름돈을 말해주세요, 단 1원짜리는 없습니다"))

import math

changes = [100000, 50000, 10000, 1000, 500, 100, 50, 10]           #리스트 사용

for i in range(0, len(changes)) :
    cnt = math.trunc(money / changes[i])
    money = money - cnt * changes[i]
    print('%7d'%changes[i], "원 ", cnt, "개")