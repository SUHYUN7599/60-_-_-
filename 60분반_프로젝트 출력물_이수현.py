print("고객님의 월급과 연봉으로 무엇을 할 수 있는지를 알 수 있게 하는 프로그램입니다!")


#로그인 하기
cnt = 0
 
while True:
 
    # ID, PW 입력받기
    id = input('ID 입력:')
    pw = input('PW 입력:')
 
    # ID 와 PW 일치하는지 비교
    if id=='BACKKOM' and pw=='Pysj0518!!':
        print('로그인 성공')
        break
    else:
        cnt = cnt + 1
        print('로그인 {}회 실패'.format(cnt))
 
    if cnt >= 3:       
        print('보안을 위해 로그인 시스템을 종료합니다!')
        break
 
    #줄바꿈
    print()
    
    
    
#기초 정보 입력    
print("기초 정보를 입력하겠습니다.")
pay = input("시급을 입력해주세요 : ")
time_of_day = input("일일근무시간 : ")
day_of_month = input("한달근무일수 : ")

pay = int(pay)
time_of_day = int(time_of_day)
day_of_month = int(day_of_month)

# 월급 계산
profit = pay * time_of_day * day_of_month
#연봉 계산
salary = profit * 12

# 결과 출력
#월급과 연봉 안내
print("고객님의 예상 월급은 : {0}원입니다.\n\n".format(profit))
print("고객님의 예상 연봉은 : {0}원입니다.\n\n".format(salary))
# 활용 질문
print("{0}원으로 무엇을 할 수 있을까요?".format(profit))
print("{0}원으로 무엇을 할 수 있을까요?".format(salary))
#활용 안내
print("야구 경기 관람 (25000원 기준) : {0}경기".format(profit / 15000))
print("스타벅스 스무디 한잔 (6800원 기준) : {0}잔".format(profit / 6800))
print("제주도 왕복 비행기 (50000원 기준) : {0}편".format(profit / 50000))
print("코인 노래방 (10000원 기준) : {0}시간".format(profit / 10000))
print("유럽 여행 (3000000원 기준) : {0}회".format(salary / 3000000))
print("자동차 구매 (18000000원 기준(모닝, 스파크)) : {0}대".format(salary / 18000000))
print("아파트 구하기(매매) (3000000000원 기준) : {0}채".format(salary / 300000000))


print('''
돈이 없으면 뭐 어때요...
지금 행복하면 됐지요 ㅎㅎㅎ
항상 긍정적으로 생각하세요!!!''')

print("이용해주셔서 대단히 감사합니다!")
