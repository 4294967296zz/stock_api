# Stock_API ( 개발중.. )

대신증권 OPEN API를 활용한 주식 API를 개발!

Develop Restful API with open API provided by Daishin Securities!

***

## [ 개발환경 ]

> Windows 10 64bit

> Python 3.5 ( Anaconda ) with FLASK



## [ 제공 데이터 ]


종목코드로 주식 기본정보 조회


 - 제공 데이터 : 종목명, 현재 주가, 현재 시간
 
 - end point : url~/data
 
 - 필요 파라미터 : 종목코드(code)
 
 - 종목코드로 조회하여 json 형식으로 데이터 제공.
 
 - ex) http://test.url/data?code=A000030
 

주식시장별 주식종목 리스팅


 - 제공 데이터 : 종목코드, 종목명, 현재 주가
 
 - end point : url~/codelist
 
 - 필요 파라미터 : 주식 시장명(market)
 
 - 시장명으로 해당 주식시장의 모든 종목을 리스팅하여 json 형식으로 데이터 제공.
 
 - ex) http://test.url/codelist?market=11
 
 
 ## [ 진행 사항 ]
 
 모듈에 app.route 지정하고, 필수값 지정하여 데이터 조회 후 json 으로 변환하여 return.
 
 Create new paths and end points with needed parameters by adding module's "app.route". Any data can be retrieved from OPEN API by parameters . When it hits end point with needed parameter, returns retrieve data after converting to json.
 Trying to add validation to check the datas while receiving parameters. 
 

