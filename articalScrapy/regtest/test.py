import re
#
# line = "xvjialing123"
#
# regex_str = "^x.*"   # "^"代表必须以"^"之后的那个字符开头，"."代表可以是任何字符，"*"代表"*"之前的字符可以出现无数次
# if re.match(regex_str, line):
#     print("True")
# else:
#     print("False")
#
# regex_str = "^x.*3$"
# if re.match(regex_str, line):  # "$"代表以"$"之前的字符结尾
#     print("True")
# else:
#     print("False")
#
# line2 ="booooooooooobbaby123"
# regex_str2 = ".*(b.*b).*"    # 括号的作用是取括号内的子串，这样的结果是"bb",因为这样是贪婪匹配，从右边开始匹配
# regex_str3 = ".*?(b.*?b).*"    # 这样的结果是"booooooooooob",因为"?"的作用是使匹配变为非贪婪匹配，从左边开始匹配
#
# match_obj = re.match(regex_str2, line2)
# match_obj2 = re.match(regex_str3, line2)
#
# print(match_obj.group(1))
# print(match_obj2.group(1))
#
#
# regex_str4 = ".*(b.+b).*"  # "+"的作用是"+"之前的字符至少出现一次
# match_obj4 = re.match(regex_str4, line2)
# print(match_obj4.group(1))
#
# regex_str4 = ".*(b.{2}b).*"  # "{1}"的作用是{1}之前的字符出现一次，{n}的作用是精确匹配前面的字符n次，{n,}的作用是匹配前面的字符出现n次以上
# match_obj4 = re.match(regex_str4, line2)
# print(match_obj4.group(1))
#
# regex_str4 = ".*(b.{2,5}b).*"  # "{1}"的作用是{1}之前的字符出现一次，{n}的作用是精确匹配前面的字符n次，{n,}的作用是匹配前面的字符出现n次以上
# match_obj4 = re.match(regex_str4, line2)
# print(match_obj4.group(1))
#
# line3 = "xvjialing123"
# regex_str5 = "(xvjia|xvjialing)"
# regex_str6 = "(xvjialing|xvjia)"
# match_obj5 = re.match(regex_str5, line3)
# match_obj6 = re.match(regex_str6, line3)
# print(match_obj5.group(1))
# print(match_obj6.group(1))
#
#
# regex_str7 = "((xvjia|xvjialing)123)"
# match_obj7 = re.match(regex_str7, line3)
# print(match_obj7.group(1))
# print(match_obj7.group(2))
#
#
# regex_str5 = "([bnaxbv]vjialing123)"   # "[]"的作用是匹配"[]"中任意一个字符
# match_obj5 = re.match(regex_str5, line3)
# print(match_obj5.group(1))
#
# phone = "18764379242"
# regex_str = "(1[78934][0-9]{9})"   # "[0-9]的作用是0到9随意数字，是一个区间"
# regex_str2 = "(1[78934][^1]{9})"  # "[^1]的作用是除1之外的所有字符"
# match_obj = re.match(regex_str, phone)
# match_obj2 = re.match(regex_str2, phone)
# if match_obj:
#     print(match_obj.group(1))
# if match_obj2:
#     print(match_obj2.group(1))
#
# line = "你 好"
# line2 = "你s好"
# regex_str = "(你\s好)"
# match_obj = re.match(regex_str, line)
# match_obj2 = re.match(regex_str, line2)
# if match_obj:
#     print(match_obj.group(1))
# if match_obj2:
#     print(match_obj2.group(1))
#
# line = "你好"
# regex_str = "([\u4E00-\u9FA5]+)"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))
#
# line = "study in 南京大学"
# regex_str = ".*?([\u4E00-\u9FA5]+大学)"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))
#
# line = "出生于2001年"
# regex_str = ".*?(\d+)年"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))

line = "xxx出生于2001年6月1日"
line2 = "xxx出生于2001/6/1"
line3 = "xxx出生于2001-6-1"
line4 = "xxx出生于2001-06-01"
line5 = "xxx出生于2001-06"
line6 = "xxx出生于2001年6月"
# regex_str = ".*出生于?(\d{4}[年/-]?\d+($|[月/-]\d{1,2}|[月/-]))"
regex_str = ".*出生于?((\d{4})([年/-])(\d{1,2})($|[月/-]\d{1,2}[日]|[月/-]\d{1,2}|[月/-]))"
match_obj = re.match(regex_str, line)
match_obj2 = re.match(regex_str, line2)
match_obj3 = re.match(regex_str, line3)
match_obj4 = re.match(regex_str, line4)
match_obj5 = re.match(regex_str, line5)
match_obj6 = re.match(regex_str, line6)
if match_obj:
    print(match_obj.group(1))
if match_obj2:
    print(match_obj2.group(1))
if match_obj3:
    print(match_obj3.group(1))
if match_obj4:
    print(match_obj4.group(1))
if match_obj5:
    print(match_obj5.group(1))
if match_obj6:
    print(match_obj6.group(1))