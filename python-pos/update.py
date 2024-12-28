# pay.main()이 반환한 고객의 매출 정보를 이용해서 일 매출과 재고 정보 갱신
def main(goods, guest_log, day_sale):
    guest_dic = guest_log["판매"]

    # 상품별 매출 업데이트
    for product_id, quantity in guest_dic.items():
        sale_amount = quantity * goods[product_id]['가격']

        # 일 매출에 상품별 매출 추가/갱신
        if product_id not in day_sale:
            day_sale[product_id] = sale_amount
        else:
            day_sale[product_id] += sale_amount

        # 재고 감소
        goods[product_id]['재고'] -= quantity

    # 결제 방식별 매출 업데이트
    payment_type = guest_log['결제']
    payment_amount = guest_log['판매 금액']

    # 결제 수단별 매출 추가/갱신
    if payment_type not in day_sale:
        day_sale[payment_type] = payment_amount
    else:
        day_sale[payment_type] += payment_amount

    return day_sale