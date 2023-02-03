# 모듈 확인
print(f"code29_module_name : {__name__}") # __name__(entry point) 프로그램이 시작하는 진입점. 지금 현재 실행 이름을 알려줌

# C int main(void) 동일
if __name__ == '__main__':
    print('main을 실행합니다.') # code29에서 실행하면 여기는 실행이 되지 않음
