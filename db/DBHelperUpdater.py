from db.DBHelper import DBHelper

db = DBHelper()
#
# # Create dict to JSON list
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

# xinshengshishe = {
#     "slider_type": 1,
#     "urls_dict": {
#         "slider-xinsheng1.jpg": [" ", "新聲詩社丹戎禺雅集照片1", " "],
#         "slider-xinsheng2.jpg": [" ", "新聲詩社丹戎禺雅集照片2", " "],
#         "slider-xinsheng3.jpg": [" ", "新聲詩社丹戎禺雅集照片3", " "],
#         "slider-xinsheng4.jpg": [" ", "新聲詩社丹戎禺雅集照片4", " "],
#         "slider-xinsheng5.jpg": [" ", "新聲詩社丹戎禺雅集照片5", " "],
#         "slider-xinsheng6.jpg": [" ", "新聲詩社丹戎禺雅集照片6", " "],
#         "slider-xinsheng7.jpg": [" ", "新聲詩社丹戎禺雅集照片7", " "],
#         "slider-xinsheng8.jpg": [" ", "新聲詩社丹戎禺雅集照片8", " "],
#         "slider-xinsheng9.jpg": [" ", "丹戎禺雅集合影", " "],
#     }
# }

# qiushuyuan = {
#     "slider_type": 1,
#     "urls_dict": {
#         "slider-qiushuyuan1.jpg": [" ", "邱菽园及振南日报印刷所照片", " "]
#     }
# }


qitashishe = {
    "slider_type": 1,
    "urls_dict": {
        "slider-shishe1.jpg": [" ", "雲南園吟唱集顧問暨籌委", " "]
    }
}



# json_list = [chunlian, dazhuan, nus, yinglian,
#     shuanglin, xinzhou, mingsheng, fengsu, yuyan, wuchan, fengyue, foyuchanxin, lunxian]


print(db.save_slider_to_db(qitashishe, 25))