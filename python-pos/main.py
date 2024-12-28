import ep
import gmanagement
import management
import pay
import update

# 재고, 물품 정보를 텍스트 파일에서 읽어오기
# goods(상품), day_sale(일 매출) 딕셔너리 생성

f = open("재고/goods.txt", "r", encoding='UTF8')
goods = {}  # 상품 정보, 재고 저장(배열 처리)
day_sale = {"card":0, "cash":0} # 일 매출 정보(카드, 현금) 저장

while(True) :
    tmp_dic = {}
    line = f.readline()     # 한줄씩 읽어온다.
    line = line.rstrip("\n")    # 읽은 줄 끝에 줄바꿈(\n) 제거
    if(line=="") :
        break   # 파일 끝에 도달했을 때 break (while 종료)

    st_list = line.split("/")   # 문자열을 리스트로 변환하기.
    # / 기준으로 문자열을 나눠서 리스트 변환함, 11/과자/맛동산/1000/10 -> st_list = [11, "과자", "맛동산", - - -]

    # 하나의 상품 데이터 저장하는 딕셔너리
    tmp_dic["분류"] = st_list[1]
    tmp_dic["품목"] = st_list[2]
    tmp_dic["가격"] = int(st_list[3])
    tmp_dic["재고"] = int(st_list[4]) # 가격과 재고는 숫자(정수)가 들어가니 int로 타입변환

    # 데이터 저장하기
    goods[st_list[0]] = tmp_dic # goods = 전체 상품 데이터 저장(키:st_list[0], 값:tmp_dic
    day_sale[st_list[0]] = 0    # day_sale = 일 매출 데이터 저장(키:st_list[0], 값:0

# 메인 메뉴 설정하기
while True:
    print("="*30)
    print("1. 상품 구매하기 \n2. 물품 관리 \n3. 매출 관리 \n9. 종료")
    print("="*30, end="\n")
    select_num = input("선택 : ")

    if select_num == '1':
        tmp = pay.main(goods)
        update.main(goods, tmp, day_sale)
    # 1번 선택하였을 때 결제 메뉴

    elif select_num == '2':
        gmanagement.main(goods)
    # 2번 선택하였을 때 물품관리

    elif select_num == '3':
        management.main(goods, day_sale)
    # 3번 선택하였을 때 매출 관리

    elif select_num == '9':
        ep.main(goods, day_sale)
        break
    # 9번 선택할 때 종료하기전에 메모리에 있는 정보를 텍스트 파일로 저장하기.

    else:
        print("번호를 다시 선택해 주세요.\n")

    print("\nSystem down")

