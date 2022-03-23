# send_sms_today_weather
파이썬 : twilio &amp; Linux_Server : crontab 을 이용한 나한테 문자로 하루하루 날씨 아침마다 알려주기!


1.설계
 -> 1단계 파이썬으로 네이버날씨 혹은 기상청 크롤링
    -현재온도 : 
    *강수확률 :
    *바람 :
    *미세먼지 :
    *초미세먼지 :
    *습도 :    => 총 7가지 크롤링 
    네이버를 크롤링해서 7가지만 json파일로 만들어줌 
 -> 2단계 : 파이썬 문자 자동으로 보내는 MODULE 선택 :
      -> twilio 선택했다. 다른 것들은 비용이 더 들어서,,,,거지........(무료는 자기핸드폰만 이용가능)
      -> pip3 install twilio
      -> 그후에 twilio 가입후 auth_token과 account_sid 가져옴
      -> 코드 작성후 네이버에서 크롤링한 Json파일 나한테 보내기 => 실패 -> 첫번째 키만 가져옴
      -> Json파일 String으로 변환후 원하는 방식으로 보내기
      EX) 
