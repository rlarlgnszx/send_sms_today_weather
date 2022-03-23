# send_sms_today_weather
파이썬 : twilio &amp; Linux_Server : crontab 을 이용한 나한테 문자로 하루하루 날씨 아침마다 알려주기!

<ul><h1>설계</h1>
 <div>-> <h2>1단계 파이썬으로 네이버날씨 혹은 기상청 크롤링<h2></div>
    <li>현재온도 : </li>
    <li>*강수확률 :</li>
    <li>*바람 :</li>
    <li>*미세먼지 :</li>
 <li>*초미세먼지 :</li>
 <li>*습도 :  </li>  => 총 7가지 크롤링 
 <div></div>
    네이버를 크롤링해서 7가지만 json파일로 만들어줌 
  <div></div>
 </ul>
  <ul>
 <div>-> <h2>2단계 : 파이썬 문자 자동으로 보내는 MODULE 선택 :</h2></div>
 <li>-> twilio 선택했다. 다른 것들은 비용이 더 들어서,,,,거지........(무료는 자기핸드폰만 이용가능)</li>
 <li>-> pip3 install twilio</li>
 <li>-> 그후에 twilio 가입후 auth_token과 account_sid 가져옴</li>
 <li> -> 코드 작성후 네이버에서 크롤링한 Json파일 나한테 보내기 => 실패 -> 첫번째 키만 가져옴</li>
 <li>-> Json파일 String으로 변환후 원하는 방식으로 보내기</li>
      EX)<img src=https://user-images.githubusercontent.com/40743105/159710416-7a025098-dfc7-404b-b8b4-fb0cef716dac.png 
               width="450" height="800">
  <div>이렇게 오는것 예시</div>
</ul>
  <ul><div>-> <h2>3단계 : 문자보내고 파일을 서버에 올리고 서버시간판단으로 파일실행시키기 :</h2></div>
   <li>->서버는 아마존서버랑 네이버서버등등이 있지만 아마존서버는 예전에 써서 네이버서버로 실행</li>
   <li>->네이버 클라우드플랫폼 가입후 1년무료 이용 서버 생성후 외부접속 IP랑 키얻고 Port는 직접 설정에서 열어줘야한다</li>
   <li>->Linux 서버 구동후 linux crontab 이란 시간관리 프로그램이 linux시스템에 기본베이스로 깔려있어 crontlab으로 6:30 12:30 18:30 24:30주기로 프로그램실행할수 있게 설정</li>
   <li><h5>서버 시간 한국시간으로 바꿔주는 것 잊지말기</h5></li>
   
   
 
   끝!!
   
   
