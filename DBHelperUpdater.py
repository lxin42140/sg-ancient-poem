from DBHelper import DBHelper

db = DBHelper()

# Create dict to JSON list
chunlian = {"slider_type": 0, "urls": ['slider-chunlian.jpeg']}
dazhuan = {"slider_type": 0, "urls": ['slider-dazhuan.png']}
nus = {"slider_type": 0, "urls": ['slider-nus.png']}
yinglian = {"slider_type": 0, "urls": ['slider-sgyinglian.png']}
shuanglin = {"slider_type": 0, "urls": ['slider-shuanglin.jpg']}
xinzhou = {"slider_type": 0, "urls": ['slider-xinzhou.png']}
mingsheng = {
    "slider_type": 1,
    "urls_dict": {
        "slider-mingshengguji-1.jpg": ["濱海灣", "魚尾獅", "1965-2019"],
        "slider-shuanglin.jpg": ["184 Jalan Toa Payoh, Singapore 319944", "雙林寺"],
    }
}
fengsu = {
    "slider_type": 1,
    "urls_dict": {
        "slider-yusheng.jpeg": ["南洋文化傳統", "撈魚生", "2019"],
        "slider-durian.jpg": ["南洋水果文化", "榴蓮"],
    }
}
yuyan = {
    "slider_type": 1,
    "urls_dict": {
        "slider-nanyang.jpg": ["百花齐放", "南洋方言", "2019"],
        "slider-minnan.png": ["Hokkien", "闽南语"],
    }
}
wuchan = {
    "slider_type": 1,
    "urls_dict": {
        "slider-binlang.jpeg": ["南洋水果", "檳榔", "2019"],
        "slider-durian.jpg": ["南洋水果", "榴蓮", "2019"],
    }
}
fengyue = {
    "slider_type": 1,
    "urls_dict": {
        "slider-fengyue.png": ["風月", "風月"],
        "slider-fengyue3.png": ["星洲風月", "新聞屑-笑紅竟作悼紅", "UT-1919-10-7-12"],
        "slider-fengyue2.png": ["風月", "風月"],
    }
}
foyuchanxin = {
    "slider_type": 1,
    "urls_dict": {
        "slider-foyuchanxin1.jpg": ["佛語禪心", "佛語禪心"],
        "slider-foyuchanxin2.png": ["佛語禪心", "佛語禪心"],
    }
}
lunxian = {
    "slider_type": 1,
    "urls_dict": {
        "slider-lunxianshiqi1.jpeg": ["Japanese Occupation of Singapore", "新加坡淪陷", "1942-1945"],
        "slider-lunxianshiqi2.png": ["Japanese Occupation of Singapore", "新加坡淪陷", "1942-1945"],
    }
}


json_list = [chunlian, dazhuan, nus, yinglian,
    shuanglin, xinzhou, mingsheng, fengsu, yuyan, wuchan, fengyue, foyuchanxin, lunxian]

print(db.save_sliders_to_db(json_list))