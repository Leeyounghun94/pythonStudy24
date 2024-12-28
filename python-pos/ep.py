# 변경된 재고 정보를 텍스트 파일에 저장하기
import datetime as t
import management
import os


def re_stock(goods) :   # 재고 정보를 텍스트 파일에 저장하는 함수
    with open("재고/goods.txt", 'w', encoding='utf-8') as f:
        for i in goods.keys() :
            f.write("{}/{}/{}/{}/{}\n".format(i, goods[i]['분류'], goods[i]['품목'], goods[i]['가격'], goods[i]['재고']))

# 일 매출 정보를 텍스트파일에 저장하기
def make_day_sale(month, day, day_sale):
    # 일 매출 저장
    filepath = f"관리/{month}{day}.txt"
    with open(filepath, "w", encoding='utf-8') as f:
        for key, value in day_sale.items():
            f.write(f"{key}/{value}\n")

# 월 매출 정보 불러와서 일 매출 정보를 더한 다음 텍스트 파일에 저장하기.
def make_month_sale(month, day_sale):
    try:
        # 기존 월 매출 데이터 읽기
        filepath = f"관리/{month}-total.txt"
        month_sale = {}

        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    key, value = line.rstrip('\n').split('/')
                    month_sale[key] = int(value)

        # 일 매출을 월 매출에 누적
        for key, value in day_sale.items():
            if key not in month_sale:
                month_sale[key] = value
            else:
                month_sale[key] += value

        # 갱신된 월 매출 저장
        with open(filepath, 'w', encoding='utf-8') as f:
            for key, value in month_sale.items():
                f.write(f"{key}/{value}\n")

        # print("월 매출 데이터가 성공적으로 업데이트되었습니다.")

    except Exception as e:
        print(f"월 매출 업데이트 중 오류 발생: {e}")

    return month_sale

def main(goods, day_sale) :  # 현재 날짜 기준으로 재고정보, 일, 월 매출 정보 저장, 업데이트

    now = t.datetime.now()

    #현재 날짜 가져오기
    month = now.month
    day = now.day

    # 월, 일을 두 자리 문자열로 변환하기
    month = f"{month:02}"
    day = f"{day:02}"

    re_stock(goods) # 재고 정보 저장
    make_day_sale(month, day, day_sale) # 일 매출 정보 저장
    make_month_sale(month, day_sale)    # 월 매출 업데이트