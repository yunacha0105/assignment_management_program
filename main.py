from movie_management import print_menu, scan_user_input, process, ExitProgram

print('----- 영화 상영 목록 관리 -----')
while True:
    try:
        print_menu()
        num = scan_user_input()
        process(num)
    except ExitProgram as e:
        print(e)
        break
    except Exception as e:
        print(e)