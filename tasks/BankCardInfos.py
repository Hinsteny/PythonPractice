#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Hinsteny 2018 ActiveState Software Inc.

""""
处理银行签约信息, 从三个文件中读取信息, 最后拼接update-sql语句, 再写入到文件
考虑到要处理的三个文件都是M级大小, 所以直接全部加载到内存中进行处理
"""

from common import FileUtils

cmf_file_path = "E:/data/bankcardinfo/cmf.csv"
member_file_path = "E:/data/bankcardinfo/member.csv"
channel_member_file_path = "E:/data/bankcardinfo/channel_member.csv"

bank_card_infos = "E:/data/bankcardinfo/bank_cards.sql"

update_sql = "UPDATE tt_bankcard_auth SET member_id = '{0}', legal_user_id = '{1}' WHERE id = '{2}';"


def chanage_file_line_to_map(file_path):
    """加载文件内容, 按行转化为字典"""
    lines = FileUtils.read_file_by_line_to_list(file_path)
    repeat = {}
    result = {}
    print("%s had lines %d" % (file_path, lines.__len__()))
    count = 0
    for item in lines:
        item = item.replace("\"", "").replace("\n", "")
        info = item.split(",")
        if result.__contains__(info[0]):
            repeat[info[0]] = info[1]
        else:
            count = count + 1
            result[info[0]] = info[1]
        # print(item)
    print("%s had items %d, count %d" % (file_path, result.__len__(), count))
    print(repeat)
    return result


def buildCardInfo(bankCards, members, channelMembers):
    lines = []
    for cardId, card in bankCards.items():
        member = members.get(card)
        if member:
            channelMember = channelMembers.get(member)
            if channelMember:
                line = update_sql.format(member, channelMember, cardId)
                lines.append(line)
    return lines


if __name__ == '__main__':
    bankCards = chanage_file_line_to_map(cmf_file_path)
    members = chanage_file_line_to_map(member_file_path)
    channelMembers = chanage_file_line_to_map(channel_member_file_path)

    infos = buildCardInfo(bankCards, members, channelMembers)
    outer = FileUtils.get_file_outer(bank_card_infos)
    for item in infos:
        outer.write(item)
        outer.write("\n")
    outer.close()
    print("Finished!")

