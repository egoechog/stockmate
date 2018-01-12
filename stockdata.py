###############################################################################
# This python3 script pulls stock data by using the 'tushare' package

# 'tushare' depends on the following dependant pacakges
#pip install pandas
#pip install lxml
#pip install requests
#pip install bs4
#pip install tushare
###############################################################################

from datetime import datetime
import tushare as ts

def getYearlyCloseData(stockNum):
    """
    股票收盘价走势曲线Over a year

    stockNum is the stock number in string type
    """
    end = datetime.today() #开始时间结束时间，选取最近一年的数据
    start = datetime(end.year-1,end.month,end.day)
    end = str(end)[0:10]
    start = str(start)[0:10]
    stock = ts.get_hist_data(stockNum,start,end)#选取一支股票
    return stock['close']


def getMovingAverageData(stockNum):
    """
    显示股票5日均线、10日均线以及20日均线(Moving average)

    stockNum is the stock number in string type
    """
    end = datetime.today() #开始时间结束时间，选取最近一年的数据
    start = datetime(end.year-1,end.month,end.day)
    end = str(end)[0:10]
    start = str(start)[0:10]
    stock = ts.get_hist_data(stockNum,start,end)#选取一支股票
    # difference
    return stock[['close','ma5','ma10','ma20']]

def getDailyReturnData(stockNum):
    """
    显示股票每日涨跌幅度(Daily return)

    stockNum is the stock number in string type
    """
    end = datetime.today() #开始时间结束时间，选取最近一年的数据
    start = datetime(end.year-1,end.month,end.day)
    end = str(end)[0:10]
    start = str(start)[0:10]
    stock = ts.get_hist_data(stockNum,start,end)#选取一支股票

    stock['Daily Return'] = stock['close'].pct_change()
    return stock['Daily Return']
