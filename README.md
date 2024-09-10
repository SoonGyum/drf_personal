**DRF 개인과제**<br><br><br>
**주제** :<br> DRF를 이용하여 기능 구현 후 POSTMAN에서 데이터 확인  <br><br><br>
- - -
개발환경 : PyCharm <br>
Framework : Django-Rest-Framework <br>
Database : Sqlite3<br>
- - -
**주요 기능**: 



**[POST]유저회원가입**:<br>
 - username, password, name, nickname, email, birthday, gender 모두 입력하여 user생성.<br>
![image](https://github.com/user-attachments/assets/757b1a3b-186e-43b2-9f00-1129d214cb13)
- - -
<br><br>
**[POST]로그인 성공**:<br>
1)등록된 username과 password를 이용하여 로그인.<br>
1-1)로그인 성공시 refresh token생성.<br>
![image](https://github.com/user-attachments/assets/d96ce65a-dba0-4ae4-acea-dfd246e12f45)
- - -
<br><br>
**[POST]로그인 실패**:<br>
 - 잘못된 username이나 password를 입력.<br>

![image](https://github.com/user-attachments/assets/99594775-395b-4f10-a2c9-e8d6d8c4bcc1)
- - -
<br>
<br>

**[GET]유저 프로필** :
<br>
1)로그인 시 생성되는 refresh token을 이용하여 access token을 발급받음.<br>
2)권한을 확인받기 위해 access token을 Authorization -> Bearer Token 값에 입력.<br>

![image](https://github.com/user-attachments/assets/6e0ff5f1-2515-4f7b-a3a0-05732df9cf18)


**[GET]상품 목록조회**:<br>
 - 로그인 불필요(=권한 필요없음). <br>
![image](https://github.com/user-attachments/assets/cde7e2e6-1a3c-4e5d-b986-14182fdb4b1d)

- - -
<br>
<br>

**[GET]상품 상세조회**:<br>
 - 로그인 불필요(=권한 필요없음).<br>
 ![image](https://github.com/user-attachments/assets/517c3668-7671-489f-aee2-5b04fd8b1f88)

- - -
<br>
<br>

**[POST]상품 등록**: <br>
1)로그인 시 생성되는 refresh token을 이용하여 access token을 발급받음.<br>
2)권한을 확인받기 위해 access token을 Authorization -> Bearer Token 값에 입력.<br>
3)Body로 가서 title, description, username, image(optional) 입력 후 생성<br>
![image](https://github.com/user-attachments/assets/f99c95c6-6545-4388-9683-47ec2a196d31)
 
 - - -
<br>
<br>

**[PUT]상품 수정**: <br>
1)로그인 시 생성되는 refresh token을 이용하여 access token을 발급받음.<br>
2)권한을 확인받기 위해 access token을 Authorization -> Bearer Token 값에 입력.<br>
3)수정하려는 product의 pk를 이용하여 이동 ex) api/products/2/
4)Body로 가서 title, description, image(optional) 입력 후 수정<br>
![image](https://github.com/user-attachments/assets/b9473f49-8770-4cd2-ac77-6cab49d07c0b)

 - - -
<br>
<br>

**[DELETE]상품 삭제**: <br>
1)로그인 시 생성되는 refresh token을 이용하여 access token을 발급받음.<br>
2)권한을 확인받기 위해 access token을 Authorization -> Bearer Token 값에 입력.<br>
3)삭제하려는 product의 pk를 이용하여 이동 ex) api/products/2/ <br>

![image](https://github.com/user-attachments/assets/a5bc9a08-0b74-4b06-9857-fd13c47b4050)


<br>
