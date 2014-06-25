# -*- coding: utf-8 -*-
import re
import sys,os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pyHannanum.morpheme import Analyzer, NOUN_EXTRACTOR

custom_stopword = """
오후
연락처
월요일
이용시간
오전
그러나
그래서
소재
정도
우리
우리나라
아침
점심
저녁
분야
세계
대규모
전체
사람
사람들
"""

def load_stopword():
    with open('./pyHannanum/stopword.txt') as f:
        words = f.readlines()
    return map(lambda x: x.strip('\n'), words)

stopword = load_stopword()

def filtering_stopword(word):
    word = re.sub(r'\(|\)|\.|\~|\%|\$|\#', '', word)
    if word.isdigit():
        return ''
    elif word in stopword:
        return ''
    elif word in custom_stopword:
        return ''
    elif len(word) == 3:
        return ''
    else:
        return word

def _main():
    analysis = Analyzer()
    analysis.set_analysis_type(NOUN_EXTRACTOR)
    for line in sys.stdin:
        if not line.strip():
            continue
        line = line.decode('utf-8')
        line = analysis.filtering_by_tag(line)
        line = filter(filtering_stopword, line)
        sys.stdout.write(' '.join(line))
        sys.stdout.write('\n')

if __name__ == '__main__':
    _main()
