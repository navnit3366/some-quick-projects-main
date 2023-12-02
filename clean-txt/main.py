import re


def clean_text(text: str):
    res1 = re.sub("[ ]{2,}", ' ', str1)
    res1 = re.sub("[\n ]{2,}", '\n', res1)
    return res1


str1 = "rrr  r rr\n\n \n\nr r\n u\n"
res1 = clean_text(str1)
print([str1])
print([res1])
