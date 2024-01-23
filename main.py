import datetime as dt
import os
import math

time_format_date = "%Y_%m_%d"
time_format_time = "%H-%M-%S"


def first_menu(): # 최상단 메뉴 메뉴 선택후 각 메뉴 번호 int 리턴
    while True:
        try:
            print("#"*30)
            print("1. 기록")
            print("2. 출력")
            print("3. 종료")
            print("#"*30)
            user_select = int(input())
            return user_select
        except:
            print("숫자만 입력해주세요")

def second_menu(): # 기록선택 -> 메뉴 선택후 각 메뉴 번호 int 리턴
    while True:
        print("#"*30)
        print("1. 업무")
        print("2. 프로그래밍")
        print("3. 공부")
        print("4. 독서")
        print("5. 극단")
        print("6. 기타")
        print("7. 취소")
        print("#"*30)
        user_select = input()
        try:
            return int(user_select) - 1
        except:
            tag_list = ["업무","프로그래밍","공부","독서","극단","기타"]
            return tag_list.index(user_select)
    

def input_data(category):
    print(category + "를 입력 중입니다.")
    print("메모입력")
    memo = input(":")
    if memo == "s" or memo == "ㄴ" or memo == "ㅜ" or memo == "n":
        print("입력을 취소합니다.")
        return
    while True:
        print("입력 종료를 원하시면 n, 아니면 계속 입력")
        temp = input(":")
        if len(temp) <= 3:
            if temp[0] !="n" and temp[0] !='ㅜ' and temp[0] != 'ㄴ' and temp[0] != 's':
                memo = memo.strip() + "," + temp.strip()
            else:
                print("입력을 종료합니다.")
                return category + "|" + memo
        else:
            memo = memo.strip() + "," + temp.strip()
        
def write_data(s_time, e_time, text):
    if text == None:
        return
    file_name = dt.datetime.strftime(dt.datetime.now(), time_format_date) + ".txt"
    if os.path.isfile(f'result/{file_name}'):
        with open(f"result/{file_name}", 'a', encoding='utf8') as f:
            f.write(f"{s_time}|{e_time}|{text}\n")
    else:
        with open(f"result/{file_name}", 'w', encoding='utf8') as f:
            f.write(f"{s_time}|{e_time}|{text}\n")

def total_data(target_dict, file_name):
    with open(f"result/{file_name}", 'a', encoding='utf8') as f:
        f.write("\n\n\n계\n")
        for k,v in target_dict.items():        
            hours = v // 3600
            v = v - (hours * 3600)
            minu = v // 60
            v = v - (minu * 60)
            f.write(f"{k} : {math.floor(hours)}h {math.floor(minu)}m {round(v)}s\n")

def print_all(lists, target_date=""):
    if target_date == "":
        file_name = dt.datetime.strftime(dt.datetime.now(), time_format_date) + ".txt"
    else:
        file_name = target_date.replace("-","_") + ".txt"
    data = {}
    for i in lists: # 딕셔너리 초기화
        data[i] =  0
    with open(f"result/{file_name}", 'r', encoding='utf8') as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            line = line.split("|")
            s_time = dt.datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S.%f")
            e_time = dt.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S.%f")
            elapsed_time = (e_time - s_time).total_seconds()
            data[line[2]] += elapsed_time
    total_data(data, file_name)

def make_time_line(target_date = ""):
    if target_date == "":
        file_name = dt.datetime.strftime(dt.datetime.now(), time_format_date) + ".txt"
    else:
        file_name = target_date.replace("-","_") + ".txt"

    stor = []
    target = []
    with open(f"result/{file_name}", 'r', encoding='utf8') as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            line = line.split("|")
            stor.append(line)
            if line[2] not in target:
                target.append(line[2])
    with open(f"result/{file_name}", 'a', encoding='utf8') as f:
        f.write("\n\n\n태그별 타임라인 정리\n")
        for i in target:
            f.write(f"{i}\n")
            for j in stor:
                if j[2] == i:
                    f.write(f"{j[0][11:19]}|{j[1][11:19]}|{j[3]}\n")
            f.write("\n\n")
            

        
tag_list = ["업무","프로그래밍","공부","독서","극단","기타"]
while True:
    menu_select = first_menu()
    if menu_select == 1: # 사용자 기록 선택 
        start_time = dt.datetime.now()  # 기록 시작하는 시간 저장
        try:
            menu_select = int(second_menu()) # 두 번째 메뉴 함수 실행
            if menu_select != 7: # 업무 선택
                data_for_wirte = input_data(tag_list[menu_select])
                end_time = dt.datetime.now()
                write_data(start_time, end_time, data_for_wirte)
            else:
                print("기록 입력을 취소하셨습니다.")
        except:
            print("잘못 입력하셨습니다.")
    elif menu_select == 2: # 사용자 출력 선택 - 현재 날짜로 result 폴더에 저장
        check_date = input(f"결과를 출력할 날짜를 입력해주세요.(미입력시 오늘)")
        if check_date == "":
            print_all(tag_list)
            make_time_line()
        else:
            print_all(tag_list, check_date)
            make_time_line(check_date)
    elif menu_select == 3: # 프로그램 종료
        print("프로그램을 종료합니다.")
        break