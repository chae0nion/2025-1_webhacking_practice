## XSS는 무엇인가?

- cross-site scripting의 약자로, 자기 자신(same-site)가 아닌 script를 실행하는 취약점
    - CSS와 이름이 겹쳐서 C대신 X를 사용함
- ‘script’, 즉 Javascript를 활용한다.
- 공격 목표
    - 해당 유저의 Data를 탈취한다.
        - 예시
            1. 쿠키를 탈취하여 세션 데이터 탈취 
                - 특히 admin 계정을 탈취하면 치명적
            2. 입력 중인 id, password를 탈취
            3. 프라이버시 침해
            4. 기타 유저 행동을 감지해서 악용할 수 있는 부분들
- JS는 어떠한 행동들을 할 수 있는가?
    - getElementBy Series
    - document.cookie
    - history

- 공격 유형(type of XSS)
    - Reflected XSS
        - 서버에 값을 요청하면서 나타나는 XSS
        - url parameter를 통해 값을 전달하면서, 이 parameter가 웹 페이지에 반영되어 javascript가 실행됨
        - 특정 user가 특정 url에 접속하면서 나타남. 광범위한 공격은 어렵지만 특정 개인에 맞춤형으로 공격을 구성하는 경우가 많음
        - 오늘 주차에서 가장 많이 볼 것
    - Stored XSS
        - 서버에 데이터가 저장됨으로써 나타나는 XSS
        - javascript data가 서버에 저장되면서 나중에 그 페이지를 불러올 때 javascript가 실행됨
        - 한 번 페이지에 업로드하면, 그 페이지에 접속하는 모든 user가 공격대상.
    - DOM-based XSS
        - DOM은 Document Objective Model의 약자로 JS HTML의 특성을 이용해 내부 logic을 바꿔 javascript가 실행됨
- 취약점 발생 이유
    - 유저 input 데이터에 대한 검증 미흡
    - 데이터와 코드가 분리되지 않음
- 공격 방법
    - 유저 데이터 중 페이지에 영향을 줄 수 있는 부분을 찾는다.
    - 코드가 실행되는지 확인
    - 원하는 데이터를 탈취할 수 있도록 코드를 작성한다.
- 공격 예제 : simple_xss
    - 공격 목표는 무엇인가?
        - 어떤 정보를 얻는 것이 목표인가?
    - 어디에 취약점이 있는가?
        - 웹 중 몇 번 줄에 존재하는가?
        - 어떤 type의 XSS인가?
    - 예제 exploit code 살펴보기
        1. script.py
            - 가장 기본적인 방법. javascript code를 실행시켜주는 <script>태그 이용
            - script 태그의 경우 javascript를 직접 태그 안에 넣어주는 방법과,
            - src=”{url}”의 형식으로 외부 혹은 자신의 사이트 혹은 파일에서 javascript 파일을 불러오는 방법이 존재한다.
        2. event_handler.py
            - HTML attribute 중에 event handler가 존재
            - event handler는 특정 유저 동작을 감지하여 특정 javascript를 실행시켜줌.
                - ex) onclick : 특정 element가 click되는 경우 attribute에 작성된 javascript 실행
        3. object.py
            - frame, embed, object 등의 태그는 페이지 안에 페이지를 삽입할 때 사용한다.
                - ex) blog 안에 들어간 youtube 동영상
            - 이 중 src, data attribute를 이용해서 javascript 실행 가능
                - 기본적으로 frame, embed, object는 안의 page에서 바깥 page에 접근할 수 없다.
                - url scheme 자체(javascript:{js code})로 실행시키는 경우 접근이 가능하며,
                - 안에 공격자 서버의 페이지를 띄우더라도 바깥 페이지의 cookie 등을 탈출하는 것은 불가능하다.
    
- mitigation
    1. sanitization, validation
        - sanitization(정화) : 특정 문자열을 없애거나
            - script 태그, frame, object, embed 태그, eventhandler 등을 제거
        - validation(검증) : 해킹 가능한 문자열일 있는지 확인하는 방식
            - script 태그, frame, object, embed 태그, eventhandler 등을 확인
    2. encode data
        - tag와 관련된 <, >과 같은 문자열을 HTML encoding을 활용하여 encode
        - <를 &lt;, >를 &gt;로 바꾸는 등
    3. use safe function
        - user input 자체를 문자열로 자동으로 취급하는 function을 이용.
    4. CSP(Content Security Policy), SOP(Same Origin Policy)
    5. HttpOnly Flag for Cookies

- 잘못된 / 부족한 mitigation bypass
    1. sanitization, validation
        - Lack_of_Validation1
        - Inappropriate_Sanitize
        - Lack_of_Validation2
    2. encode data
    3. use safe function
        - safe_renderer
    4. CSP(Content Security Policy), SOP(Same Origin Policy)
    5. HttpOnly Flag for Cookies