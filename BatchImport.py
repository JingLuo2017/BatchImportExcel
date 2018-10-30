# -*- coding: utf-8 -*-
import pymysql

import sys
import cx_Oracle
import os
from CellList import *

'''
2018年10月23日16点24分备份
    能够实现插入数据库表格
2018年10月24日10点22分备份
    实现多余出现空行处理删除
20181029更新
    1.实现判断空行操作，将非空行所在行数存入列表
    2.修改代码结构，
'''

# 保证客户端与数据库字符集一致
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'

# FAMILY_BUSINSESS_TOTAL_INCOME
# business_income_sheet = [uuid.uuid1(), FAMILY_ID, BUSINESS_TYPE, BUSINESS_SIZE, NUMBER_OF_HIRED_PEOPLE, START_TIME,
#                          TOTAL_BUSINESS_INCOME_YEAR]


# try:
sql = 'delete from family_basic'

insert_basic = '''
insert into ads.family_basic (
FAMILY_ID,CITY,COUNTY,TOWN,VILLAGE,UNIT,HOUSE_NUMBER,POVERTIES,MILITARY_FAMILY,MARTYR_FAMILY,
FARMER_PROFESSIONAL_COOPERATIV,COMMEND,AGRICULTURAL_ORDERS,INVESTMENT_INSURANCE,OCCUPATION_OF_LINEAL_RELATIVES,
TOTAL_SUBSIDY,NET_WORKING,TOTAL_EXPENDITURE,TOTAL_LOAN_MONEY,
RECOMMENDED_LOAN_AMOUNT,COMPLETE_DANGEROUS_HOUSE_REPAI,HONESTY_CREDIT,RESPECT_AGE,UNITE_NEIGHBORHOOD,
BAD_HABITS,FAMILY_NAME,ID,ORGNIZATION_ID
) 
values (
:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,
:11,:12,:13,:14,:15,
:16,:17,:18,:19,
:21,:22,:23,:24,:25,
:26,:27,:28,:29)
'''

if __name__ == '__main__':

    input_file = 'C:\\Users\\admin\\Desktop\\ADS家庭信息采集表模板.xlsx'
    data_frame = pd.read_excel(input_file, sheet_name=[1])  # 第二张sheet转化为字典
    sheet = data_frame[1].values
    # FAMILY_BASIC
    basic_sheet = loc_basic(sheet)
    print(basic_sheet)
    basic_after = replace_null(basic_sheet)
    print('after' + str(basic_after))

    # # FAMIY_MEMBER
    # member_sheet = loc_member(sheet)
    # print(member_sheet)

    # # FAMILLY_PLANTING_TOTAL_INCOME
    planting_sheet = loc_planting_income(sheet)
    print(planting_sheet)

    # FAMILY_BUSINSESS_TOTAL_INCOME
    business_list = loc_business(sheet)
    print(business_list)

    # 打开数据库连接
    host = "192.168.118.140"
    port = "1521"
    sid = "dbsrv2"
    service_name = 'orcl11g.us.oracle.com'
    username = 'ads'
    password = 'ADS'
    conn = username + '/' + password + '@' + host + ':' + port + '/' + service_name
    try:
        # db = cx_Oracle.connect(conn)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        print('连接数据库成功')
        cursor.execute(sql)
        a = cursor.execute(insert_basic, basic_after)
        db.commit()
        print('插入数据成功')
        sql2 = 'select * from family_basic'
        cursor.execute(sql2)
        results = cursor.fetchall()  # 获取查询的所有记录
        print(results)
        # except Exception as e:
        #     db.rollback()
        #     print(str(e))
        # if errno == 1062:
        #     print('唯一性约束错误，请检查身份证后再试')
        # elif errno == 0850:

        # 使用 execute()  方法执行 SQL 查询
        # cursor.execute(sql1)
        # 关闭数据库连接
        db.close()
    except Exception as e:
        print(e)
