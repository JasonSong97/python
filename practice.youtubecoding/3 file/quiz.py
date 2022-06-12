# http://naver.com
# 1. http:// 를 제거 2. 처음 만나는 점(.) 이후 부분은 제거 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성


# url = "http://google.com"
# my_str = url.replace("http://","")
# my_str = my_str[:my_str.index(".")]


# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"     # int 는 정수   / str 은 정수를 문자로
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))