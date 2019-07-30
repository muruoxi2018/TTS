from os import path
import codecs
import winsound

class Hanzi2Pinyin():
    def __init__(self):
        self.table = {}
        try:
            fp = codecs.open(path.join(path.dirname(__file__), 'pinyin.txt'), 'r', 'utf-8')
        except IOError:
            raise Exception("Can't load data from pinyin.txt")
        except UnicodeDecodeError:
            raise Exception("Can't decode data from pinyin.txt")
        else:
            for l in fp.readlines():
                self.table[l[0]] = l[1:-1]
            fp.close()

    def convert(self, value):
        pinyin = []
        tASCII = ''
        # 字符检查
        for c in value.lower() + ' ': # 加个空格多一次循环 修正尾部字符丢失问题
            i = ord(c)
            if (i >= 48 and i <= 57) or (i >= 97 and i <= 122): # 48-57[0-9]   97-122[a-z]
                tASCII += c
                continue

            tASCII and pinyin.append(tASCII)
            tASCII = ''

            if c in self.table:
                pinyin.append(self.table[c])

        return pinyin

# 播放wav
def play(word):
    p = Hanzi2Pinyin().convert(str(word))
    for name in p:
        winsound.PlaySound(path.join(path.dirname(__file__),  'yyk\\{0}.wav'.format(name) ), winsound.SND_FILENAME)

def main():
    string = input('请输入要转换为语音的中文文本：\n')
    print()
    print('*'*12)
    print('待转换的语音为：',string)
    print('*'*12)
    play(string)

if __name__ == '__main__':
    main()
