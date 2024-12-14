# 省份名称与城市列表映射
province_to_cities = {
    "山东": ["济南", "滨州", "青岛", "烟台", "临沂", "潍坊", "淄博", "东营", "聊城", "菏泽", "枣庄", "德州", "威海", "济宁", "泰安", "莱芜", "日照"],
    "贵州": ["贵阳", "黔南", "六盘水", "遵义", "黔东南", "铜仁", "安顺", "毕节", "黔西南"],
    "江西": ["南昌", "九江", "鹰潭", "抚州", "上饶", "赣州", "吉安", "萍乡", "景德镇", "新余", "宜春"],
    "内蒙古": ["呼和浩特", "包头", "鄂尔多斯", "巴彦淖尔", "乌海", "阿拉善盟", "锡林郭勒盟", "赤峰", "通辽", "呼伦贝尔", "乌兰察布", "兴安盟"],
    "湖北": ["武汉", "黄石", "荆州", "襄阳", "黄冈", "荆门", "宜昌", "十堰", "随州", "恩施", "鄂州", "咸宁", "孝感", "仙桃", "天门", "潜江", "神农架"],
    "辽宁": ["沈阳", "大连", "盘锦", "鞍山", "朝阳", "锦州", "铁岭", "丹东", "本溪", "营口", "抚顺", "阜新", "辽阳", "葫芦岛"],
    "湖南": ["长沙", "岳阳", "衡阳", "株洲", "湘潭", "益阳", "郴州", "湘西", "娄底", "怀化", "常德", "张家界", "永州", "邵阳"],
    "福建": ["福州", "莆田", "三明", "龙岩", "厦门", "泉州", "漳州", "宁德", "南平"],
    "广西": ["南宁", "柳州", "桂林", "贺州", "贵港", "玉林", "河池", "北海", "钦州", "防城港", "百色", "梧州", "来宾", "崇左"],
    "广东": ["广州", "深圳", "东莞", "云浮", "佛山", "湛江", "江门", "惠州", "珠海", "韶关", "阳江", "茂名", "潮州", "揭阳", "中山", "清远", "肇庆", "河源", "梅州", "汕头", "汕尾"],
    "四川": ["成都", "宜宾", "绵阳", "广元", "遂宁", "巴中", "内江", "泸州", "南充", "德阳", "乐山", "广安", "资阳", "自贡", "攀枝花", "达州", "雅安", "眉山", "甘孜", "阿坝", "凉山"],
    "云南": ["昆明", "玉溪", "楚雄", "大理", "昭通", "红河", "曲靖", "丽江", "临沧", "文山", "保山", "普洱", "西双版纳", "德宏", "怒江", "迪庆"],
    "江苏": ["南京", "苏州", "无锡", "连云港", "淮安", "扬州", "泰州", "盐城", "徐州", "常州", "南通", "镇江", "宿迁"],
    "浙江": ["杭州", "丽水", "金华", "温州", "台州", "衢州", "宁波", "绍兴", "嘉兴", "湖州", "舟山"],
    "青海": ["西宁", "海西", "海东", "玉树", "海南", "海北", "黄南", "果洛"],
    "宁夏": ["银川", "吴忠", "固原", "石嘴山", "中卫"],
    "河北": ["石家庄", "衡水", "张家口", "承德", "秦皇岛", "廊坊", "沧州", "保定", "唐山", "邯郸", "邢台"],
    "黑龙江": ["哈尔滨", "大庆", "伊春", "大兴安岭", "黑河", "鹤岗", "七台河", "齐齐哈尔", "佳木斯", "牡丹江", "鸡西", "绥化", "双鸭山"],
    "吉林": ["长春", "四平", "辽源", "松原", "吉林", "通化", "白山", "白城", "延边"],
    "陕西": ["西安", "铜川", "安康", "宝鸡", "商洛", "渭南", "汉中", "咸阳", "榆林", "延安"],
    "甘肃": ["兰州", "庆阳", "定西", "武威", "酒泉", "张掖", "嘉峪关", "平凉", "天水", "白银", "金昌", "陇南", "临夏", "甘南"],
    "新疆": ["乌鲁木齐", "石河子", "吐鲁番", "昌吉", "哈密", "阿克苏", "克拉玛依", "博尔塔拉", "阿勒泰", "喀什", "和田", "巴音郭楞", "伊犁", "塔城", "克孜勒苏柯尔克孜", "五家渠", "阿拉尔", "图木舒克"],
    "河南": ["郑州", "南阳", "新乡", "开封", "焦作", "平顶山", "许昌", "安阳", "驻马店", "信阳", "鹤壁", "周口", "商丘", "洛阳", "漯河", "濮阳", "三门峡", "济源"],
    "安徽": ["合肥", "铜陵", "黄山", "池州", "宣城", "巢湖", "淮南", "宿州", "六安", "滁州", "淮北", "阜阳", "马鞍山", "安庆", "蚌埠", "芜湖", "亳州"],
    "山西": ["太原", "大同", "长治", "忻州", "晋中", "临汾", "运城", "晋城", "朔州", "阳泉", "吕梁"],
    "海南": ["海口", "万宁", "琼海", "三亚", "儋州", "东方", "五指山", "文昌", "陵水", "澄迈", "乐东", "临高", "定安", "昌江", "屯昌", "保亭", "白沙", "琼中"],
    "台湾": ["台北", "高雄", "台中", "台南", "新北", "桃园", "台东", "台中", "基隆", "花莲"],
    "西藏": ["拉萨", "日喀则", "那曲", "林芝", "山南", "昌都", "阿里"],
}

city_to_code = {
    "全国": 0,
    "山东": 901, "山东-济南": 1, "山东-滨州": 76, "山东-青岛": 77, "山东-烟台": 78, "山东-临沂": 79,
    "山东-潍坊": 80, "山东-淄博": 81, "山东-东营": 82, "山东-聊城": 83, "山东-菏泽": 84, "山东-枣庄": 85,
    "山东-德州": 86, "山东-威海": 88, "山东-济宁": 352, "山东-泰安": 353, "山东-莱芜": 356, "山东-日照": 366,
    "贵州": 902, "贵州-贵阳": 2, "贵州-黔南": 3, "贵州-六盘水": 4, "贵州-遵义": 59, "贵州-黔东南": 61,
    "贵州-铜仁": 422, "贵州-安顺": 424, "贵州-毕节": 426, "贵州-黔西南": 588,
    "江西": 903, "江西-南昌": 5, "江西-九江": 6, "江西-鹰潭": 7, "江西-抚州": 8, "江西-上饶": 9,
    "江西-赣州": 10, "江西-吉安": 115, "江西-萍乡": 136, "江西-景德镇": 137, "江西-新余": 246, "江西-宜春": 256,
    "重庆": 904,
    "内蒙古": 905, "内蒙古-呼和浩特": 20, "内蒙古-包头": 13, "内蒙古-鄂尔多斯": 14, "内蒙古-巴彦淖尔": 15,
    "内蒙古-乌海": 16, "内蒙古-阿拉善盟": 17, "内蒙古-锡林郭勒盟": 19, "内蒙古-赤峰": 21, "内蒙古-通辽": 22,
    "内蒙古-呼伦贝尔": 25, "内蒙古-乌兰察布": 331, "内蒙古-兴安盟": 333,
    "湖北": 906, "湖北-武汉": 28, "湖北-黄石": 30, "湖北-荆州": 31, "湖北-襄阳": 32, "湖北-黄冈": 33,
    "湖北-荆门": 34, "湖北-宜昌": 35, "湖北-十堰": 36, "湖北-随州": 37, "湖北-恩施": 38, "湖北-鄂州": 39,
    "湖北-咸宁": 40, "湖北-孝感": 41, "湖北-仙桃": 42, "湖北-天门": 73, "湖北-潜江": 74, "湖北-神农架": 687,
    "辽宁": 907, "辽宁-沈阳": 150, "辽宁-大连": 29, "辽宁-盘锦": 151, "辽宁-鞍山": 215, "辽宁-朝阳": 216,
    "辽宁-锦州": 217, "辽宁-铁岭": 218, "辽宁-丹东": 219, "辽宁-本溪": 220, "辽宁-营口": 221, "辽宁-抚顺": 222,
    "辽宁-阜新": 223, "辽宁-辽阳": 224, "辽宁-葫芦岛": 225,
    "湖南": 908, "湖南-长沙": 43, "湖南-岳阳": 44, "湖南-衡阳": 45, "湖南-株洲": 46, "湖南-湘潭": 47,
    "湖南-益阳": 48, "湖南-郴州": 49, "湖南-湘西": 65, "湖南-娄底": 66, "湖南-怀化": 67, "湖南-常德": 68,
    "湖南-张家界": 226, "湖南-永州": 269, "湖南-邵阳": 405,
    "福建": 909, "福建-福州": 50, "福建-莆田": 51, "福建-三明": 52, "福建-龙岩": 53, "福建-厦门": 54,
    "福建-泉州": 55, "福建-漳州": 56, "福建-宁德": 87, "福建-南平": 253,
    "上海": 910,
    "北京": 911,
    "广西": 912, "广西-南宁": 90, "广西-柳州": 89, "广西-桂林": 91, "广西-贺州": 92, "广西-贵港": 93,
    "广西-玉林": 118, "广西-河池": 119, "广西-北海": 128, "广西-钦州": 129, "广西-防城港": 130, "广西-百色": 131,
    "广西-梧州": 132, "广西-来宾": 506, "广西-崇左": 665,
    "广东": 913, "广东-广州": 95, "广东-深圳": 94, "广东-东莞": 133, "广东-云浮": 195, "广东-佛山": 196,
    "广东-湛江": 197, "广东-江门": 198, "广东-惠州": 199, "广东-珠海": 200, "广东-韶关": 201, "广东-阳江": 202,
    "广东-茂名": 203, "广东-潮州": 204, "广东-揭阳": 205, "广东-中山": 207, "广东-清远": 208, "广东-肇庆": 209,
    "广东-河源": 210, "广东-梅州": 211, "广东-汕头": 212, "广东-汕尾": 213,
    "四川": 914, "四川-成都": 97, "四川-宜宾": 96, "四川-绵阳": 98, "四川-广元": 99, "四川-遂宁": 100,
    "四川-巴中": 101, "四川-内江": 102, "四川-泸州": 103, "四川-南充": 104, "四川-德阳": 106, "四川-乐山": 107,
    "四川-广安": 108, "四川-资阳": 109, "四川-自贡": 111, "四川-攀枝花": 112, "四川-达州": 113, "四川-雅安": 114,
    "四川-眉山": 291, "四川-甘孜": 417, "四川-阿坝": 457, "四川-凉山": 479, 
    "云南": 915, "云南-昆明": 117, "云南-玉溪": 123, "云南-楚雄": 124, "云南-大理": 334, "云南-昭通": 335,
    "云南-红河": 337, "云南-曲靖": 339, "云南-丽江": 342, "云南-临沧": 350, "云南-文山": 437,
    "云南-保山": 438, "云南-普洱": 666, "云南-西双版纳": 668, "云南-德宏": 669, "云南-怒江": 671,
    "云南-迪庆": 672,
    "江苏": 916, "江苏-南京": 125, "江苏-苏州": 126, "江苏-无锡": 127, "江苏-连云港": 156,
    "江苏-淮安": 157, "江苏-扬州": 158, "江苏-泰州": 159, "江苏-盐城": 160, "江苏-徐州": 161,
    "江苏-常州": 162, "江苏-南通": 163, "江苏-镇江": 169, "江苏-宿迁": 172,
    "浙江": 917, "浙江-杭州": 138, "浙江-丽水": 134, "浙江-金华": 135, "浙江-温州": 149,
    "浙江-台州": 287, "浙江-衢州": 288, "浙江-宁波": 289, "浙江-绍兴": 303, "浙江-嘉兴": 304,
    "浙江-湖州": 305, "浙江-舟山": 306,
    "青海": 918, "青海-西宁": 139, "青海-海西": 608, "青海-海东": 652, "青海-玉树": 659,
    "青海-海南": 676, "青海-海北": 682, "青海-黄南": 685, "青海-果洛": 688,
    "宁夏": 919, "宁夏-银川": 140, "宁夏-吴忠": 395, "宁夏-固原": 396, "宁夏-石嘴山": 472,
    "宁夏-中卫": 480,
    "河北": 920, "河北-石家庄": 141, "河北-衡水": 143, "河北-张家口": 144, "河北-承德": 145,
    "河北-秦皇岛": 146, "河北-廊坊": 147, "河北-沧州": 148, "河北-保定": 259, "河北-唐山": 261,
    "河北-邯郸": 292, "河北-邢台": 293,
    "黑龙江": 921, "黑龙江-哈尔滨": 152, "黑龙江-大庆": 153, "黑龙江-伊春": 295,
    "黑龙江-大兴安岭": 297, "黑龙江-黑河": 300, "黑龙江-鹤岗": 301, "黑龙江-七台河": 302,
    "黑龙江-齐齐哈尔": 319, "黑龙江-佳木斯": 320, "黑龙江-牡丹江": 322, "黑龙江-鸡西": 323,
    "黑龙江-绥化": 324, "黑龙江-双鸭山": 359,
    "吉林": 922, "吉林-长春": 154, "吉林-四平": 155, "吉林-辽源": 191, "吉林-松原": 194,
    "吉林-吉林": 270, "吉林-通化": 407, "吉林-白山": 408, "吉林-白城": 410, "吉林-延边": 525,
    "天津": 923, "天津-天津": 923,
    "陕西": 924, "陕西-西安": 165, "陕西-铜川": 271, "陕西-安康": 272, "陕西-宝鸡": 273,
    "陕西-商洛": 274, "陕西-渭南": 275, "陕西-汉中": 276, "陕西-咸阳": 277, "陕西-榆林": 278,
    "陕西-延安": 401,
    "甘肃": 925, "甘肃-兰州": 166, "甘肃-庆阳": 281, "甘肃-定西": 282, "甘肃-武威": 283,
    "甘肃-酒泉": 284, "甘肃-张掖": 285, "甘肃-嘉峪关": 286, "甘肃-平凉": 307, "甘肃-天水": 308,
    "甘肃-白银": 309, "甘肃-金昌": 343, "甘肃-陇南": 344, "甘肃-临夏": 346, "甘肃-甘南": 673,
    "新疆": 926, "新疆-乌鲁木齐": 467, "新疆-石河子": 280, "新疆-吐鲁番": 310,
    "新疆-昌吉": 311, "新疆-哈密": 312, "新疆-阿克苏": 315, "新疆-克拉玛依": 317,
    "新疆-博尔塔拉": 318, "新疆-阿勒泰": 383, "新疆-喀什": 384, "新疆-和田": 386,
    "新疆-巴音郭楞": 499, "新疆-伊犁": 520, "新疆-塔城": 563, "新疆-克孜勒苏柯尔克孜": 653,
    "新疆-五家渠": 661, "新疆-阿拉尔": 692, "新疆-图木舒克": 693,
    "河南": 927, "河南-郑州": 168, "河南-南阳": 262, "河南-新乡": 263, "河南-开封": 264,
    "河南-焦作": 265, "河南-平顶山": 266, "河南-许昌": 268, "河南-安阳": 370, "河南-驻马店": 371,
    "河南-信阳": 373, "河南-鹤壁": 374, "河南-周口": 375, "河南-商丘": 376, "河南-洛阳": 378,
    "河南-漯河": 379, "河南-濮阳": 380, "河南-三门峡": 381, "河南-济源": 667,
    "安徽": 928, "安徽-合肥": 189, "安徽-铜陵": 173, "安徽-黄山": 174, "安徽-池州": 175,
    "安徽-宣城": 176, "安徽-巢湖": 177, "安徽-淮南": 178, "安徽-宿州": 179, "安徽-六安": 181,
    "安徽-滁州": 182, "安徽-淮北": 183, "安徽-阜阳": 184, "安徽-马鞍山": 185, "安徽-安庆": 186,
    "安徽-蚌埠": 187, "安徽-芜湖": 188, "安徽-亳州": 391,
    "山西": 929, "山西-太原": 231, "山西-大同": 227, "山西-长治": 228, "山西-忻州": 229,
    "山西-晋中": 230, "山西-临汾": 232, "山西-运城": 233, "山西-晋城": 234, "山西-朔州": 235,
    "山西-阳泉": 236, "山西-吕梁": 237,
    "海南": 930, "海南-海口": 239, "海南-万宁": 241, "海南-琼海": 242, "海南-三亚": 243,
    "海南-儋州": 244, "海南-东方": 456, "海南-五指山": 582, "海南-文昌": 670, "海南-陵水": 674,
    "海南-澄迈": 675, "海南-乐东": 679, "海南-临高": 680, "海南-定安": 681, "海南-昌江": 683,
    "海南-屯昌": 684, "海南-保亭": 686, "海南-白沙": 689, "海南-琼中": 690,
    "台湾": 931,
    "西藏": 932, "西藏-拉萨": 466, "西藏-日喀则": 516, "西藏-那曲": 655, "西藏-林芝": "656", 
    "山南": "677", "昌都": "678", "阿里": "691",
    "香港": 933, "澳门": 934
}