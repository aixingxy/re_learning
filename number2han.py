import re
liangci_set = {'串', '事', '册', '丘', '乘', '下', '丈', '丝', '两', '举', '具', '美', '包', '厘', '刀', '分', '列', '则', '剂', '副', '些',
               '匝', '队', '陌', '陔', '部', '出', '个', '介', '令', '份', '伙', '件', '任', '倍', '儋', '卖', '亩', '记', '双', '发', '叠',
               '节', '茎', '莛', '荮', '落', '蓬', '蔸', '巡', '过', '进', '通', '造', '遍', '道', '遭', '对', '尊', '头', '套', '弓', '引',
               '张', '弯', '开', '庄', '床', '座', '庹', '帖', '帧', '席', '常', '幅', '幢', '口', '句', '号', '台', '只', '吊', '合', '名',
               '吨', '和', '味', '响', '骑', '门', '间', '阕', '宗', '客', '家', '彪', '层', '尾', '届', '声', '扎', '打', '扣', '把', '抛',
               '批', '抔', '抱', '拨', '担', '拉', '抬', '拃', '挂', '挑', '挺', '捆', '掬', '排', '捧', '掐', '搭', '提', '握', '摊', '摞',
               '撇', '撮', '汪', '泓', '泡', '注', '浔', '派', '湾', '溜', '滩', '滴', '级', '纸', '线', '组', '绞', '统', '绺', '综', '缕',
               '缗', '场', '块', '坛', '垛', '堵', '堆', '堂', '塔', '墩', '回', '团', '围', '圈', '孔', '贴', '点', '煎', '熟', '车', '轮',
               '转', '载', '辆', '料', '卷', '截', '户', '房', '所', '扇', '炉', '炷', '觉', '斤', '笔', '本', '朵', '杆', '束', '条', '杯',
               '枚', '枝', '柄', '栋', '架', '根', '桄', '梃', '样', '株', '桩', '梭', '桶', '棵', '榀', '槽', '犋', '爿', '片', '版', '歇',
               '手', '拳', '段', '沓', '班', '文', '曲', '替', '股', '肩', '脬', '腔', '支', '步', '武', '瓣', '秒', '秩', '钟', '钱', '铢',
               '锊', '铺', '锤', '锭', '锱', '章', '盆', '盏', '盘', '眉', '眼', '石', '码', '砣', '碗', '磴', '票', '罗', '畈', '番', '窝',
               '联', '缶', '耦', '粒', '索', '累', '緉', '般', '艘', '竿', '筥', '筒', '筹', '管', '篇', '箱', '簇', '角', '重', '身', '躯',
               '酲', '起', '趟', '面', '首', '项', '领', '顶', '颗', '顷', '袭', '群', '袋', '元', '岁'}

# NUM_LIANGCI = {'%'}
NUM_LIANGCI = {'岁', '万', '元', '亿', '人', '家', '个', '余', '来', '环', '公里', '天', '日', '瓦', '大洋', '局', '折',
               '兆', '米', '字', '封', '分钟', '年代', '磅', '倍', '月', '多', '℃', '%', '平方', '名', '所', '世纪', '点',
               '公斤', '幅'}

DIGIT_LIANGCI = {'年'}
NUM2HAN = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}
DANWEI = ['', '十', '百', '千', '万']
LIANGJI = ['', '万', '亿', '兆']


def _4num2han(str4):
    out = ''
    len_str4 = len(str4)
    for i in range(len(str4)):
        n = str4[len_str4 - i - 1]
        if n != '0':
            out += DANWEI[i] + NUM2HAN[n]
        elif out != '':
            if out[-1] != '零':
                out += '零'
    return out[::-1]


def integer2han(num):
    """将整数转换为汉字"""
    if num == '0':
        return '零'
    len_num = len(num)
    c = len_num // 4
    y = len_num % 4
    out = ''
    i = 0
    for i in range(1, c+1):
        num4 = num[len_num-(i*4):len_num-(i*4)+4]
        out = _4num2han(num4) + LIANGJI[i-1] + out
    if y:
        end = _4num2han(num[:y]) + LIANGJI[i]
        if len(end) < 4:
            end = end.replace('一十', '十')
        out = end + out
    return out


def digit2han(num):
    """将数字映射位汉字"""
    out = ''
    for n in range(len(num)):
        out += NUM2HAN[num[n]]
    return out


def real_num2han(num):
    """将实数转换位汉字"""
    if '.' in num:
        first = num.split('.')[0]
        second = num.split('.')[1]
        return integer2han(first) + '点' + digit2han(second)
    else:
        return integer2han(num)

def nian2han(num):
    if len(num) == 4:
        return digit2han(num)
    else:
        return real_num2han(num)


def process_real_num(text, reg='[1-9]\d*\.?\d*'):
    for l in NUM_LIANGCI:
        pat = re.compile(r'({}{})'.format(reg, l))
        rst = pat.findall(text)
        # print(rst)

        for i in range(len(rst)):
            if l == '%':
                text = text.replace(rst[i], "百分之" + real_num2han(rst[i][:-len(l)]))
            elif l == '℃':
                text = text.replace(rst[i], real_num2han(rst[i][:-len(l)]) + '摄氏度')
            elif l == '年':
                text = text.replace(rst[i], nian2han(rst[i][:-(len(l))]) + l)
            else:
                text = text.replace(rst[i], real_num2han(rst[i][:-(len(l))]) + l)

    # text = process_digit(text)
    return text

def process_digit(text, reg= '\d+'):
    pat = re.compile(r'({})'.format(reg))
    rst = pat.findall(text)
    # print(rst)
    for i in range(len(rst)):
        text = text.replace(rst[i], digit2han(rst[i]))
    return text


if __name__ == '__main__':

    # print(cwchange('20.75'))
    text = '据了解天津市今年粮食种植面积一一达665万亩预计全年粮食总产量可达20.75亿公斤比去年提高9%一一丨一丨丨丨'
    print(text.count('丨'))
    reg = '[1-9]\d*\.?\d*'
    # print(re.findall(r'[1-9]\d*\.?\d*%', text))
    # print(process_real_num(text, reg))

    # if re.findall(r'\d+', text):
    #     print()
    #     print(text)
