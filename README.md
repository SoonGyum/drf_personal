**[POST]유저회원가입**:
username, password, name, nickname, email, birthday, gender 모두 입력 받아 user생성.
![image](https://github.com/user-attachments/assets/757b1a3b-186e-43b2-9f00-1129d214cb13)
<br><br>
**[POST]로그인 성공**:
등록된 username과 password를 이용하여 로그인.
로그인 성공시 refresh token생성.
![image](https://github.com/user-attachments/assets/d96ce65a-dba0-4ae4-acea-dfd246e12f45)
<br><br>
**[POST]로그인 실패**:
잘못된 username이나 password를 입력.

![image](https://github.com/user-attachments/assets/99594775-395b-4f10-a2c9-e8d6d8c4bcc1)
<br><br>
**[GET]유저 프로필**:
1)로그인 시 생성되는 refresh token을 이용하여 access token을 발급받음.
2)권한을 확인받기 위해 access token을 Authorization -> Bearer Token 값에 입력.

![image](https://github.com/user-attachments/assets/6e0ff5f1-2515-4f7b-a3a0-05732df9cf18)

**[GET]상품 목록조회**:
1)로그인 시 생성되는 refresh token을 이용하여 access token을 발급받음.
2)권한을 확인받기 위해 access token을 Authorization -> Bearer Token 값에 입력.
![image](https://github.com/user-attachments/assets/72203643-b7f8-41ad-a04b-4eaecb64729d)
