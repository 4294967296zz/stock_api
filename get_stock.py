from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!';

@app.route('/data', methods=["GET", "POST"])

def get_data():
    import win32com.client
    import json

    connect_check = win32com.client.Dispatch("CpUtil.CpCybos")
    connect_chk = connect_check.IsConnect
    if (connect_chk == 0):
            print("Plus 통신 오류입니다. 연결을 확인하세요.")
            exit()

    code = request.args.get('code')
            
    StockMst_obj = win32com.client.Dispatch("DsCbo1.StockMst")
    StockMst_obj.SetInputValue(0, code)
    StockMst_obj.BlockRequest()

    name = StockMst_obj.GetHeaderValue(1)
    time = StockMst_obj.GetHeaderValue(4)
    cur_juka = StockMst_obj.GetHeaderValue(11)

    stock_info = {'code':code, 'name':name, 'juka':cur_juka, 'time':time}
    return json.dumps(stock_info)

@app.route('/codelist', methods=["GET", "POST"])

def get_code_list():
    import win32com.client
    import json

    market = request.args.get('market')

    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codeList = instCpCodeMgr.GetStockListByMarket(market)

    kospi = {}
    
    for i, code in enumerate(codeList):
        name = instCpCodeMgr.CodeToName(code)
        stdPrice = instCpCodeMgr.GetStockStdPrice(code)
        kospi[i] = "code : {}, name: {}, price: {}".format(code,name,stdPrice)

    return json.dumps(kospi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
