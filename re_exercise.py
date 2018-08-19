NUM2HAN = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}
DANWEI = ['', '十', '百', '千', '万']
LIANGJI = ['','万', '亿', '兆']
str4 = '1234'


def _4num2han(str4):
    out = ''
    len_str4 = len(str4)
    for i in range(len(str4)):
        if str4[len_str4 - i - 1] != '0':
            out += DANWEI[i]
            out += NUM2HAN[str4[len_str4 - i - 1]]
        else:
            if len(out) == 0 or "零"  in out:
                continue
            else:
                out += "零"
    return out[::-1]


def num2han(num):
    len_num = len(num)
    c = len_num // 4
    y = len_num % 4
    out = ''
    i = 0
    for i in range(c):
        num4 = num[4*i:4*i+4]
        out += _4num2han(num4) + LIANGJI[c-i-1]
    if y != 0:
        out += _4num2han(num[:y]) + LIANGJI[i+1]
    # else:
    #     out = out + LIANGJI[i + 1]
    return out


if __name__ == '__main__':
    # 四位数
    # print(_4num2han( '1234'))

    # 四位数，一个零
    # print(_4num2han( '1230'))
    # print(_4num2han( '1204'))
    # print(_4num2han( '1034'))

    # 四位数，两个零
    # print(_4num2han( '1030'))
    # print(_4num2han( '1004'))
    # print(_4num2han( '1200'))

    # 四位数，三个零
    # print(_4num2han( '1000'))

    # 多位数
    print(num2han('12345'))
    print(num2han('123456'))
    print(num2han('1234567'))
    print(num2han('12345678'))
    print(num2han('123456789'))
    print(num2han('1234567891'))
    print(num2han('12345678912'))
    print(num2han('123456789123'))
    print(num2han('1234567891234'))
    print(num2han('12345678912345'))
    print(num2han('123456789123456'))


    # 五位数，一个零
    # print(num2han('12345'))
    # print(num2han('12340'))
    # print(num2han('12305'))
    # print(num2han('12045'))
    # print(num2han('10345'))

    # 五位数，两个零
    # print(num2han('10340'))
    # print(num2han('10305'))
    # print(num2han('10045'))
    # print(num2han('12040'))
    # print(num2han('12005'))
    # print(num2han('12300'))

    # 五位数，三个零
    # print(num2han('10040'))
    # print(num2han('10005'))
    # print(num2han('10300'))
    # print(num2han('12000'))

    # 五位数，四个零
    # print(num2han('10000'))









