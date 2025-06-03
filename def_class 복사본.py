import re # 정규식 표현 모듈
import pwinput # 비밀번호를 * 처리하기위한 라이브러리

# 전역변수
user_db = {} # 회원가입 아이디,패스워드 저장용

# 아이디 정규식
def valid_id(user_id): # 함수가 호출될때 매개변수 즉, user_id에 사용자 입력한 id가 함수 안으로 들어옴
    return bool(re.match(r'[A-Za-z0-9]{9,}', user_id)) # return 함수 실행 결과를 밖으로 반환 / bool로 묶어 True,False판별 / re.match 문자열이 '처음부터' 패턴에 맞는지 검사 / r'[A-Za-z0-9]{9,}' 영문 대소문자, 숫자를 포함해서 9개 이상
                                 #패턴          문자열

# 비밀번호 정규식
def valid_pw(user_pw): # 함수가 호출될때 매개변수 즉, user_pw에 사용자 입력한 pw가 함수 안으로 들어옴
    return ( # 함수 실행 결과를 밖으로 반환
        len(user_pw) >= 8 and # 사용자가 입력한 pw길이가 8자리 이상이어야 하고,
        re.search(r'[A-Za-z]', user_pw) and # user_pw에 영문 패턴이 포함되고,
        re.search(r'[0-9]', user_pw) and # 숫자 패턴이 포함되고,
        re.search(r'[!@#$%^&*(),.?":{}|<>]', user_pw) # 특수기호가 포함되어야 가능
    )
'''
re.match()와 re.search()의 차이점
match는 특정 패턴으로 시작해야 할 때 사용
search는 특정 패턴이 포함되기만 해도 될 때 사용
'''

# 회원가입 툴
def signup():
    print("##### 회원가입 페이지 #####") # 현재 페이지 출력
    new_id = input("ID를 입력하세요: ") # 회원가입 할 새로운 id 입력
    if not valid_id(new_id): # 조건문 입력한 id가 valid_id 정규표현식 조건에 맞지 않을때
        print("❌ ID는 영문, 숫자를 포함해서 9자리 이상이어야 합니다.") # 문구 출력
        return
    
    if new_id in user_db: # 입력한 id가 전역변수 user_db에 저장된 값일때
        print("❌ 이미 존재하는 ID입니다.") # 문구 출력
        return
    
    new_pw = pwinput.pwinput("비밀번호를 입력하세요: ") # 입력할 비밀번호가 * 처리되기 위해서 pwinput.pwinput사용
    re_pw = pwinput.pwinput("비밀번호를 다시 입력하세요: ") # //
    if new_pw != re_pw: # 입력한 비밀번호와 재입력한 비밀번호와 다르면
        print("❌ 입력한 비밀번호가 서로 다릅니다.")
        return
    
    if not valid_pw(new_pw): # 입력한 비밀번호가 valid_pw 정규표현식 조건에 맞지 않을때
        print("❌ 비밀번호는 영문, 숫자, 특수기호를 포함해서 8자리 이상이어야 합니다.")
        return
    
    user_db[new_id] = new_pw # 전역변수 user_db{} 에 저장하기 위해 
    print("✅ 회원가입이 완료되었습니다!!!!")

# 로그인 툴 
def login():
    print("##### 로그인 페이지 #####") # 현재 페이지 출력
    user_id = input("ID를 입력하세요: ") # 사용자 id 입력
    user_pw = pwinput.pwinput("비밀번호를 입력하세요: ") # 사용자 비밀번호 *으로 입력
    if user_id in user_db and user_db[user_id] == user_pw: # user_id가 user_db에 저장되어있으며, 키와 벨류가 일치할 때
        print("✅ 로그인 성공!!!!")   
    else:
        print("❌ ID 또는 비밀번호가 잘못되었습니다.")

# 메인모드
def main():
    check_mode = ["로그인", "회원가입", "종료"] # 모드 변수 설정
    while True: # 종료 전까지 실행되어야 하므로 반복문 실행
        mode = input("로그인, 회원가입, 종료 : ") # 모드 선택 입력

        if mode not in check_mode: # 모드 입력값이 체크모드에 없을 때
            print("❌ 잘못된 모드입니다.")
        elif mode == "종료": # 종료 선택 시
            print("👋 프로그램을 종료합니다.")
            break # 반복문 종료
        elif mode == "회원가입": # 회원가입 선택 시
            signup() # def signup() 함수 호출
        elif mode == "로그인": # 로그인 선택 시
            login() # def signup() 함수 호출

if __name__ == "__main__": # 직접 실행할 때
    main() # 메인 함수 호출