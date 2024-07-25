from ltp import LTP
from opencc import OpenCC
import random
import json
import os
from ChineseErrorCorrector.config import LTPPath
from ChineseErrorCorrector.utils import set_seed

ltp = LTP(LTPPath.LTP_MODEL_DIR)
cc = OpenCC('t2s')
set_seed()


class GrammarErrorDat(object):

    def wrong_word(self, line):
        """
        错别字
        :param line:
        :return:
        """
        confuse_set = {}

        with open(os.path.join(LTPPath.LTP_DATA_PATH, 'token_set.txt'), 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line_ in lines:
                temp_line = line_.strip('\n').split('\t')
                ch = temp_line[0]
                if cc.convert(ch) == ch:
                    confuse_set[ch] = []
                    for word in temp_line[1]:
                        new_word = cc.convert(word)
                        if word == new_word:
                            confuse_set[temp_line[0]].append(word)
        line_len = len(line)
        confuse_index = random.randint(0, line_len - 1)
        while confuse_set.get(line[confuse_index]) == None:
            confuse_index = random.randint(0, line_len - 1)
        new_line = {}
        label = []
        source = ""
        target = line
        label.append('correct')
        for j in range(line_len):
            if j == confuse_index:
                confuse_word_set = confuse_set[line[j]]
                new_index = random.randint(0, len(confuse_word_set) - 1)
                source += confuse_word_set[new_index]
                label.append('char_error')
            else:
                source += line[j]
                label.append('correct')
        source += ""
        label.append('correct')
        new_line['source'] = source
        new_line['target'] = target
        new_line['label'] = label
        return new_line['source']

    def lack_word(self, line):
        """
        缺字漏字
        :return:
        """

        result = ltp.pipeline([line], tasks=["cws", "pos"])
        cws = result.cws[0]
        pos = result.pos[0]
        res = list(zip(cws, pos))
        sum_char = 0
        # 如果句子里面有名词或者动词
        for (c, p) in res:
            if p == 'n' or p == 'v':
                sum_char += 1
        if sum_char != 0:
            i_char = 0
            tar_char = random.randint(1, sum_char)
            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')
            for (c, p) in res:
                if p == 'n' or p == 'v':
                    i_char += 1
                    if i_char == tar_char:
                        c_len = len(c)
                        del_index = random.randint(0, c_len - 1)
                        for j in range(c_len):
                            if j == del_index:
                                label[-1] = 'char_append'
                            else:
                                source += c[j]
                                label.append('correct')
                    else:
                        for word in c:
                            source += word
                            label.append('correct')
                else:
                    for word in c:
                        source += word
                        label.append('correct')
            label.append('correct')
            new_line['source'] = source
            new_line['target'] = target
            new_line['label'] = label

            return new_line['source']
        else:
            return None

    def lack_char(self, line):
        """
        缺少标点
        :param line:
        :return:
        """

        punc_list = ['！', '？', '｡', '＂', '＃', '＄', '％', '＆', '＇', '（', '）', '＊', '＋', '，', '－', '／', '：', '；', '＜', '＝',
                     '＞',
                     '＠', '［', '＼', '］', '＾', '＿', '｀', '｛', '｜', '｝', '～', '｟', '｠', '｢', '｣', '､', '、', '〃', '》', '「',
                     '」',
                     '『', '』', '【', '】', '〔', '〕', '〖', '〗', '〘', '〙', '〚', '〛', '〜', '〝', '〞', '〟', '〰', '‘', '‛', '“',
                     '”',
                     '„', '‟']
        sum_char = 0
        for word in line:
            if word in punc_list:
                sum_char += 1
        if sum_char > 0:
            tar_char = random.randint(1, sum_char)

            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')

            i_char = 0
            for word in line:
                if word in punc_list:
                    i_char += 1
                    if i_char == tar_char:
                        label[-1] = 'char_punc_append'
                    else:
                        source += word
                        label.append('correct')
                else:
                    source += word
                    label.append('correct')

            source += ""
            label.append('correct')
            new_line['source'] = source
            new_line['target'] = target
            new_line['label'] = label
            # assert (len(source) - len(label)) == 8
            return new_line['source']
        else:
            return None

    def wrong_char(self, line):
        """
        错用标点
        :param line:
        :return:
        """

        common_punc = {'，': ['。', '、', '；', '？', '：'], '。': ['，', '！', '？', '：', '；'], '？': ['。', '、', '；', '！', '，'],
                       '：': ['。', '、', '；', '？', '，'], '、': ['。', '；', '，']}

        sum_char = 0
        for word in line:
            if word in common_punc:
                sum_char += 1
        if sum_char > 0:
            tar_char = random.randint(1, sum_char)

            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')

            i_char = 0
            for word in line:
                if word in common_punc:
                    i_char += 1
                    if i_char == tar_char:
                        label.append('char_punc_error')
                        new_punc = random.sample(common_punc[word], 1)
                        source += new_punc[0]
                    else:
                        source += word
                        label.append('correct')

                else:
                    source += word
                    label.append('correct')

            source += ""
            label.append('correct')
            new_line['source'] = source
            new_line['target'] = target
            new_line['label'] = label
            # assert (len(source) - len(label)) == 8
            return new_line['source']
        else:
            return None

    def unknow_sub(self, line):
        """
        主语不明
        :param line:
        :return:
        """
        result = ltp.pipeline([line], tasks=["cws", "dep"])
        cws = result.cws[0]
        label = result.dep[0]['label']
        res = list(zip(cws, label))
        sum_sub = 0
        for (c, l) in res:
            if l == 'SBV':
                sum_sub += 1
        if sum_sub != 0:
            i_sub = 0
            tar_sub = random.randint(1, sum_sub)
            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')
            for (c, l) in res:
                if l == 'SBV':
                    i_sub += 1
                    if i_sub == tar_sub:
                        label[-1] = 'miss_sub'
                    else:
                        for word in c:
                            source += word
                            label.append('correct')
                else:
                    for word in c:
                        source += word
                        label.append('correct')
            source += ""
            label.append('correct')
            new_line['source'] = source
            new_line['target'] = target
            new_line['label'] = label
            return new_line['source']
        else:
            return None

    def unknow_pred(self, line):
        """
        谓语残缺
        :param line:
        :return:
        """
        result = ltp.pipeline([line], tasks=["cws", "pos"])
        cws = result.cws[0]
        pos = result.pos[0]
        res = list(zip(cws, pos))
        sum_char = 0
        for (c, p) in res:
            if p == 'v':
                sum_char += 1
        if sum_char != 0:
            i_char = 0
            tar_char = random.randint(1, sum_char)
            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')
            for (c, p) in res:
                if p == 'v':
                    i_char += 1
                    if i_char == tar_char:
                        label[-1] = 'miss_pre'
                    else:
                        for word in c:
                            source += word
                            label.append('correct')
                else:
                    for word in c:
                        source += word
                        label.append('correct')
            source += ""
            label.append('correct')
            new_line['source'] = source
            new_line['target'] = target
            new_line['label'] = label
            return new_line['source']
        else:
            return None

    def lack_obj(self, line):
        """
        缺少宾语
        :param line:
        :return:
        """

        result = ltp.pipeline([line], tasks=["cws", "dep"])
        cws = result.cws[0]
        label = result.dep[0]['label']
        res = list(zip(cws, label))
        sum_obj = 0
        for (c, l) in res:
            if l == 'VOB' or l == 'IOB' or l == 'FOB':
                sum_obj += 1
        if sum_obj != 0:
            i_obj = 0
            tar_obj = random.randint(1, sum_obj)
            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')
            for (c, l) in res:
                if l == 'VOB' or l == 'IOB' or l == 'FOB':
                    i_obj += 1
                    if i_obj == tar_obj:
                        label[-1] = 'miss_obj'
                    else:
                        for word in c:
                            source += word
                            label.append('correct')
                else:
                    for word in c:
                        source += word
                        label.append('correct')
            source += ""
            label.append('correct')
            new_line['source'] = source
            new_line['target'] = target
            new_line['label'] = label
            return new_line['source']
        else:
            return None

    def lack_others(self, line):
        """
        其他成分残缺
        :param line:
        :return:
        """
        result = ltp.pipeline([line], tasks=["cws", "dep", "pos"])
        cws = result.cws[0]
        label = result.dep[0]['label']
        pos = result.pos[0]
        res = list(zip(cws, label, pos))
        sum_other = 0
        for (c, l, p) in res:
            if l != 'VOB' and l != 'IOB' and l != 'FOB' and l != 'SBV' and p != 'v' and l != 'WP':
                sum_other += 1
        if sum_other != 0:
            i_other = 0
            tar_other = random.randint(1, sum_other)
            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')
            for (c, l, p) in res:
                if l != 'VOB' and l != 'IOB' and l != 'FOB' and l != 'SBV' and p != 'v' and l != 'WP':
                    i_other += 1
                    if i_other == tar_other:
                        label[-1] = 'miss_other'
                    else:
                        for word in c:
                            source += word
                            label.append('correct')
                else:
                    for word in c:
                        source += word
                        label.append('correct')
            source += ""
            label.append('correct')
            new_line['source'] = source
            new_line['target'] = target
            new_line['label'] = label
            return new_line['source']
        else:
            return None

    def red_sub(self, line):
        """
        主语多余
        :param line:
        :return:
        """

        result = ltp.pipeline([line], tasks=["cws", "dep", "pos"])
        cws = result.cws[0]
        pos = result.pos[0]
        head = result.dep[0]['head']
        label = result.dep[0]['label']
        sum_sub = 0
        for j in range(len(cws)):
            if pos[j] == 'v' and (label[j] == 'HED' or label[j] == 'COO'):
                temp_j = j - 1
                while temp_j > 0 and label[temp_j] == 'ADV':
                    temp_j -= 1
                if label[temp_j] != 'SBV':
                    sum_sub += 1
        if sum_sub != 0:
            i_sub = 0
            tar_sub = random.randint(1, sum_sub)
            new_line = {}
            labels = []
            add_sub = ''
            flag = 0
            source = ""
            target = line
            labels.append('correct')
            for j in range(len(cws)):
                if pos[j] == 'v' and (label[j] == 'HED' or label[j] == 'COO'):
                    temp_j = j - 1
                    while temp_j > 0 and label[temp_j] == 'ADV':
                        temp_j -= 1
                    if label[temp_j] != 'SBV':
                        i_sub += 1
                        add_index = temp_j
                    if i_sub == tar_sub:
                        temp_index = head[j] - 1
                        while label[temp_index] == 'COO':
                            temp_index = head[temp_index] - 1
                        for m in range(len(cws)):
                            if label[m] == 'SBV' and head[m] == temp_index + 1:
                                flag = 1
                                add_sub = cws[m]
            if flag == 1:
                for j in range(len(cws)):
                    if j == add_index:
                        for word in cws[j]:
                            source += word
                            labels.append('correct')
                        for word in add_sub:
                            source += word
                            labels.append('redu_sub')
                    else:
                        for word in cws[j]:
                            source += word
                            labels.append('correct')
                source += ""
                labels.append('correct')
                new_line['source'] = source
                new_line['target'] = target
                new_line['label'] = labels
                return new_line['source']
            else:
                return None

    def red_fun(self, line):
        """
        虚词多余
        :param line:
        :return:
        """

        result = ltp.pipeline([line], tasks=["cws", "dep", "pos"])
        cws = result.cws[0]
        pos = result.pos[0]
        head = result.dep[0]['head']
        label = result.dep[0]['label']
        sum_emp = 0
        for j in range(len(cws)):
            if (pos[j] == 'a' or pos[j] == 'd' or pos[j] == 'q') and j < len(cws) - 1:
                if cws[j + 1] != '的' and cws[j + 1] != '地':
                    sum_emp += 1
            elif pos[j] == 'v' and j > 0:
                if cws[j - 1] != '所':
                    sum_emp += 1
        if sum_emp != 0:
            i_emp = 0
            tar_emp = random.randint(1, sum_emp)
            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')
            for j in range(len(cws)):
                flag = 0
                if (pos[j] == 'a' or pos[j] == 'd' or pos[j] == 'q') and j < len(cws) - 1:
                    if cws[j + 1] != '的' and cws[j + 1] != '地':
                        i_emp += 1
                        flag = 1
                    else:
                        for word in cws[j]:
                            source += word
                            label.append('correct')
                elif pos[j] == 'v' and j > 0:
                    if cws[j - 1] != '所':
                        i_emp += 1
                        flag = 1
                    else:
                        for word in cws[j]:
                            source += word
                            label.append('correct')
                else:
                    for word in cws[j]:
                        source += word
                        label.append('correct')
                if flag == 1 and i_emp == tar_emp:
                    if pos[j] == 'a' or pos[j] == 'q':
                        for word in cws[j]:
                            source += word
                            label.append('correct')
                        source += '的'
                        label.append('redu_emp')
                    elif pos[j] == 'd':
                        for word in cws[j]:
                            source += word
                            label.append('correct')
                        source += '地'
                        label.append('redu_emp')
                    elif pos[j] == 'v':
                        source += '所'
                        label.append('redu_emp')
                        for word in cws[j]:
                            source += word
                            label.append('correct')
                        source += '的'
                        label.append('redu_emp')
                elif flag == 1:
                    for word in cws[j]:
                        source += word
                        label.append('correct')
            source += ""
            label.append('correct')
            new_line['source'] = source
            new_line['target'] = target
            new_line['label'] = label
            return new_line['source']
        else:
            return None

    def red_component(self, sentence):
        """
           随机添加一个多余的成分：动词、宾语、定语或状语
           :param sentence: 输入的句子
           :return: 添加了多余成分的句子
           """

        # 各种可能添加的多余成分
        # 添加多余的动词
        redundant_verbs = [
            "看着", "尝试", "进行", "思考", "理解", "感知",
            "欣赏", "研究", "探索", "尊重", "忽略", "遵循",
            "挑战", "鼓励", "想象", "建议", "计划", "决定"
        ]

        # 添加多余的宾语
        redundant_objects = [
            "事情", "问题", "情况", "决策", "计划", "挑战",
            "机会", "梦想", "设想", "疑问", "方式", "策略",
            "可能性", "尝试", "方案", "部分", "结果", "选择"
        ]

        # 添加多余的定语
        redundant_adjectives = [
            "美丽的", "快乐的", "悲伤的", "寂静的", "优秀的",
            "明智的", "勇敢的", "复杂的", "微妙的", "决定性的",
            "深份的", "清晰的", "困惑的", "先进的", "古代的",
            "完美的", "普通的", "特别的", "有趣的", "重要的"
        ]

        # 添加多余的状语
        redundant_adverbs = [
            "显然", "突然", "可能", "实际上", "简单地",
            "最终", "同样地", "特别地", "逐渐", "轻易地",
            "积极地", "惊讶地", "明确地", "完全地", "立刻",
            "频繁地", "大约", "恰好", "轻松地", "当然"
        ]

        # 定义可以添加的成分类型
        component_types = ['verb', 'object', 'adjective', 'adverb']

        # 随机选择一个成分
        component_to_add = random.choice(component_types)

        # 根据选择的成分类型，随机选择一个词
        if component_to_add == 'verb':
            word_to_add = random.choice(redundant_verbs)
            position = random.choice(['beginning', 'middle', 'end'])
            if position == 'beginning':
                new_sentence = word_to_add + "，" + sentence
            elif position == 'middle':
                # 在中间插入时，简单的示例是分割句子并添加动词
                parts = sentence.split('，')
                if len(parts) > 1:
                    insert_index = random.randint(0, len(parts) - 1)
                    parts.insert(insert_index, word_to_add)
                    new_sentence = '，'.join(parts)
                else:
                    new_sentence = sentence
            else:
                new_sentence = sentence + "，" + word_to_add
            return new_sentence

        elif component_to_add == 'object':
            word_to_add = random.choice(redundant_objects)
            # 假设始终在句尾添加宾语
            new_sentence = sentence.rstrip('。') + word_to_add + "。"
            return new_sentence

        elif component_to_add == 'adjective':
            word_to_add = random.choice(redundant_adjectives)
            # 假设添加定语到句子的开头
            new_sentence = word_to_add + sentence
            return new_sentence

        elif component_to_add == 'adverb':
            word_to_add = random.choice(redundant_adverbs)
            # 假设始终在句首添加状语
            new_sentence = word_to_add + "，" + sentence
            return new_sentence
        else:
            return None

    def wrong_sentence_order(self, line):
        """
        语序不当
        :param line:
        :return:
        """

        line_split = line.split("，")
        if len(line_split) > 1:
            # 随机选取两句 然后进行反转
            reverse_list = random.sample(range(len(line_split)), 2)

            res_1 = line_split[reverse_list[0]]
            res_2 = line_split[reverse_list[1]]
            line_split[reverse_list[0]] = res_2
            line_split[reverse_list[1]] = res_1

            return '，'.join(line_split)

        else:
            return None

    def wrong_ver_obj(self, line):
        """
        动宾搭配不当
        :param line:
        :return:
        """
        con_v_obj = {}
        with open(os.path.join(LTPPath.LTP_DATA_PATH, 'confuse_v_obj.json'), 'r', encoding='utf-8') as f:
            str = f.read()
            raw_data = json.loads(str)
            for v in raw_data:
                con_v_obj[v] = list(set(raw_data[v]))
        con_obj_v = {}
        with open(os.path.join(LTPPath.LTP_DATA_PATH, 'confuse_obj_v.json'), 'r', encoding='utf-8') as f:
            str = f.read()
            raw_data = json.loads(str)
            for obj in raw_data:
                con_obj_v[obj] = list(set(raw_data[obj]))

        result = ltp.pipeline([line], tasks=["cws", "dep"])
        cws = result.cws[0]
        head = result.dep[0]['head']
        label = result.dep[0]['label']
        res = list(zip(cws, head, label))
        sum_v_obj = 0
        for (c, h, l) in res:
            if l == 'VOB' or l == 'IOB' or l == 'FOB':
                sum_v_obj += 1
        if sum_v_obj != 0:
            i_v_obj = 0
            tar_v_obj = random.randint(1, sum_v_obj)
            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')
            flag = 0
            temp_label = []
            temp_source = []
            for p in range(len(cws)):
                temp_label.append([])
                temp_source.append([])
            temp_index = 0
            for (c, h, l) in res:
                if l == 'VOB' or l == 'IOB' or l == 'FOB':
                    i_v_obj += 1
                    if i_v_obj == tar_v_obj:
                        temp_i = random.randint(0, 1)
                        v = cws[h - 1]
                        obj = c
                        if temp_i == 1:
                            if con_v_obj.get(v) != None:
                                obj_set = con_v_obj[v]
                                if obj in obj_set:
                                    obj_set.remove(obj)
                                if len(obj_set) > 0:
                                    flag = 1
                                    index = random.randint(0, len(obj_set) - 1)
                                    new_obj = obj_set[index]
                                    temp_source[temp_index] = []
                                    temp_label[temp_index] = []
                                    temp_label[h - 1] = []
                                    temp_source[h - 1] = []
                                    for word in new_obj:
                                        temp_source[temp_index].append(word)
                                        temp_label[temp_index].append('coll_vobj')
                                    for word in v:
                                        temp_source[h - 1].append(word)
                                        temp_label[h - 1].append('coll_vobj')
                        else:
                            if con_obj_v.get(obj) != None:
                                v_set = con_obj_v[obj]
                                if v in v_set:
                                    v_set.remove(v)
                                if len(v_set) > 0:
                                    flag = 1
                                    index = random.randint(0, len(v_set) - 1)
                                    new_v = v_set[index]
                                    temp_source[temp_index] = []
                                    temp_label[temp_index] = []
                                    temp_label[h - 1] = []
                                    temp_source[h - 1] = []
                                    for word in new_v:
                                        temp_source[h - 1].append(word)
                                        temp_label[h - 1].append('coll_vobj')
                                    for word in obj:
                                        temp_source[temp_index].append(word)
                                        temp_label[temp_index].append('coll_vobj')
                    else:
                        if temp_source[temp_index] == []:
                            for word in c:
                                temp_source[temp_index].append(word)
                                temp_label[temp_index].append('correct')
                else:
                    if temp_source[temp_index] == []:
                        for word in c:
                            temp_source[temp_index].append(word)
                            temp_label[temp_index].append('correct')
                temp_index += 1

            if flag == 1:
                for j in range(len(cws)):
                    for word in temp_source[j]:
                        source += word
                    for temp_l in temp_label[j]:
                        label.append(temp_l)
                source += ""
                label.append('correct')
                new_line['source'] = source
                new_line['target'] = target
                new_line['label'] = label

                return new_line['source']
        else:
            return None

    def other_wrong(self, line):
        """
        其他搭配不当
        :param line:
        :return:
        """
        con_sub_v = {}
        with open(os.path.join(LTPPath.LTP_DATA_PATH, 'confuse_sub_v.json'), 'r', encoding='utf-8') as f:
            str = f.read()
            raw_data = json.loads(str)
            for sub in raw_data:
                con_sub_v[sub] = list(set(raw_data[sub]))
        con_v_sub = {}
        with open(os.path.join(LTPPath.LTP_DATA_PATH, 'confuse_v_sub.json'), 'r', encoding='utf-8') as f:
            str = f.read()
            raw_data = json.loads(str)
            for v in raw_data:
                con_v_sub[v] = list(set(raw_data[v]))

        result = ltp.pipeline([line], tasks=["cws", "dep"])
        cws = result.cws[0]
        head = result.dep[0]['head']
        label = result.dep[0]['label']
        res = list(zip(cws, head, label))
        sum_sub_v = 0
        for (c, h, l) in res:
            if l == 'SBV':
                sum_sub_v += 1
        if sum_sub_v != 0:
            i_sub_v = 0
            tar_sub_v = random.randint(1, sum_sub_v)
            new_line = {}
            label = []
            source = ""
            target = line
            label.append('correct')
            flag = 0
            temp_label = []
            temp_source = []
            for p in range(len(cws)):
                temp_label.append([])
                temp_source.append([])
            temp_index = 0
            for (c, h, l) in res:
                if l == 'SBV':
                    i_sub_v += 1
                    if i_sub_v == tar_sub_v:
                        temp_i = random.randint(0, 1)
                        v = cws[h - 1]
                        sub = c
                        if temp_i == 1:
                            if con_v_sub.get(v) != None:
                                sub_set = con_v_sub[v]
                                if sub in sub_set:
                                    sub_set.remove(sub)
                                if len(sub_set) > 0:
                                    flag = 1
                                    index = random.randint(0, len(sub_set) - 1)
                                    new_sub = sub_set[index]
                                    temp_source[temp_index] = []
                                    temp_label[temp_index] = []
                                    temp_label[h - 1] = []
                                    temp_source[h - 1] = []
                                    for word in new_sub:
                                        temp_source[temp_index].append(word)
                                        temp_label[temp_index].append('coll_other')
                                    for word in v:
                                        temp_source[h - 1].append(word)
                                        temp_label[h - 1].append('coll_other')
                        else:
                            if con_sub_v.get(sub) != None:
                                v_set = con_sub_v[sub]
                                if v in v_set:
                                    v_set.remove(v)
                                if len(v_set) > 0:
                                    flag = 1
                                    index = random.randint(0, len(v_set) - 1)
                                    new_v = v_set[index]
                                    temp_source[temp_index] = []
                                    temp_label[temp_index] = []
                                    temp_label[h - 1] = []
                                    temp_source[h - 1] = []
                                    for word in new_v:
                                        temp_source[h - 1].append(word)
                                        temp_label[h - 1].append('coll_other')
                                    for word in sub:
                                        temp_source[temp_index].append(word)
                                        temp_label[temp_index].append('coll_other')
                    else:
                        if temp_source[temp_index] == []:
                            for word in c:
                                temp_source[temp_index].append(word)
                                temp_label[temp_index].append('correct')
                else:
                    if temp_source[temp_index] == []:
                        for word in c:
                            temp_source[temp_index].append(word)
                            temp_label[temp_index].append('correct')
                temp_index += 1

            if flag == 1:
                for j in range(len(cws)):
                    for word in temp_source[j]:
                        source += word
                    for temp_l in temp_label[j]:
                        label.append(temp_l)
                source += ""
                label.append('correct')
                new_line['source'] = source
                new_line['target'] = target
                new_line['label'] = label
                return new_line['source']
            return None
        else:
            return None


if __name__ == '__main__':
    cged_tool = GrammarErrorDat()
    print(cged_tool.lack_word("小明住在北京"))

    print(cged_tool.wrong_word("小明住在北京"))

    print(cged_tool.lack_char("小明住在北京"))

    print(cged_tool.wrong_char("小明住在北京"))

    print(cged_tool.unknow_sub("小明住在北京"))

    print(cged_tool.unknow_pred("小明住在北京"))

    print(cged_tool.lack_obj("小明住在北京"))

    print(cged_tool.lack_others("小明住在北京"))

    print(cged_tool.red_sub("小明住在北京"))

    print(cged_tool.red_fun("小明住在北京"))

    print(cged_tool.red_component("小明住在北京"))

    print(cged_tool.wrong_sentence_order("小明住在北京"))

    print(cged_tool.wrong_ver_obj("小明住在北京"))

    print(cged_tool.wrong_ver_obj("小明住在北京"))

    print(cged_tool.other_wrong("小明住在北京"))

    """
    python -m twine upload --repository-url https://upload.pypi.org/legacy/  dist/*
或
twine upload --repository-url https://upload.pypi.org/legacy/  dist/*
    """
