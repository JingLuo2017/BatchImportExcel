# -*- coding: utf-8 -*-
import pandas as pd
import uuid

FAMILY_ID = ''.join(str(uuid.uuid1()).split('-'))  # family_basic表的id为其余表的family_id 删除python生成的uuid中的短横线
print(FAMILY_ID)

# 判断excel一行是否为空，对于空行不处理，不为空的行则进入后续单元格为空处理
def notna(sheet, start_line, end_line, start_col=0, end_col=10):#参数含义：起始行、中止行、起始列、终止列
    notna = []
    for i in range(start_line, end_line):
        for j in range(start_col, end_col):
            if pd.isna(sheet[i][j]):
                j += 1
                if j == end_col:
                    continue
                    # print('第' + str(i) + '行是空的')
            else:
                # print(i,j)
                print('第' + str(i) + '行是非空的')
                notna.append(i)
                break
        i += 1
    return (notna)

# 检测excel表格单元格空值，如果存在则替换为能够插入数据库的null的形式
def replace_null(list):
    for i in range(0, len(list)):
        if pd.isna(list[i]):
            list[i] = None
    return (list)


# FAMILY_BASIC
def loc_basic(sheet):
    CITY = sheet[1][0]  # 市（州）
    COUNTY = sheet[1][1]  # 县
    TOWN = sheet[1][2]  # 乡、镇
    VILLAGE = sheet[1][3]  # 村
    UNIT = sheet[1][4]  # 组
    HOUSE_NUMBER = sheet[1][5]  # 号
    POVERTIES = sheet[17][0]  # 是否贫困户
    INVESTMENT_INSURANCE = sheet[17][1]  # 是否参加农合、新农保和商业保险或任意一项保险
    MILITARY_FAMILY = sheet[17][2]  # 是否军属
    COMMEND = sheet[17][3]  # 是否受过乡镇以上表彰
    FARMER_PROFESSIONAL_COOPERATIV = sheet[17][4]  # 是否加入农村合作社
    AGRICULTURAL_ORDERS = sheet[17][5]  # 农业订单
    OCCUPATION_OF_LINEAL_RELATIVES = sheet[17][6]  # 直系亲属的职业情况
    MARTYR_FAMILY = sheet[17][7]  # 是否烈属
    TOTAL_SUBSIDY = float(sheet[19][8])  # 年补贴总额
    NET_WORKING = sheet[19][9]  # 财产净值
    TOTAL_EXPENDITURE = float(sheet[19][6])  # 家庭总支出金额
    TOTAL_LOAN_MONEY = float(sheet[19][7])  # 借贷款总额
    RECOMMENDED_LOAN_AMOUNT = float(sheet[19][0])  # 建议贷款金额
    COMPLETE_DANGEROUS_HOUSE_REPAI = sheet[19][1]  # 是否完成危房改造
    HONESTY_CREDIT = sheet[19][2]  # 诚信状况
    RESPECT_AGE = sheet[19][4]  # 户成员敬老爱幼情况
    UNITE_NEIGHBORHOOD = sheet[19][3]  # 户成员团结邻里情况
    BAD_HABITS = sheet[19][5]  # 户成员是否有黄赌毒等不良嗜好
    FAMILY_NAME = sheet[4][0]  # 户主姓名
    ID = sheet[4][3]  # 户主身份证
    ORGNIZATION_ID = '22016'  # 机构号

    basic_sheet = [ID, CITY, COUNTY, TOWN, VILLAGE, UNIT, HOUSE_NUMBER, POVERTIES, MILITARY_FAMILY, MARTYR_FAMILY,
               FARMER_PROFESSIONAL_COOPERATIV, COMMEND, AGRICULTURAL_ORDERS, INVESTMENT_INSURANCE,
               OCCUPATION_OF_LINEAL_RELATIVES,
               TOTAL_SUBSIDY, NET_WORKING, TOTAL_EXPENDITURE, TOTAL_LOAN_MONEY,
               RECOMMENDED_LOAN_AMOUNT, COMPLETE_DANGEROUS_HOUSE_REPAI, HONESTY_CREDIT, RESPECT_AGE, UNITE_NEIGHBORHOOD,
               BAD_HABITS, FAMILY_NAME, FAMILY_ID, ORGNIZATION_ID]
    return(basic_sheet)



# FAMILY_MEMBER 4-15行
def loc_member(sheet):
    member_list = notna(sheet, 4, 16)
    for i in range(0, len(member_list)):
        MEMBER_NAME = sheet[member_list[i]][0]  # 成员姓名
        GENDER = None  # 性别
        RELATIONSHIP_WITH_HEAD = sheet[member_list[i]][1]  # 与户主关系
        NATIONALITY = sheet[member_list[i]][2]  # 民族
        IDCARD = sheet[member_list[i]][3]  # 身份证
        EDUCATION = sheet[member_list[i]][4]  # 文化程度
        POLITICAL = sheet[member_list[i]][5]  # 政治面貌
        MARITAL = sheet[member_list[i]][6]  # 婚姻状况
        HEALTH = sheet[member_list[i]][7]  # 健康状况
        JOB_TYPE = sheet[member_list[i]][8]  # 职业类型
        TELE = sheet[member_list[i]][9]  # 联系电话
        WECHAT = sheet[member_list[i]][10]  # 微信QQ
        member_sheet = [''.join(str(uuid.uuid1()).split('-')), FAMILY_ID, MEMBER_NAME, GENDER, RELATIONSHIP_WITH_HEAD, NATIONALITY, IDCARD, EDUCATION, POLITICAL, MARITAL, HEALTH, JOB_TYPE, TELE, WECHAT]
    return(member_sheet)
# # FAMILLY_PLANTING_TOTAL_INCOME 23-26行
# PLANTING_AND_BREEDING_CATEGORI = sheet[23][0]  # 种养殖类别
# AMOUNT = sheet[23][1]  # 数量(亩、头、只、箱)
# PER_YEAR_INCOME = sheet[23][2]  # 该农产品年收入

# # FAMILY_BUSINSESS_TOTAL_INCOME 35-38行
# BUSINESS_TYPE = sheet[35][0]  # 经营类型
# BUSINESS_SIZE = sheet[35][1]  # 经营规模
# NUMBER_OF_HIRED_PEOPLE = sheet[35][2]  # 雇佣人数
# START_TIME = sheet[35][3]  # 该总经营时长
# TOTAL_BUSINESS_INCOME_YEAR = sheet[35][4]  # 该经营年收入
'''
# LAND 42-43行   需单个单元格进行操作，每一个单元格的值都要写入数据库的一行
CULTIVATION_TYPE = sheet[][0]  # 使用权类型(自有和流转)
LAND_STATUS = sheet[][]  # 耕地、水浇地、林地、草地
PLOUGH_AREA = sheet[][]  # 面积

# FAMILY_HOUSE 46-47行
HOUSE_NATURE = sheet[][0]  # 房屋性质
HOUSE_TYPE = sheet[][1]  # 房屋类型
BUILDING_TIME = sheet[][2]  # 构建年月
FAMILY_HOUSE_AREA = sheet[][3]  # 房屋面积
BUILDING_PRICE = sheet[][4]  # 构建价格
PURCHASE_FAMILY_HOUSE_PLAN = sheet[][5]  # 近期是否有购房计划

# FAMILY_AGRICULTURAL_MACHINERY 50-53行
FAMILY_ID = sheet[][]  # 户id
MACHINERY_TYPE = sheet[][0]  # 机械类型
MACHINERY_NUM = sheet[][1]  # 数量
MACHINERY_PURCHASE_TIME = sheet[][2]  # 购买年月
MACHINERY_PRICE = sheet[][3]  # 价格
PURCHASE_MACHINERY_PLAN = sheet[][4]  # 是否有采购农业机械计划

# FAMILY_NON_FARM_VEHICLE 55-58行
VEHICLE_TYPE = sheet[][0]  # 车辆类型
VEHICLE_NUM = sheet[][1]  # 该类型车辆数量
VEHICLE_PURCHASE_TIME = sheet[][2]  # 购买年月
VEHICLE_PRICE = sheet[][3]  # 价格
PURCHASE_VEHICLE_PLAN = sheet[][4]  # 近期是否有采购车辆计划

# FAMILY_AGRICULTURAL_FACILITIES 61-63行
TYPES_OF_AGRICULTURAL_FACILITI = sheet[][0]  # 农业设施类型
NUMBER_OF_AGRICULTURAL_FACILIT = sheet[][1]  # 农业设施数量
COAST = sheet[][2]  # 成本

# FAMILY_EQUITYINVESTMENT 66行
INVESTMENT_TYPES = sheet[66][0]  # 投资类型(现金、土地、其他)
APPRAISEMENT = sheet[66][1]  # 估值
ANNUAL_EARNINGS = sheet[66][2]  # 年收益

# FAMILLY_SUBSIDY 69行0-8列   此处需要注意，对于补贴金额是null的不做插入操作
SUBSIDY_TYPE = sheet[68][]  # 补贴类型
SUBSIDY_AMOUNT = sheet[69][]  # 补贴金额

# FAMILY_EXPENDITURE 73行0-4列    需单个单元格进行操作，每一个单元格的值都要写入数据库的一行
FAMILY_EXPENDITURE_TYPE = sheet[][]#支出类型'
FAMILY_EXPENDITURE_AMOUNT = sheet[][]#支出金额'

# FAMILY_LOAN 75-76行    注意，第一行父类型是银行借款，第二行是私人借入款
BORROW_PATTERN = sheet[][0]#贷款方式
BORROW_SUM = sheet[][1]#贷、借款金额(万元)
LOAN_TERM = sheet[][2]#贷、借款期限(月)
LOAN_DEADLINE = sheet[][3]#到期时间
REPAY_MONEY = sheet[][4]#已偿还金额(万元)
BORROW_PATTERN_PARENT = #偿还方式父类型

# LOG_ENTER_AUDIT
ENTER_USERNAME = #录入人员
ENTER_DATETIME = #录入时间
AUDIT_USERNAME = #审核人员
AUDIT_DATETIME = #审核时间
STATUS = #状态
DELETE_USERNAME = #删除人员
DELETE_DATETIME = #删除日期
NOT_PASSED_INFO = #未通过信息
DEPTID = #部门ID
RESERVED_FIELD1 = #预留字段1
RESERVED_FIELD2 = #预留字段2
'''
