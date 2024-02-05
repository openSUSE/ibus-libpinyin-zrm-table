#!/usr/bin/python3
# 用于转换 rime 自然码词库至 ibus-libpinyin 能导入的格式，并从 libpinyin 词库中提取词组的频率
# 至新词库中
# License: GPL-3.0+

import os, string

# 自然码码表来源： https://github.com/mutoe/rime
file_import1 = "zrm2000.dict.yaml"
# 词组频率来源：https://github.com/libpinyin/libpinyin
# cat gb_char.table gbk_char.table > libpinyin.table
file_import2 = "libpinyin.table"
file_export = "output.txt"

if os.path.exists(file_export):
    os.remove(file_export)

with open(file_import1) as import1:
    for line in import1:
        line1_list = line.split()
        if line[0] == '#' or len(line1_list) < 2 or len(line1_list) >=3:
            continue
        count_cn = len(line1_list[0])
        count_en = len(line1_list[1])
        
        """只保留单字、双字和三字词组"""
        if (count_cn == 1 and count_en == 4 or
            count_cn == 2 and count_en == 5 or
            count_cn == 3 and count_en == 7):
            line1_list.reverse()
            with open(file_import2) as import2:
                for line2 in import2:
                    line2_list = line2.split()
                    if line1_list[1] == line2_list[1]:
                        word_frequency = line2_list[3]
                        break
                    else:
                        word_frequency = 1
                        
                with open(file_export, "a") as export:
                    export.write(line1_list[0] + "\t" + line1_list[1] + "\t" + 
                        str(word_frequency) + "\n")
