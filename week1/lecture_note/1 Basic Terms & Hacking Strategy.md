# 1. Basic Terms & Hacking Strategy

- 설명을 아래 두 개로 나눠서 생각하자!
    - 받아들일 개념
    - 이해할 개념

## 1. web이란 무엇인가?

- Network
    - 컴퓨터와 link의 집합
- Web, WWW(World Wide Web)이란
    - Network의  Network 즉, 네트워크끼리 연결된 intranet, internet이다.
    - 정보 공유
    - 하이퍼 텍스트로 연결하여 제공
        - 문서 내부에 하이퍼 링크를 넣을 수 있는 문서를 의미
        - 하이퍼 링크 : 문서로 연결되는 참조
- 연결된 것은 알겠다. 그런데…
    - 어떻게 연결되어 있지?
        - WIFI, Bluetooth, 랜선 등등
        - 다루지 않을 예정
    - 어떻게 통신을 하지?
        - HTTP(S) 프로토콜!
    - 누가 웹 서핑을 할 수 있게 해주지?
        - Server, Client

## 2. 서버와 클라이언트

- 클라이언트 : 데이터를 받는 친구들, front-end
    - Chrome 등 웹 브라우저에서 동작
    - HTML, Javascript, CSS 등을 받아서 우리들에게 출력해줌.
        1. HTML(HyperText Markup Language)
            - 태그를 사용하여 정보를 쓴 파일에 구조를 제공
            - attribution 등을 이용하여 JS와 연계해 다양한 내용 처리
        2. JS
            - 사용자의 행동에 따라 연산처리
            - 페이지가 움직이거나 하는 동적인 역할 담당
            - programming language
        3. CSS
            - Casacading Style Sheets
            - 꾸미는 것
            - 왜 배우냐? 얘도 악용할 수 있으니까…
- 서버 : 데이터를 제공해주는 친구들, back-end
    - 특정 컴퓨터(들)에서 동작
    - 우리가 볼 웹 페이지(HTML, Javascript, CSS)를 만들어서 줌.
    - 데이터를 저장 및 관리

### 2.1 HTML

- 구성요소
    - Tag : 다양한 구조 정보 제공
        - 이미지나 JS 등 다른 요소를 넣을 때에도 사용
        - 여는 태그와 닫는 태그가 한 세트, 혼자서 사용되는 태그도 존재 (ex) <br>)
    - Attribute : 추가 정보 제공
    - Element : Tag 안에 있는 텍스트
- 주요 태그
    - a태그
        - <a href=””>
        - hyperlink reference : hyperlink 주소를 써준다.
    - img 태그
        - <img src=”” alt=””>
        - src : 이미지의 주소나 파일 경로
    - html 태그
        - 
    - meta 태그
        - 
    - script 태그
        - Javascript를 넣어 작성, 실행할 수 있게 해주는 태그
        - 태그 안의 문자들은 JS 언어로 간주된다.
    - style 태그
        - CSS를 넣어 디자인 요소를 작성하는 태그
        - 태그 안의 문자들은 CSS 언어로 간주된다.
    - frame류 태그
        - 외부 자료(url 경로가 다른 자료)를 넣는 데 용이
        - frame, frameset, iframe, object 등등
    - form 태그
        - post method 형식을 만들어주는 태그
        - 안에 input tag, submit tag 등을 활용하여 태그를 만든다.
- 이스케이프 문자
    - **&lt;**: 작은 부등호 기호(**<**)
    - **&gt;**: 큰 부등호 기호(**>**)
    - **&amp;**: 앰퍼샌드 기호(**&**)
    - **&quot;**: 쌍따옴표(**"**)
    - **&apos;**: 따옴표(**'**)

### 2.2 JS

- 코드 선언
    - 기본적으로 자료형을 사용하지 않음.
        
        ```jsx
        let v1 = 1;
        var v2 = "test";
        const v3 = 0.4;
        ```
        
    - function의 두 가지 선언 방식
        1.  function 예약어 사용
            
            ```jsx
            function func1 (var1, var2) {
            	return 1;
            }
            ```
            
        2. 변수(상수)에 할당, 화살표 함수라고도 함
            
            ```jsx
            const func1 = (var1, var2) => {
            	return 1;
            }
            ```
            
- 동기 / 비동기
    - JS는 기본적으로 코드를 순서대로 실행하지 않는다.(비동기)
    - 병렬 처리를 통해 속도를 올리는 것
    - 오래 걸리는 작업이 있으면 그 작업을 하는 동안 다른 작업을 수행
        - 예상치 못한 결과가 나오기도 함.

### 2.3 CSS

- Selector와 Declaration list가 대응
    
    ```css
    h1 { 
    	color: blue;
    	font-size: 20px;
    }
    ```
    
    - Declaration은 Property와 value로 구성
    - color가 property, blue가 value.
    - selector에는 id, class 등을 활용할 수 있다.

### 2.4 Framework

- Front-end나 Back-end를 개발할 때 더 쉽게, 규칙을 지켜서 만들 수 있도록 도와주는 도구
- front-end의 경우 react, tailwind css**,** angular, vue.js, bootstrap같은 프레임워크가 존재
- back-end의 경우 express, next.js, flask, django, springboot, go 등의 프레임워크가 존재
    - php같은 자체로 backend를 위한 언어도 존재 (php에도 프레임 워크가 존재)
- 너무나 다양한 framework가 존재하고, 생기고, 사라지고 있기 때문에
    1. 공통적으로 사용하는 기능
    2. 무엇이 다른지
    3. 프로그래밍 언어를 익히는 속도를 빠르게
    - 해주면 좋다.
- 주로 쓸 것은 Flask

### 2.5 DB

- Database
    - 정보를 효율적으로 저장 및 가져오기 위한 도구
- Type
    - SQL
        - 관계형 DB : table 형태로 row, column을 통해 데이터 관리
        - MySQL, SQLite, MS SQL, Postgre SQL
    - NoSQL
        - 비 관계형 DB : Table처럼 구조화되지 않아 유연하게 데이터를 저장
            - 문서, 키-값, 와이드 칼럼, 그래프 등의 다양한 구조가 저장될 수 있음
        - mongo DB, Redis

## 3. 관련 지식

- HTTP, cookie, session 등

### 3.1 URL Structures

- URL : Uniform Resource Locator
    - Resource(문서 등)을 어디에 요청하는지 표시해주는 도구
- structure
    - scheme
        - request 요청을 어떤 방식으로 보낼 것인가?
        - http, https, files 등등
    - domain name
        - 특정 IP 주소로 연결해주는 이름
    - port
        - IP 주소에서 어떤 Process에 연결할지 정해주는 주소
        - 우리가 사용하는 웹 브라우저도 각각의 port를 가진다.
    - path(이하 endpoint)
        - 그 IP에서 요청할 file
    - params
        - dictionary 형태의 추가 정보
    - anchor(fragment; 이하 hash)
        - string 형태의 추가 정보
        - 숫자로 페이지를 나타내거나 하는 형식
- + URI / URN / URL
    - URI는 web3, blockchain, NFT 공부하다 보면 사용하게 될 수도 있음.

### 3.2 HTTP(S)

- HyperText Transfer Protocol
    - HTML같은 문서를 가져오기 위한 프로토콜이다.
    - 요청 - 응답 구조
        - 요청 : Request
            - 클라이언트가, 이 파일을 내놔라
        - 응답 : Response
            - 서버가, ㅇㅋ 줌
    - 작동 순서
        1. TCP 연결
        2. 요청
            - Method : 어떤 형식의 요청인가?
                - GET, POST, DELETE, OPTIONS, HEAD
            - Path
                - /~~~ 하는 endpoint
            - Version
            - Headers
                - Host 등등의 정보
            - 기타 Data
        3. 응답
            - Status : 어떤 형식의 응답인가?
            - Header
    - Stateless : 이전 request의 정보를 알 수 없다. (연결되어 request를 보내주지 않는다.)
        - 이를 위해 쿠키를 활용 (request를 보낼 때마다 같이 보내져 Stateful한 서비스 제공)

### 3.3 쿠키와 세션

- 쿠키
    - 요청을 보낼 때마다 항상 같이 보내주는 값으로,
    - key:value인 딕셔너리 형식으로 구성됨
- 세션
    - login 정보를 유지해서 Stateful한 서비스를 제공하기 위한 기능
    - key는 주로 session, sess 등을 사용
    - value에 random hex string을 줌
    - 작동 방식
        1. 서버 session storage에 user identifier와 session을 저장
        2. 서버 측에서 클라이언트에 session 값을 쿠키로 등록
        3. 클라이언트가 요청할 때 session 값 획득
        4. session 값을 통해 session storage를 활용해 user임을 인식
    - expiration(만료 기간)
        - session 만료 기간을 정해줘야 함.

### 3.4 Python Request Module

- python의 module로, 웹에 request를 할 수 있다.
    - brute force를 진행할 때 자동으로 request를 보내는 방식이 가능하다.
- install
    
    ```bash
    pip install requests
    ```
    
- import
    
    ```python
    import requests
    ```
    
- get method
    
    ```python
    requests.get("http://www.url.com", params={"key":"value"})
    ```
    
- post method & cookie
    
    ```python
    
    url = "http://localhost:5000"
    cookies = {
        "key":"value"
    }
    data = {
        "key":"value"
    }
    response = requests.post(url=url, data=data, cookies=cookies)
    print(response.text)
    ```
    

## 4. Web Hacking

### term about hacking

- weakness
- vulnerability
    - weakness + available + exploitable
- exploit code를 작성해라 → 해당 시나리오에 성공하도록 하는 코드를 작성해라

### web hacking이란?

- 웹에서 이루어지는 해킹
- 웹의 대중화, 정보의 집중화, 금전적 가치가 존재
    - 해킹을 시도하는 공격자가 늘고 있다.
- 웹 해킹의 대상은
    1. 서버와
    2. 클라이언트

### Strategy

1. 정보 얻기
    - 서버 or 클라이언트의 구조를 이해한다.
        - 프론트엔드와 백엔드가 어떻게 연결되어 있는가
        - 웹 서버는 또 어떻게 연결되어 있는가
        - 주요 구성 대상 :
            1. 클라이언트
            2. 서버
                - apache, nginx 등 캐싱, 로드밸런싱 기능을 제공해주는 친구들
                - ex) apache의 .htaccess 기능을 활용한 exploit
            3. 앱 서버
                - next.js, Flask 등 프레임워크로 프로그래밍을 통해 내부 정보 처리 구조를 구성하는 친구들
            4. DB 
    - 정보를 수집한다.
        - 방법들 :
            1. 서버 정보
            2. 스캐닝
            3. 인증
            4. 분석
        - 운영체제, Open port, 서비스의 버전 등등
    - 위의 내용을 목록화하여 정리한다.
        - 인증 수준, 앱 프로세스, 디렉터리, 토큰에 대한 정보를 수집
        - 정말로 쓰면 좋고, 최소한 머리에라도 (CTF 관점에서는 앱이 너무 크지 않으면 머리로 기억해도 크게 문제 없었다.) 넣어두고 생각하기
2. 공격 경로 파악
    - 취약점 분석
    - 공격 목적에 따른 공격 시나리오 구성
3. 가장 가능성 있는 경로부터 공격 시작
    - 공격 시도 (exploit 기법 활용)
    - 공격 결과 분석
        - 한 번에 성공하지 못한 경우
        - 실패한 원인을 찾아보기
            - 이것 또한 정보 수집이다!
            - 같은 공격 시나리오에서 기법만 조금 수정할지,
            - 다른 공격 시나리오로 넘어갈 지 고민하기

### 정보 수집 방법

1. 포트 스캐닝
    - nmap을 활용한 포트 스캐닝
2. 웹 스캐닝
    - 다양한 도구들
    - sql injection을 테스트한다던가,
3. 인증 정보
    - cookie를 사용하는지, session을 사용하는지, 이게 취약하진 않은지
4. 지원 파일
    - 어떤 파일 확장자 사용하는지, 어떤 파일 .py, .js, .php 등 사용하는지
5. 디렉터리 / 파일 목록화
    - 내가 공격에 쓸 수 있을 것 같은 공격 대상들 목록화
    - admin 디렉터리가 있다면 그 곳을 타겟으로 삼는 등
    - wget -r을 통해 전체 웹 애플리케이션의 디렉터리 구조와 파일 복사가 가능한 경우
    - curl의 regex 활용
        - regex란 ? 정규 표현식으로, 문자열이 원하는 대상인지 확인할 수 있는 방법 중에 하나
6. get / post params 목록화
7. 파일 처리 기능의 존재 여부
    - file을 upload하여 해당 파일을 통해 exploit 하는 등
8. 주석 확인

### 취약점 분석

- 알려진 취약점 확인 (구글링)
- 오류 유도를 통해 추가 정보 획득

## 5. Flask

- Python의 backend 모듈
- jinja2라는 template engine 사용
- 설치 방법
    
    ```bash
    pip install Flask
    ```
    
- 사용 방법(basic)
    
    ```python
    from flask import Flask
    import os
    
    app = Flask(__name__)
    app.secret_key = os.urandom(32)
    
    @app.route("/")
    def index():
        return "my_web"
    
    app.run()
    ```
    
    - app을 Flask로 지정
    - app에서 route되는 지점(endpoint)에 함수를 설정해줌
        - @는 wrapper라는 기능으로, 함수 위에 쓰여서, 아래에 있는 함수에서 기존에 해줘야 할 세팅, 변수 선언 등을 미리 사용할 수 있게 짜둔 또 다른 함수
    - 이렇게 만들어진 index에서 return 값으로 html 문서를 주게 됨
    - app.run()으로 서버 실행 시작
- method && render_template()
    
    ```python
    from flask import Flask, request, render_template, make_response
    import os
    
    app = Flask(__name__)
    app.secret_key = os.urandom(32)
    
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            return render_template('index.html')
        if request.method == "POST":
            return "POST!"
        return "Unused method!", 404 # status code
    ```
    
    - endpoint 말고도 method를 지정해줄 수 있다.
    - if문으로 method가 맞는지 확인, 그에 따라 다른 값을 보여줄 수 있다.
    - render_template은 templates 폴더에 있는 외부 파일을 가져온다.
- cookie
    
    ```python
    @app.route("/test")
    def test():
        cookie = request.cookies.get('test_cookie')
        
        # quiz! 왜 \n을 썼는데 web에서 개행이 되지 않았을까요?
        response = make_response(f"set cookie! \n this is your cookie : {cookie}")
        response.set_cookie('test_cookie', 'I_love_cookies!')
        return response
    
    app.run(host="0.0.0.0", port=5000)
    ```