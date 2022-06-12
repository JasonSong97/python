# 순서를 가지는 객체의 집합

# 지하철탐 칸별로 10명 20명 30명 있음
# subway1 = 10
# subway2 = 20
# subway3 = 30
# 이거를 간단하게 묶어 버림

# subway = [ 10, 20, 30]  #subway 리스트에 위의 것들을 묶어 버린것(EZ)
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호가 몇번쨰 칸에 탔는가
# print(subway.index("조세호"))
# #하하가 탑승
# subway.append("하하")  # append는 항상 뒤에 붙음
# print(subway)

# #정형돈씨를 유재석 / 조세호 사이에 넣기

# subway.insert(1, "정형돈")   # 정형돈을 1번쨰 순서에 넣는 다는 것
# print(subway)

#지하철에 있는 사람 한명씩 빼기
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
# print(subway.pop())
# print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#정렬도 가능
num_list = [ 5, 2 , 4, 3, 1]
num_list.sort()  # 정렬
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#자료형과 함꼐 사용
mix_list = ["조세호", 1, True]
num_list = [5,4,3,1,2]
# print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)
