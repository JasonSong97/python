# 반복문

# print("대기번호 : 1")
# print("대기번호 : 2")
# .
# .
    #변수

for waiting_no in [0,1,2,3,4]:   # 리스트 말고 range 가능(5) == 0,1,2,3,4   /  range(1,6) == 1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))

#리스트내에 값을들 변수에 다 넣어라 의미

#1
starbucks = ["아이언맨","토르","아이엠 그루트"]
for customer in starbucks:  # starbucks 리스트 안에 있는 사람들을 한명씩 부르면서 변수에 넣는 것.
    print("{0}, 커피가 준비되었습니다.".format(customer))
