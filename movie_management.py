from movie import Movie

movie_list = []

#  print menu
def print_menu():
    print('----- menu -----')
    print('''0. 프로그램 종료
1. 영화 등록
2. 영화 목록
3. 영화 조회
4. 목록 수정       
5. 영화 삭제''')

class ExitProgram(Exception):
    pass
# scan user input
def scan_user_input():
    try:
        return int(input('메뉴 번호: '))
    except ValueError:
        return -1

# process
def process(num):
    match num:
        case 0:
            raise ExitProgram('프로그램을 종료합니다.')
        case 1:
            enroll_movies()
        case 2:
            select_movie_list()
        case 3:
            select_movie_one()
        case 4:
            modify_movie()
        case 5:
            remove_movie()
        case _:
            print('잘못 입력하셨습니다.')


# 등록
def enroll_movies():
    print('----- 영화 등록 -----')
    t = input('제목: ')
    d = input('주연: ')
    g = input('장르: ')
    y = input('개봉연도: ')
    movie = Movie(t, d, g, y)
    movie_list.append(movie)
    print('영화 등록 완료 !')

# 목록 조회
def select_movie_list():
    print('----- 영화 목록 -----')
    for idx, movie in enumerate(movie_list):
        print(f'{idx+1}. {movie.title}')


# 상세조회
def select_movie_one():
    print('----- 영화 상세 정보 -----')
    num = int(input('조회 하고 싶은 영화 번호: '))
    movie = movie_list[num-1]
    print(movie)

# 수정
def modify_movie():
    print('----- 목록 수정 -----')
    num = int(input('수정하고 싶은 영화 번호: '))
    movie = movie_list[num-1]
    print(movie)

    t = input(f'제목 ({movie.title}): ') or movie.title
    d = input(f'감독 ({movie.actor}): ') or movie.actor
    g = input(f'장르 ({movie.genre}): ') or movie.genre
    y = input(f'개봉연도 ({movie.year}): ') or movie.year

    movie_list[num-1] = Movie(t, d, g, y)
    print('수정 완료 !')

#삭제
def remove_movie():
    print('----- 영화 삭제 -----')
    num = int(input('삭제하고 싶은 영화 번호: '))
    del movie_list[num-1]
    print('삭제 완료 !')