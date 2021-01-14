import markovify
import jieba
from model_gen import MarkovifyInterface
jieba.setLogLevel("WARNING")

def get_1():
    # Get raw text as string.
    with open("./test/texts/zh_good.txt") as f:
        text = f.read()
    text = " ".join(list(jieba.lcut(text)))
    return text


def get_2():
    # Get raw text as string.
    with open("test/texts/zh_split_vocabulary_good.txt") as f:
        text = f.read()
    return text


inter = MarkovifyInterface()
inter.add_text(get_1(), split_by="\n")
inter.add_text(get_2(), split_by="\n")

# Print five randomly-generated sentences
for i in range(15):
    print(inter.make_sentence().replace(" ", ""))



