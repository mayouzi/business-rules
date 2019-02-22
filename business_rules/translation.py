# coding: utf-8

_EN_ZH_CN_MAP = {
    "Is False": "为假",
    "Is True": "为真",
    "Equal To": "等于",
    "Greater Than": "大于",
    "Greater Than Or Equal To": "大于等于",
    "Less Than": "小于",
    "Less Than Or Equal To": "小于等于",
    "Not Equal To": "不等于",
    "Contains": "包含",
    "Does Not Contain": "不包含",
    "Contains All": "包含所有",
    "Is Contained By": "是否包含于",
    "Shares At Least One Element With": "至少有一个交集于",
    "Shares Exactly One Element With": "刚好有一个交集于",
    "Shares No Elements With": "没有交集于",
    "Ends With": "结尾于",
    "Equal To (case insensitive)": "等于(不区分大小写)",
    "Matches Regex": "正则匹配",
    "Non Empty": "不为空",
    "Not Equal To": "不等于",
    "Starts With": "开始于",
}


def get_real_label(label, chinese=False):
    if not chinese:
        return label
    return _EN_ZH_CN_MAP.get(label, label)
