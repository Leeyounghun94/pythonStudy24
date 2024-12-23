
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

#### 📖 For문 학습(12.23) 에서 커피 자판기 프로그램 미션(개인 실습(For, While 병행))
```
# 미션 - 커피 자판기를 리스트화 해서 for문으로 구현하기.

# 커피 종류가 5개(커피명, 수량, 단가)
# 사용자 커피를 반복 구매
# 관리자가 판매 종료 후 통계 보기 출력



coffee_menu = [ 
{"name" : "아메리카노", "price" : 2000, "cellCount" : 100},
{"name" : "카페라떼", "price" : 3000, "cellCount" : 100},
{"name" : "카라멜마끼아또", "price" : 3500, "cellCount" : 100},
{"name" : "바닐라라떼", "price" : 3800, "cellCount" : 100},
{"name" : "콜드브루", "price" : 4000, "cellCount" : 100}]

totalMoney = 0  # 총액
totalSell = 0   # 총 갯수
exit_program = False  # 종료 여부

while not exit_program:
    
    print("""
 ☕ 커피 자판기에 오신걸 환영합니다.(version.2.0.0) ☕

1. 커피 구입하기
2. 관리자 메뉴
3. 통계 보기
4. 판매 종료
""")

    try:
        main_Menu_num = int(input("메뉴를 선택해주세요. : "))
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        continue

    if main_Menu_num == 1 :
        while True:
            print("\n구매할 커피를 고르세요")
            print("=====================")

           
            # 파이썬 내장함수 -> enumerate : 순서가 있는 자료형(list, set, string , dictionary, tuple)을 입력 받았을 때 인덱스 포함해서 리턴, for문과 자주 사용된다. 인덱스와 값을 동시에 접근하면서 루프를 돌릴 때 사용한다.
            # 형식 : enumerate(순서가 있는 객체, start=0)
            for idx, coffee in enumerate(coffee_menu, start=1):
                print(f"{idx}. {coffee['name']} : {coffee['price']}원 (재고: {coffee['cellCount']}개)")
            print("0. 이전 메뉴 돌아가기")
            print("=====================")

            try:
                coffee_choice = int(input("입력 : "))
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")
                continue

            if coffee_choice == 0:
                print("이전 메뉴로 돌아갑니다.")
                break

            elif 1 <= coffee_choice <= len(coffee_menu):
                selected_coffee = coffee_menu[coffee_choice - 1]

                if selected_coffee["cellCount"] > 0:
                    print(f"{selected_coffee['name']}를 선택하셨습니다. 가격은 {selected_coffee['price']}원 입니다." )

                    try:
                        money = int(input("돈을 넣어주세요 : "))
                    except ValueError:
                        print("잘못된 입력입니다. 숫자를 입력해주세요.")
                        continue

                    if money >= selected_coffee["price"]:
                        change = money - selected_coffee["price"]
                        selected_coffee["cellCount"] -= 1
                        totalMoney += selected_coffee["price"]
                        totalSell += 1

                        print(f"{selected_coffee['name']}를 구매하셨습니다. 거스름돈은 {change}원 입니다.")
                        print(f"남은 {selected_coffee['name']} 재고는 {selected_coffee['cellCount']} 개 입니다.")
                    
                    else:
                        print("돈이 부족합니다. 돈을 다시 넣어주세요")
                        continue

                else:
                    print("잔여 수량이 없습니다. 다시 선택해주세요.")

            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")

    elif  main_Menu_num == 2 :
        print("관리자 메뉴입니다.")
        while True:
            print("=====================")
            print("1.커피 등록하기")
            print("2.커피 수량 수정")
            print("3.커피 단가 수정")
            print("4.이전 메뉴로 돌아가기")
            print("=====================")

            try:
                admin_choice = int(input("입력 : "))
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")
                continue

            if admin_choice == 4:
                print("이전 메뉴로 돌아갑니다.")
                break
                
            elif admin_choice == 1:
                print("커피를 등록합니다.")
                new_coffee_name = input("커피 이름을 입력하세요 : ")
                new_coffee_price = int(input("커피 가격을 입력하세요 : "))
                new_coffee_count = int(input("커피 재고를 입력하세요 : "))
                new_coffee = {"name" : new_coffee_name, "price" : new_coffee_price, "cellCount" : new_coffee_count}
                coffee_menu.append(new_coffee)
                print("커피가 등록되었습니다.")

            elif admin_choice == 2:
                print("커피 수량을 수정합니다.")
                for idx, coffee in enumerate(coffee_menu, start=1):
                    print(f"{idx}. {coffee['name']} : {coffee['price']}원 (재고: {coffee['cellCount']}개)")
                coffee_choice = int(input("수정할 커피의 번호를 입력하세요 : "))
                coffee_menu[coffee_choice - 1]["cellCount"] = int(input("수정할 수량을 입력하세요 : "))
                print("커피 수량이 수정되었습니다.")

            elif admin_choice == 3:
                print("커피 단가를 수정합니다.")
                for idx, coffee in enumerate(coffee_menu, start=1):
                    print(f"{idx}. {coffee['name']} : {coffee['price']}원 (재고: {coffee['cellCount']}개)")
                coffee_choice = int(input("수정할 커피의 번호를 입력하세요 : "))
                coffee_menu[coffee_choice - 1]["price"] = int(input("수정할 가격을 입력하세요 : "))
                print("커피 단가가 수정되었습니다.")

            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")

    elif main_Menu_num == 3:
        print("\n커피 판매를 종료합니다. 통계가 출력이 됩니다.")
        print("=====================")
        print(f"총 판매 금액 : {totalMoney}원")
        print(f"총 판매 갯수 : {totalSell}개")

        if totalSell > 0 :
            print(f"평균 판매 금액 : {totalMoney / totalSell}원")
        
        else:
            print("판매된 커피가 없습니다.")
        print("=====================")
        exit_program = True

    elif main_Menu_num == 4:
        print("커피 판매 프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
        exit_program = True

    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

# 개발하는 것은 밑도 끝도 없기 때문에 프로그램 개발 하기 앞서 C R U D를 먼저 체계적으로 잡아놔야 가지를 뻗어 나갈 수 있다.
```
#### 📖 함수(Function) 학습(12.23) 에서 커피 자판기 프로그램 미션(개인 실습(각 메뉴 별 함수 지정해보기))
```
# 미션 - 자판기 코드를 함수로 Rebuilde를 해보자

# 1번 메뉴 눌렀을때 커피 메뉴를 def 묶어 밑에서 실행해서 돌리게끔..

coffee_menu = [     # 커피명, 가격, 판매갯수 초기 데이터 설정
{"name" : "아메리카노", "price" : 2000, "cellCount" : 100},
{"name" : "카페라떼", "price" : 3000, "cellCount" : 100},
{"name" : "카라멜마끼아또", "price" : 3500, "cellCount" : 100},
{"name" : "바닐라라떼", "price" : 3800, "cellCount" : 100},
{"name" : "콜드브루", "price" : 4000, "cellCount" : 100},
                    ]

totalMoney = 0  # 총액
totalSell = 0   # 총 갯수

def main_menu() :
    # 함수 main_menu() 설정

    print("""
 ☕ 커피 자판기에 오신걸 환영합니다.(version.3.0.0) ☕

1. 커피 구입하기
2. 관리자 메뉴
3. 통계 보기
4. 판매 종료
""")

def buy_coffee():
    # 함수 buy_coffee() 설정 : 커피 구매하기 메뉴

    global totalMoney, totalSell
    while True:
        print("\n구매할 커피를 고르세요")
        print("=====================") 
            # 파이썬 내장함수 -> enumerate : 순서가 있는 자료형(list, set, string , dictionary, tuple)을 입력 받았을 때 인덱스 포함해서 리턴, for문과 자주 사용된다. 인덱스와 값을 동시에 접근하면서 루프를 돌릴 때 사용한다.
            # 형식 : enumerate(순서가 있는 객체, start=0)
        for idx, coffee in enumerate(coffee_menu, start=1):
                print(f"{idx}. {coffee['name']} : {coffee['price']}원 (재고: {coffee['cellCount']}개)")
        print("0. 이전 메뉴 돌아가기")
        print("=====================")

        try:
            coffee_choice = int(input("입력 : "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            continue

        if coffee_choice == 0:
            print("이전 메뉴로 돌아갑니다.")
            break

        elif 1 <= coffee_choice <= len(coffee_menu):
            selected_coffee = coffee_menu[coffee_choice - 1]

            if selected_coffee["cellCount"] > 0:
                print(f"{selected_coffee['name']}를 선택하셨습니다. 가격은 {selected_coffee['price']}원 입니다." )
                try:
                     money = int(input("돈을 넣어주세요 : "))
                except ValueError:
                    print("잘못된 입력입니다. 숫자를 입력해주세요.")
                    continue

                if money >= selected_coffee["price"]:
                    change = money - selected_coffee["price"]
                    selected_coffee["cellCount"] -= 1
                    totalMoney += selected_coffee["price"]
                    totalSell += 1

                    print(f"{selected_coffee['name']}를 구매하셨습니다. 거스름돈은 {change}원 입니다.")
                    print(f"남은 {selected_coffee['name']} 재고는 {selected_coffee['cellCount']} 개 입니다.")
                    
                else:
                    print("돈이 부족합니다. 돈을 다시 넣어주세요")
                    continue

            else:
                print("잔여 수량이 없습니다. 다시 선택해주세요.")

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

def admin_menu():
    # 함수 admin_menu() 설정 : 관리자 메뉴

    while True:
        print("관리자 메뉴입니다.")
        print("=====================")
        print("1.커피 등록하기")
        print("2.커피 수량 수정")
        print("3.커피 단가 수정")
        print("4.이전 메뉴로 돌아가기")
        print("=====================")

        try:
            admin_choice = int(input("입력 : "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            continue

        if admin_choice == 4:
            print("이전 메뉴로 돌아갑니다.")
            break
                
        elif admin_choice == 1:
            print("커피를 등록합니다.")
            new_coffee_name = input("커피 이름을 입력하세요 : ")
            new_coffee_price = int(input("커피 가격을 입력하세요 : "))
            new_coffee_count = int(input("커피 재고를 입력하세요 : "))
            new_coffee = {"name" : new_coffee_name, "price" : new_coffee_price, "cellCount" : new_coffee_count}
            coffee_menu.append(new_coffee)
            print("커피가 등록되었습니다.")

        elif admin_choice == 2:
            print("커피 수량을 수정합니다.")
            for idx, coffee in enumerate(coffee_menu, start=1):
                print(f"{idx}. {coffee['name']} : {coffee['price']}원 (재고: {coffee['cellCount']}개)")
            coffee_choice = int(input("수정할 커피의 번호를 입력하세요 : "))
            coffee_menu[coffee_choice - 1]["cellCount"] = int(input("수정할 수량을 입력하세요 : "))
            print("커피 수량이 수정되었습니다.")

        elif admin_choice == 3:
            print("커피 단가를 수정합니다.")
            for idx, coffee in enumerate(coffee_menu, start=1):
                print(f"{idx}. {coffee['name']} : {coffee['price']}원 (재고: {coffee['cellCount']}개)")
            coffee_choice = int(input("수정할 커피의 번호를 입력하세요 : "))
            coffee_menu[coffee_choice - 1]["price"] = int(input("수정할 가격을 입력하세요 : "))
            print("커피 단가가 수정되었습니다.")

        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

def statistics():
    # 함수 statistics() 설정 : 통계 보기

        print("통계가 출력이 됩니다.")
        print("=====================")
        print(f"총 판매 금액 : {totalMoney}원")
        print(f"총 판매 갯수 : {totalSell}개")

        if totalSell > 0 :
            print(f"평균 판매 금액 : {totalMoney / totalSell}원")
        
        else:
            print("판매된 커피가 없습니다.")
        print("=====================")

exit_program = False

while not exit_program:
    main_menu()
    try:
        main_Menu_num = int(input("메뉴를 선택해 주세요 : "))
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        continue

    if main_Menu_num == 1:
        buy_coffee()
            
    elif main_Menu_num == 2:
        admin_menu()

    elif main_Menu_num == 3:
        statistics()
            
    elif main_Menu_num == 4:
        print("프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
        exit_program = True

    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
```
