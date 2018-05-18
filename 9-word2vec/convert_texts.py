import os
import re
import nltk
from nltk.tokenize import TweetTokenizer, sent_tokenize

my_tokenizer = TweetTokenizer(preserve_case=False)

def removeHTML(content):
    withoutNL = re.sub(r"-\n", "", content);
    withoutNL = re.sub(r"\n", " ", withoutNL);
    withoutHTML = re.sub(r"<[^>]*>", "", withoutNL);
#    return withoutHTML.split(".")
    return [my_tokenizer.tokenize(x) for x in nltk.sent_tokenize(withoutHTML)]

with open("fileList.txt") as file_list:
    with open("dataList.txt", "w") as data_list:
        for old_path in file_list.readlines():
            old_path = old_path.strip()
            if old_path:
                new_path = old_path.replace("content", "data")
                with open(old_path) as content_file:
                    sentences = removeHTML(content_file.read())
                    with open(new_path, "w") as data_file:
                        for sentence in sentences:
                            data_file.write(" ".join(sentence) + "\n")
                data_list.write(new_path + "\n")

