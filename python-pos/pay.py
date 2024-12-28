import lotto
import datetime as t

# 성별 선택 함수
def choice_gender(guest_log) :  # 고객의 성별 데이터를 guest_log에 저장
    while True:
        print("="*30)
        gender = input("\n성별 입력\n1.남성 / 2.여성 :")
        print("="*30, end="\n")

        if gender == '1' :
            guest_log["gender"] = 'man'
            return

        elif gender == '2' :
            guest_log["gender"] = 'woman'
            return

        else :
            print("잘못된 입력입니다. 다시 선택해 주세요.")

# 물건 목록 띄우고 그 중에서 어떤 물건 구매할지 선택하기
# 물건의 수량 정보까지 취합하여 저장
# 구매 물건으로 로또를 선택할 경우 lotto.main() 호출

LOTTO_PRODUCT_NUMBER = '20'

# 상품 선택 함수
def select_goods(tmp, goods) :      # 상품 목록 출력, 선택한 상품의 번호와 수량을 tmp 저장.
    tmp_list = list(goods.keys())

    print("="*30)

    for i in tmp_list :
        print("\n{}.\t{}\t금액\t:\t{}".format(i, goods[i]['품목'], goods[i]['가격']))

    print("="*30, end="\n")

    while True :
        s_num = input("\n구매 상품 번호 :")
        if s_num in goods :
            break

    while True :
        try :
            count = int(input("\n구매 상품 수량 : "))
            break
        except ValueError :
            print("숫자로 입력해 주세요.")
            continue

    if s_num == LOTTO_PRODUCT_NUMBER:
        lotto.main(count)
    # 10 숫자가 들어오면 lotto.main() 호출

    while True :
        print("="*30)
        print("제품 : {} / 수량 : {}".format(goods[s_num]['품목'], count))
        print("="*30, end="\n")

        num = input("1.확인 / 2.취소")
        print("="*30, end="\n")
        if num == '1' :
            tmp[s_num] = count
            return False

        elif num == '2' :
            return True

# 구매하려는 물건 수량, 종류 선택하기

# 상품 구매 함수
def flow_choice(guest_log, goods) :

    boolean = True
    service = 0
    tmp_goods = guest_log['판매']

    while boolean :
        boolean = select_goods(tmp_goods, goods)

    guest_log['판매'] = tmp_goods

    while True :
        print("="*30)
        end_flag = input("1.다음 / 2.다른 물품 선택 :")
        print("="*30, end="\n")

        if end_flag == '1' :
            return False

        elif end_flag == '2' :
            return True

# 영수증 출력하기 위해 구매한 물건의 수량, 합계금액 정보 저장
def calc_cost(tmp_dic, goods) :     # 구매한 상품을 총 금액과 상세 정보를 계산하는 함수
    total = 0
    tmp_list = list(tmp_dic.keys())
    sale_dic = {}
    count = 0
    for i in tmp_list :
        tmp = {}
        count += 1
        t = goods[i]['가격'] * tmp_dic[i]
        total += t
        tmp['품목'] = goods[i]['품목']
        tmp['수량'] = tmp_dic[i]
        tmp['총 금액'] = t
        sale_dic[count] = tmp

    return sale_dic, total

# 결제 방법 선택
def select_payment() :
    print("="*30)
    payment = input("1.카드 / 2.현금 : ")
    print("="*30, end="\n")
    tmp = 0

    if payment == '1' :
        tmp = 1

    elif payment == '2' :
        tmp = 2

    else:
        return True, tmp

    return False, tmp

# 결제 방법 중 카드 결제 했을 경우
def select_card(sale_dic, total, guest_log) :
    print()
    print()
    print("= = = = = = 영수증 = = = = = = =")
    print("품목\t수량\t금액")
    print()

    for i in sale_dic.keys() :
        print("{}\t{}".format(sale_dic[i]['품목'], sale_dic[i]['총 금액']))

    print()
    print("="*30, end="\n")
    print("\ntotal : {}".format(total))
    print("="*30, end="\n")

    tmp = input("1.확인 / 2.취소 : ")

    print("=" * 30, end="\n")

    if tmp == '1' :
        print("결제가 완료되었습니다.")
        print("="*15)
        guest_log["결제"] = "card"
        guest_log["판매 금액"] = total
        guest_log["거스름돈"] = None
        return False

    elif tmp == '2' :
        print("결제가 취소되었습니다.")
        print("=" * 15)
        return True

    else:
        print("다시 입력하세요")
        return True

# 결제 방법 중 현금 결제 했을 경우
def select_cash(sale_dic, total, guest_log) :
    print()
    print()
    print("= = = = = = 영수증 = = = = = = =")
    print("품목\t수량\t금액")
    print()

    for i in sale_dic.keys():
        print("{}\t{}\t{}".format(sale_dic[i]['품목'], sale_dic[i]['수량'], sale_dic[i]['총 금액']))

    print()
    print("=" * 30, end="\n")
    print("\ntotal : {}".format(total))
    print("=" * 30, end="\n")

    while True:
        try:
            tmp = int(input("\n받은 현금 : "))
            if tmp < total:
                print("현금이 부족합니다. 금액을 다시 넣어 주세요")
                continue

            # 거스름돈 계산 및 저장 추가
            change = tmp - total
            print(f"\n거스름돈: {change}원")

            guest_log["결제"] = "cash"
            guest_log["판매 금액"] = total
            guest_log["거스름돈"] = change

            return False  # 성공적으로 처리됨

        except ValueError:
            print("숫자로 입력해 주세요")

# 물건 구매 후 결제
def flow_payment(guest_log, goods) :

    boolean = True
    select_num = 0
    tmp_goods = guest_log["판매"]
    sale_dic, total = calc_cost(tmp_goods, goods)

    while boolean :
        boolean, select_num = select_payment()

    boolean = True
    if select_num == 1 :
        while boolean :
            boolean = select_card(sale_dic, total, guest_log)

    elif select_num == 2 :
        while boolean :
            boolean = select_cash(sale_dic, total, guest_log)

    return False

def main(goods) :

    now = t.datetime.now()      # 현재 시간을 기록함.

    guest_log = {'판매' : {}}
    print("="*30)
    print(now)
    print("="*30, end="\n")

    while choice_gender(guest_log) :
        print("\n다시 입력해 주세요")

    while flow_choice(guest_log, goods) :
        continue

    while flow_payment(guest_log, goods) :
        continue
    # 고객의 성별, 물건 수량, 선택 저장, 결제 방법 을 저장.

    now_time = "{}-{}-{}/{}:{}".format(now.year, now.month, now.day, now.hour, now.minute)
    # 년-월-일/시:분 데이터 지정
    guest_log["일시"] = now_time

    print("="*30, end="\n")
    print()

    return(guest_log)