import datetime as dt

time_format_date = "%Y_%m_%d"
time_format_time = "%H-%M-%S"

def menu():
    print("#"*30)
    print("1. 기록")
    print("2. 출력")
    print("3. 종료")
    print("#"*30)
    user_select = int(input())
    return user_select

while True:
    menu_select = menu()
    if menu_select == 1:
        pass
    elif menu_select == 7:
        print("프로그램을 종료합니다.")
        break