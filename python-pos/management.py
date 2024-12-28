import datetime as t
import os


# 월 매출 파일에서 읽어온 다음 딕셔너리 형태로 저장한 후 변환하기

def month_margin(month) :   # 월 매출 데이터를 파일에서 읽어와서 딕셔너리 형태로 저장 후 반환 함수

    # 현재 파일의 절대 경로 기준으로 파일 경로 설정하기
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(BASE_DIR, "관리", month + "-total.txt")

    # 기본 데이터 구조 정의 (1-20까지 모든 상품 포함)
    default_data = {str(i): 0 for i in range(1, 21)}  # 1부터 20까지의 상품
    default_data.update({
        "card": 0,
        "cash": 0
    })

    if not os.path.exists(filepath):
        print(f"해당 파일이 없습니다. 새로 생성합니다.: {filepath}")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            for key, value in default_data.items():
                f.write(f"{key}/{value}\n")
        return {month: default_data}

    tmp_month = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            key, value = line.rstrip('\n').split('/')
            tmp_month[key] = int(value)

    # 누락된 키가 있으면 추가
    for key in default_data:
        if key not in tmp_month:
            tmp_month[key] = 0

    return {month: tmp_month}

# 받아온 day_sale 딕셔너리 이용하여 일 매출을 화면에 출력하기
# 월 매출 딕셔너리를 반환 받아서 화면에 출력하기
def main(goods, day_sale) :     # 매출 데이터 기반으로 일, 월 매출 화면 출력

    now = t.datetime.now()
    month = now.month
    day = now.day
    # now() 통해서 현재 날짜 가져오기

    if month < 10 :
        month = '0' + str(month)

    else:
        month = str(month)

    if day < 10 :
        day = '0' + str(day)

    else:
        day = str(day)

    while True:
        try:
            print("="*30)
            s_num = int(input("1.일 매출 / 2.월 매출 / 5.종료"))
            print("="*30 , end="\n")
        except ValueError:
            print("올바른 숫자를 입력해 주세요.")
            continue

        if s_num == 1:
            print("일 매출")
            print("=" * 30)
            for i in day_sale.keys():
                if i in ['card', 'cash']:
                    continue
                print("{}. {} : {}".format(i, goods[i]['품목'], day_sale[i]))

            print("=" * 30)
            # cash와 card 출력 수정
            print("card : {}".format(day_sale.get('card', 0)))
            print("cash : {}".format(day_sale.get('cash', 0)))
            print("=" * 30)
            print()


        elif s_num == 2:

            try:

                month = str(t.datetime.now().month).zfill(2)

                filepath = f"관리/{month}-total.txt"

                if not os.path.exists(filepath):
                    print("월 매출 데이터가 없습니다.")

                    return

                month_sale = {}

                with open(filepath, 'r', encoding='utf-8') as f:

                    for line in f:
                        key, value = line.rstrip('\n').split('/')

                        month_sale[key] = int(value)

                print("월 매출")

                print("=" * 30)

                # 상품별 매출 출력 (1부터 20까지 순서대로)

                for i in range(1, 21):

                    str_i = str(i)

                    if str_i in month_sale and str_i in goods:
                        print("{}. {} : {}".format(str_i, goods[str_i]['품목'], month_sale[str_i]))

                print("=" * 30)

                # 결제 수단별 매출 출력

                print("card : {}".format(month_sale.get('card', 0)))

                print("cash : {}".format(month_sale.get('cash', 0)))

                print("=" * 30)


            except Exception as e:

                print(f"월 매출 조회 중 오류 발생: {e}")

        elif s_num == 5:
            break

        else:
            print("="*30)
            print("다시 입력해 주세요.")
            print("=" * 30, end="\n")
            print()

