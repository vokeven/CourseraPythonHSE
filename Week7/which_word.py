# Во входном файле (вы можете читать данные из файла input.txt)
#  записан текст. Словом считается последовательность непробельных
#  подряд идущих символов. Слова разделены одним или большим
# числом пробелов или символами конца строки. Для каждого слова
#  из этого текста подсчитайте, сколько раз оно встречалось в
# этом тексте ранее.

from collections import defaultdict


def main():
    count_word()


def count_word():
    with open('input.txt', encoding='utf-8') as f:
        dic_word = defaultdict(int)
        for word in f.read().split():
            print(dic_word[word], end=' ')
            dic_word[word] += 1


if __name__ == '__main__':
    main()
