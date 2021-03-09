#-*-coding:utf-8-*-


import clr
import datetime

clr.FindAssembly("ss_level2.dll") ## 加载c#dll文件
clr.AddReference('ss_level2')
from ss_level2 import *   # 导入命名空间

#回调函数：数据拷贝到需要的内存中进行处理，需多线程处理，全推数据量很大，py处理性能不足，需根据需要过滤或拷贝别处内存处理
'''
 /*temp_x market行情快照结构
                    temp_x[0] 000002.SZ  标准代码
                    temp_x[1] 000002 代码
                    temp_x[2] 20170101 日期
                    temp_x[3] 93000000 时间
                    temp_x[4] 状态
                    temp_x[5] 前收盘价
                    temp_x[6] 开盘价
                    temp_x[7] 最高价
                    temp_x[8] 最低价
                    temp_x[9] 最新价
                    temp_x[10]-temp_x[19] 申卖价1-10
                    temp_x[20]-temp_x[29] 申卖量1-10
                    temp_x[30]-temp_x[39] 申买价1-10
                    temp_x[40]-temp_x[49] 申买量1-10
                    temp_x[50] 成交笔数
                    temp_x[51] 成交总量
                    temp_x[52] 成交总金额
                    temp_x[53] 委托买入总量
                    temp_x[54] 委托卖出总量
                    temp_x[55] 加权平均委买价格
                    temp_x[56] 加权平均委卖价格
                    temp_x[57] 涨停价
                    temp_x[58] 跌停价                                                        
                    */
                    '''
def Market_Data(str):
    strx = str.split("#")
    for neiron in strx:
        #print(neiron)
        temp_x = neiron.split("|")
        if( temp_x[1]=="000002"):
            print(temp_x[1]+" "+temp_x[3] +" "+datetime.datetime.now().strftime('%H:%M:%S'))

            
    '''
    /*指数名称	指数代码
                      上证指数	000001
                      上证Ａ股	000002
                      上证Ｂ股	000003
                      工业指数	000004
                      商业指数	000005
                      地产指数	000006
                      公用指数	000007
                      综合事业	000008
                      上证180 	000010
                      基金指数	000011
                      国债指数	000012
                      企债指数	000013
                      上证５０	000016
                      红利指数	000015
                      沪深300 	000300*/


                    /*temp_x index行情快照结构
                    temp_x[0] 000002.SZ  标准代码
                    temp_x[1] 000002 代码
                    temp_x[2] 20170101 日期
                    temp_x[3] 93000000 时间
                    temp_x[4] 开盘指数
                    temp_x[5] 最高指数
                    temp_x[6] 最低指数
                    temp_x[7] 最新指数
                    temp_x[8] 交易量
                    temp_x[9] 成交金额
                    temp_x[10] 前盘指数                                                      
                    */
                    '''
def Index_Data(str):
    print(str)


    
    '''
    /*temp_x option行情快照结构
                    temp_x[0] 000002.SZ  标准代码
                    temp_x[1] 000002 代码
                    temp_x[2] 20170101 日期
                    temp_x[3] 93000000 时间
                    temp_x[4] 阶段标志
                    temp_x[5] 涨停价
                    temp_x[6] 跌停价
                    temp_x[7] 成交总量
                    temp_x[8] 成交总金额
                    
                    temp_x[9] 最新价
                    temp_x[10] 开盘价
                    temp_x[11] 最高价
                    temp_x[12] 最低价
                    temp_x[13] 昨结算价
                    temp_x[14] 持仓总量
                    temp_x[15-19] 买1-5价
                    temp_x[20-24] 买1-5量
                    temp_x[25-29] 卖1-5价
                    temp_x[30-34] 卖1-5量
                     */'''
def Option_Data(str):
    print(str)

'''
    /*temp_x queue 委托队列结构
                    temp_x[0] 000002.SZ  标准代码
                    temp_x[1] 000002 代码
                    temp_x[2] 20170101 日期
                    temp_x[3] 93000000 时间
                    temp_x[4] 卖一price
                    temp_x[5] 卖一队列数
                    temp_x[6] 买一price
                    temp_x[7] 买一队列数
                    temp_x[8]-temp_x[107] 订单明细 sell_queue0-sell_queue50  buy_queue0-buy_queue50                                                     
                    */'''
def Queue_Data(str):
    strx = str.split("#")
    for neiron in strx:
        #print(neiron)
        temp_x = neiron.split("|")
        if( temp_x[1]=="000002"):
            print(temp_x[1]+" "+temp_x[3] +" "+datetime.datetime.now().strftime('%H:%M:%S'))


'''
            /*temp_x tran 逐笔成交结构
                    temp_x[0] 000002.SZ  标准代码
                    temp_x[1] 000002 代码
                    temp_x[2] 20170101 日期
                    temp_x[3] 93000000 时间
                    temp_x[4] 成交编号
                    temp_x[5] 成交价格
                    temp_x[6] 成交数量
                    temp_x[7] 成交金额
                    temp_x[8] 买卖方向(买:'B',卖'A')
                    temp_x[9] 成交类别
                    temp_x[10] 成交代码
                    temp_x[11]叫卖方委托序号
                    temp_x[12]叫买方委托序号                                                      
                    */'''
def Tran_Data(str):
    strx = str.split("#")
    for neiron in strx:
        #print(neiron)
        temp_x = neiron.split("|")
        if( temp_x[1]=="000002"):
            print(temp_x[1]+" "+temp_x[3] +" "+datetime.datetime.now().strftime('%H:%M:%S'))


'''
             /*temp_x queue 委托队列结构
                temp_x[0] 000002.SZ  标准代码
                temp_x[1] 000002 代码
                temp_x[2] 20170101 日期
                temp_x[3] 93000000 时间
                temp_x[4] 委托号 
                temp_x[5] 委托价格
                temp_x[6] 委托数量
                temp_x[7] 委托类别
                temp_x[8] 委托代码                                           
                */'''
def Order_Data(str):
    strx = str.split("#")
    for neiron in strx:
        #print(neiron)
        temp_x = neiron.split("|")
        if( temp_x[1]=="000002"):
            print(temp_x[1]+" "+temp_x[3] +" "+datetime.datetime.now().strftime('%H:%M:%S'))    


if __name__ == '__main__':
    print('test level2 dll by python')
    login = login()

    login.ip = "";
    login.user = "";
    login.password = "";
    #heart_o_c = false;
    
    login.ss_Index_event += Index_Data;
    login.ss_Option_event += Option_Data;
    login.ss_Market_event0 += Market_Data;
    login.ss_Queue_event0 += Queue_Data;
    login.ss_Tran_event0 += Tran_Data;
    login.ss_Order_event0 += Order_Data;


    #开启订阅
    #login.index_Get();
    #login.option_Get();
    #login.market_Get();
    login.tran_Get();
    #login.order_Get();
    #login.queue_Get();
    #推送的数据在SS_data.cs中的回调函数中获取

    #login.index_Close();
    #login.option_Close();
    #login.market_Close();
    #login.tran_Close();
    #login.order_Close();
    #login.queue_Close();

print ("=====================0=====================")

#print (ord(msvcrt.getch()))


