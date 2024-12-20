
# 점프 투 파이썬 📚

### 학습용 교재::
![k362833219_1](https://github.com/user-attachments/assets/0be10c0a-51c4-4975-8e2a-ce46b79815dd)



*  MBC 아카데미 컴퓨터 교육센터 수원점에서 Ai 기초 학습으로 파이썬 학습 진행용

*  파이썬 Ai 기초 학습용

### ⏳ 교육 기간  
#### 2024.12 ~ 2025.02 (수료 예정)



#### 📖 While문 학습(12.20) 에서 커피 자판기 프로그램 미션(개인 실습)
```
# 미션 - 관리자가 커피 가격과 커피명을 정하고 개수를 입력한다.
#      - 소비자가 커피를 구매하는데 잔돈이 나와야 한다.
#      - 판매 종료 후 관리자가 커피 판매한 총액을 파악할 수 있어야 한다.

prompt = """
 ☕ 커피 자판기에 오신걸 환영합니다. ☕

1. 커피 구입하기
2. 관리자 메뉴
3. 통계 보기
4. 판매 종료

Enter
"""
number = 0      # 커피 자판기 메뉴 번호

while number != 4 :
    print(prompt)
    number = int(input())



    if number == 1:     # 1번 메뉴
    
            
        print("커피 구입하기 메뉴 입니다.")

        coffeeNum = 0   # 커피 구입하기 메뉴의 커피 버튼
        money = 0      
        total = 0       
        totalMoney = 0  

        # 판매할 커피 수량
        americano = 100
        caramel = 100
        capucino = 100
        coffeeLatte = 100

        print("구매할 커피를 골라주세요.")
        print("=====================")
        print("1.아메리카노 : 1000원")
        print("2.카라멜 : 3500원")
        print("3.카푸치노 : 3000원")
        print("4.커피라떼 : 2500원")
        print("0.이전 메뉴 돌아가기")
        print("=====================")
       
        coffeeNum = int(input())

    
        if coffeeNum == 1:

            print("아메리카노 선택하셨습니다. 가격은 1000원입니다.")
            print("돈을 넣어주세요.")
            money = int(input())
            total = money - 1000
            totalMoney = totalMoney + 1000
            americano = americano - 1
            print("잔돈은 %d원 입니다." % total)
            print("남은 커피는 %d잔 입니다." % americano)
            print("=====================")
            break

        elif coffeeNum == 2:
            print("카라멜 선택하셨습니다. 가격은 3500원입니다.")
            print("돈을 넣어주세요.")
            money = int(input())
            total = money - 3500
            totalMoney = totalMoney + 3500
            caramel = caramel - 1
            print("잔돈은 %d원 입니다." % total)
            print("남은 커피는 %d잔 입니다." % caramel)
            print("=====================")
            break
        
        elif coffeeNum == 3:
            print("카푸치노 선택하셨습니다. 가격은 3000원입니다.")
            print("돈을 넣어주세요.")
            money = int(input())
            total = money - 3000
            totalMoney = totalMoney + 3000
            capucino = capucino - 1
            print("잔돈은 %d원 입니다." % total)
            print("남은 커피는 %d잔 입니다." % capucino)
            print("=====================")
            break

        elif coffeeNum == 4:
            print("커피라떼 선택하셨습니다. 가격은 2500원입니다.")
            print("돈을 넣어주세요.")
            money = int(input())
            total = money - 2500
            totalMoney = totalMoney + 2500
            coffeeLatte = coffeeLatte - 1
            print("잔돈은 %d원 입니다." % total)
            print("남은 커피는 %d잔 입니다." % coffeeLatte)
            print("=====================")
            break

        elif coffeeNum == 0:
            print("이전 메뉴로 돌아갑니다.")
        
    elif number == 2:

        print("관리자 메뉴 입니다.")
        print("=====================")
        print("1.커피명 입력")
        print("2.커피 가격 입력")
        print("3.커피 개수 입력")
        print("0.이전 메뉴 돌아가기")
        print("====================")

        adminNum = 0
        adminNum = int(input()) # 관리자 메뉴 번호

        if adminNum == 1:
            print("커피명 입력해주세요.")
            coffeeName = input()
            print("%s 가(이) 입력되었습니다." % coffeeName)
            break

        elif adminNum == 2:
            print("커피 가격 입력해주세요.")
            coffeePrice = input()
            print("가격은 %s 원으로 책정 되었습니다." % coffeePrice)
            break

        elif adminNum == 3:
            print("커피 개수 입력해주세요.")
            coffeeCount = input()
            print("커피 개수는 %s 입니다." % coffeeCount)
            break

        elif adminNum == 0:
            print("이전 메뉴로 돌아갑니다.")


    elif number == 3:
        print("통계 메뉴 입니다.")
        print("=====================")
        print("1.판매한 총액 보기")
        print("2.판매한 갯수 보기")
        print("3.판매 평균 보기")
        print("0.이전 메뉴 돌아가기")
        print("=====================")

        statistics = 0
        statistics = int(input())   # 통계 메뉴 번호

        if statistics == 1:
            print("판매한 총액은 %d원 입니다." % totalMoney)
            break

        elif statistics == 2:
            print("판매한 총 갯수는 %d개 입니다." % (americano + caramel + capucino + coffeeLatte))
            break

        elif statistics == 3:
            print("판매 평균은 %d원 입니다." % (totalMoney / (americano + caramel + capucino + coffeeLatte)))
            break

        elif statistics == 0:
            print("이전 메뉴로 돌아갑니다.")
            
    elif number == 4:
        print("판매가 종료됩니다. 이용해 주셔서 감사합니다.")
        break

# 1번 누르면 커피 구입하기 메뉴 나오기
# 2번 누르면 커피명, 가격 정하는 메뉴 나오기
# 3번 누르면 통계
# 4번 누르면 프로그램 종료
```
