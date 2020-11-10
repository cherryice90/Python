# 2020.11.10 23.30
# 코딩이란
# https://learnaday.kr/my-account/my-course/0AEGB1/MxpQgs/56724
# 코딩으로 가능한 것!
# 구글, 네이버, g마켓 같은 인터넷 서비스
# 리니지, FIFA, LOL 같은 게임
# 카카오톡, 인스타그램, 넷플릭스 같은 모바일 서비스
# ERP, MS오피스, 알집같은 오피스 SW
# 인공지능 스피커, 스마트 시계와 같은 IoT

# 2020.11.11 00.05
# 파이썬-변수
# https://learnaday.kr/my-account/my-course/0AEGB1/MxpQgs/56726
# 변수는 데이터를 저장하는 공간  = : 코딩에서 값을 변수에 넣고 싶을때 변수명을 만들고,
# 저장할 데이터를 넣는다. >> a = 6 변수명 a에 변수값 6을 저장한다.

# https://learnaday.kr/my-account/my-course/0AEGB1/MxpQgs/56727
# 변수명 규칙
# 1. 대/소문자 구분한다
# 2. 띄어쓰기 불가
# 3. 특수기호 사용불가/예외 _ (언더바 : 밑줄)
# 4. 숫자가 맨앞에 오거나 숫자 단독으로는 불가
# 5. 맨앞에 문자오고 이후 숫자는 가능
# use python

a=6
print(a)  >> 변수 a에 저장된 6을 출력
print("a") >> 문자 a를 출력



# https://learnaday.kr/my-account/my-course/0AEGB1/MxpQgs/56729
# 저장할 데이터의 형태에 따라 변수의 형태가 달라짐
# 이것을 자료형이라 한다.

# 1. https://learnaday.kr/my-account/my-course/0AEGB1/MxpQgs/56730
a=6
# 데이터가 정수일 경우 : int
a=6
# type은 어떠한 데이터 형태인가를 나타냄.
print(type(a))
<class 'int'>

b=3.14
# 데이터가 실수일 경우 : float
c="python"
# 데이터가 문자열일 경우 : str(string)
d=[1,2,3,4,5]
# 데이터가 리스트(배열)일 경우 : list
e={"사과":"apple", "포도":"grape","오렌지":"orange"}
# 데이터가 딕셔너리일(key, value) 경우 : dict
f=True / g=False
# 데이터가 불린(boolean) 참/거짓 판단일 경우 : bool


# 연산이 가능한 정수형(int)과 실수형(float)
# 더하기
  print(a+b)
# 빼기
  print(a-b)
# 곱하기
  print(a*b)
# 나누기
  print(a/b)
# 몫 구하기
  print(a//b)
# 나머지 구하기
  print(a%b)
# 제곱 구하기
  print(a**b)
# 최댓값
  print(max(a,b))
# 최소값
  print(min(a,b))

  x=5
  x = x+1 >>> x += 1
  # 같은 표현
  print(x) = 6

# https://learnaday.kr/my-account/my-course/0AEGB1/MxpQgs/56731
# 문자열 str
# 데이터가 문자열일 때 >> str (string) 을 사용
  c="지수 바보" d="시작"
# 문자 이어주기
  print(c+d)
  # = 지수 바보시작
# 문자열 거꾸로 만들기
  print(c[::-1])
  # = 보바 수지
# 문자열 반복
  print(d*3)
  # = 시작시작시작
# 글가져오기
  print(c[0])
  # = 지
  print(c[3])
  # = ' ' 빈공간도 값
  print(c[1:5])
  # 인덱스 1번부터 5번전까지 (1,2,3,4)의 데이터를 가져와라
  # = 수 바보
  print(c[1:])
  # index 1번부터 끝까지 다 가져옴
  print(c[-1])
  # = index 0번의 데이터를 가져온다.
# 문자열의 길이 구하기 : length ==>
  print(len(c))
  # 5
# 문자열에 있는 글자 개수 구하기
  print(c.count('지'))
  # 1
# 문자열에서 특정 글자 바꾸기
  print(c.replace('바보','사랑해'))
  # 지수 바보 >> 지수 사랑해 로 변경
# 문자열을 리스트로 분리하기
  print(c.split())
  # = ['지수', "바보"]
  # c의 값을 빈칸을 기준으로 분리후에 리스트에 넣는다.
  f="지수,바보멍청이"
  print(f.split(","))
  # 반점기준으로 분리하여 리스트에 데이터를 넣는다.
  # = ['지수', "바보멍청이"]
