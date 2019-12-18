# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Connect + Add Data to Table on AWS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

import pymysql
import pandas as pd
import json


# JSON method
def get_db_prep_value(value):
    try:
        return json.dumps(value)
    except TypeError:
        BAD_DATA.error(
            "cannot serialize %s to store in a JsonField", str(value)
        )
        return ""

def from_db_value(value):
    if value == "":
        return None
    try:
        return json.loads(value)
    except TypeError:
        BAD_DATA.error("cannot load dictionary field -- type error")
        return None

def get_dict_from_cursor(cursorObject):
    #Fetch all the rows
    rows = cursorObject.fetchall()

    for row in rows:
        data = row[0]
        dict_value = from_db_value(data)
        return dict_value



# ~ Connect to Database ~ #
host = 'sg-jiutishi-db.ciuqsne5nixf.ap-southeast-1.rds.amazonaws.com'
dbname = 'poemDB'
user = 'admin'
password='?Jiutishi.2019'
port=3306
charSet = "utf8"
connectionObject = pymysql.connect(host, user=user, port=port, charset=charSet, 
	passwd=password,db=dbname,autocommit=True)

try:
    # Create a cursor object
    cursorObject = connectionObject.cursor()                                     

    # SQL query string
    # SELECT
    sqlQuery = "SELECT slider FROM Topic WHERE id = 1"
    cursorObject.execute(sqlQuery)

    # Show Tables
    # sqlQuery = "show tables"  

    # CREATE
    # sqlQuery = "CREATE TABLE Topic(id int primary key, name varchar(32), chn_name varchar(32), logo_url int, slider TEXT)"   
    # sqlQuery = "CREATE TABLE Poem(id int primary key, LastName varchar(32), FirstName varchar(32), YearOfBirth int)"   

    # INSERT
    # Create a new record
    # sqlQuery = "INSERT INTO `Poet` (`id`, `LastName`, `FirstName`, `YearOfBirth`) VALUES (1, '林', '遵宪', 1980)"
    
    # DROP TABLE
    # sqlQuery = "DROP TABLE Poem"

    # Add Column
    # sqlQuery = "ALTER TABLE Topic ADD slider blob(1024)"

    # Create dict to JSON list
    # chunlian = {"slider_type": 0, "urls": ['slider-chunlian.jpeg']}
    # dazhuan = {"slider_type": 0, "urls": ['slider-dazhuan.png']}
    # nus = {"slider_type": 0, "urls": ['slider-nus.png']}
    # yinglian = {"slider_type": 0, "urls": ['slider-sgyinglian.png']}
    # shuanglin = {"slider_type": 0, "urls": ['slider-shuanglin.jpg']}
    # xinzhou = {"slider_type": 0, "urls": ['slider-xinzhou.png']}
    # mingsheng = {
    #     "slider_type": 1, 
    #     "urls_dict": {
    #         "slider-mingshengguji-1.jpg": ["濱海灣", "魚尾獅", "1965-2019"], 
    #         "slider-shuanglin.jpg": ["184 Jalan Toa Payoh, Singapore 319944", "雙林寺"],
    #     }
    # }
    # fengsu = {
    #     "slider_type": 1, 
    #     "urls_dict": {
    #         "slider-yusheng.jpeg": ["南洋文化傳統", "撈魚生", "2019"], 
    #         "slider-durian.jpg": ["南洋水果文化", "榴蓮"], 
    #     }
    # }
    # yuyan = {
    #     "slider_type": 1, 
    #     "urls_dict": {
    #         "slider-nanyang.jpg": ["百花齐放", "南洋方言", "2019"], 
    #         "slider-minnan.png": ["Hokkien", "闽南语"], 
    #     }
    # }
    # wuchan = {
    #     "slider_type": 1, 
    #     "urls_dict": {
    #         "slider-binlang.jpeg": ["南洋水果", "檳榔", "2019"], 
    #         "slider-durian.jpg": ["南洋水果", "榴蓮", "2019"], 
    #     }
    # }
    # fengyue = {
    #     "slider_type": 1, 
    #     "urls_dict": {
    #         "slider-fengyue.png": ["風月", "風月"], 
    #         "slider-fengyue3.png": ["星洲風月", "新聞屑-笑紅竟作悼紅", "UT-1919-10-7-12"], 
    #         "slider-fengyue2.png": ["風月", "風月"], 
    #     }
    # }
    # foyuchanxin = {
    #     "slider_type": 1, 
    #     "urls_dict": {
    #         "slider-foyuchanxin1.jpg": ["佛語禪心", "佛語禪心"], 
    #         "slider-foyuchanxin2.png": ["佛語禪心", "佛語禪心"], 
    #     }
    # }
    # lunxian = {
    #     "slider_type": 1, 
    #     "urls_dict": {
    #         "slider-lunxianshiqi1.jpeg": ["Japanese Occupation of Singapore", "新加坡淪陷", "1942-1945"], 
    #         "slider-lunxianshiqi2.png": ["Japanese Occupation of Singapore", "新加坡淪陷", "1942-1945"], 
    #     }
    # }


    # json_list = [chunlian, dazhuan, nus, yinglian, 
    #     shuanglin, xinzhou, mingsheng, fengsu, yuyan, wuchan, fengyue, foyuchanxin, lunxian]

    # count = 1
    # for json_item in json_list:
    #     this_item = get_db_prep_value(json_item)
    #     sqlQuery = "UPDATE Topic SET slider = '{}' WHERE id = {}".format(this_item, count)
    #     cursorObject.execute(sqlQuery)
    #     count += 1


    # data_json = get_db_prep_value(chunlian)
    # # sqlQuery = "UPDATE `Topic` SET `slider` = {} WHERE `id` = 2;".format(data_json)
    # sqlQuery = "UPDATE Topic SET slider = '{}' WHERE id = 5".format(data_json)
    # # Execute the sqlQuery
    # cursorObject.execute(sqlQuery)

    #Fetch all the rows
    dict_data = get_dict_from_cursor(cursorObject)
    print(dict_data)

except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    connectionObject.close()