# 주소록 앱
# 2023-02-06(월)
# Seulyena O
# 15. 예외처리
# 15-1. 파일 없을 때 나는 예외
# 15-2. 입력 시 슬래시 개수가 다를 때의 예외
# 15-3. 메뉴번호 입력 시 숫자 외의 예외
import os # 화면 클리어를 위한 운영체제용 모듈을 불러옴

# 2. 클래스 생성
class Contact: # 상속 받을 것이 없어 괄호 쓰지 않음
    # 생성자 - 이름, 전번, 이메일, 주소
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

    # 4. __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름 : {self.__name}\n'
                   f'휴대폰 : {self.__phone_num}\n'
                   f'이메일 : {self.__email}\n'
                   f'주  소 : {self.__addr}')
        return str_res
    
    # 10. 객체 존재 여부 확인
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False

    # 12. 각 멤버변수 접근하는 함수
    # getName, getPhoneNum, getEmail, getAddr
    def getName(self) -> str:
        return self.__name
    
    def getPhoneNum(self) -> str:
        return self.__phone_num
 
    def getEmail(self):
        return self.__email
    
    def getAddr(self):
        return self.__addr

# 5. 사용자 입력
def set_contact():
    name, phone_num, email, addr = input('정보입력(이름/전화번호/이메일/주소) : ').split('/')
    # print(name, phone_num, email, addr)
    # 7. contact 객체 만들기
    contact = Contact(name, phone_num, email, addr) # name=name, email=email 이런 식으로 작성하면 순서 바꿔서 사용할 수 있음
    return contact

# 9. 주소록 출력
def get_contacts(list):
    for item in list:
        print(item) # 컨텍트 객체에서 실행하면 str 출력 됨
        print('----------')

# 10. 주소록 삭제
def del_contact(list, name):
    count = 0
    for i, item in enumerate(list): # enumerate 실행 시 입력한 값에 대한 순서를 정리해 줌
        if item.isNameExist(name):
            count += 1
            del list[i] # 리스트 삭제
    
    if count > 0: # 11. 메시지 출력
        print('삭제했습니다.')
    else:
        print('삭제할 주소록이 없습니다.')

# 13. 주소록 파일 저장
def save_contacts(list): # self x -> 클래스 아님
    file = open('C:/Source/StudyPython2023/Project/contacts.txt', 'w', encoding='utf-8')
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')
    
    file.close() # 파일 종료할 때 닫아주는 명령어

# 14. 주소록 읽어오기
def load_contacts(list):
    try:
        file = open('C:/Source/StudyPython2023/Project/contacts.txt', 'r', encoding='utf-8')
    except Exception as e:
        f = open('C:/Source/StudyPython2023/Project/contacts.txt', 'w', encoding='utf-8')
        f.close() # 15-1. (예외처리) 파일이 없어서 생기는 예외는 파일 생성 후 함수 탈출(return)함
        return

    while True:
        line = file.readline().replace('\n', '') # 15. 문장 끝에 \n 제거
        if not line: break

        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3]) # 클래스로 만든 변수 = 클래스
        list.append(contact)

    file.close()


# 추가 기능(7번 이후) / 화면 클리어를 위한 기능
def clear_console():
    command = 'clear' # Linux, Unix 화면 클리어 명령어 이름(윈도우는 cls)
    if os.name in('nt', 'dos'): # Window 운영체제라면
        command = 'cls' # 윈도우 화면 클리어 명령으로 변형

    os.system(command)

# 6. 메뉴표시
def get_menu():
    str_menu = ('주소록앱 version v0.5\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 앱 종료')
    print(str_menu)
    try:
        menu = int(input('메뉴입력 : '))
    except Exception as e: # 15-3. 숫자 외 입력 예외 처리
        menu = 0 # 영문자 혹은 특수문자를 넣으면 전부 0(값 없음)으로 처리함

    return menu

# 3. 전체 실행
def run(): # class의 함수가 아니라 self를 쓰지 않음
    contacts = list() # 앞으로 받을 모든 자료 구조를 담을 빈 리스트 생성
    load_contacts(contacts) # 14. 주소록 읽어오기
    clear_console()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1: # 8. 연락처 추가 / sel_menu가 연락처 추가라면
            clear_console()
            try:
                contact = set_contact()
                contacts.append(contact)
                input('주소록 입력 성공.') # 아무것도 받지 않는 입력 / 최초의 메뉴로 돌아가게 함(clear_console까지)
            except Exception as e: # 15-2. 연락처 입력 잘못했을 때 예외처리
                print('이름/전화번호/이메일/주소 순으로 입력해주세요.')
                input()
            finally:
                clear_console()
        elif sel_menu == 2: # 9. 연락처 출력
            clear_console()
            get_contacts(contacts)
            input('주소록 출력 완료.')
            clear_console()
        elif sel_menu == 3: # 10. 연락처 삭제
            name = input('이름입력 : ')
            del_contact(contacts, name)
            input()
            clear_console
        elif sel_menu == 4: # 13. 종료시 주소록 파일 저장
            save_contacts(contacts)
            break
        else:
            clear_console()
    # temp = Contact('오슬예나', '010-9602-5612', 'realtansan@gmail.com', '부산광역시 남구')
    # set_contact()

# 1. 메인영역
if __name__ == '__main__':
    print('주소록 앱 시작합니다.')
    run()