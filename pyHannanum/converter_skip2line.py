# -*- coding: utf-8 -*-
import sys,os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pyHannanum.morpheme import Analyzer, NOUN_EXTRACTOR

if __name__ == '__main__':
    analysis = Analyzer()
    analysis.set_analysis_type(NOUN_EXTRACTOR)
    i = 0
    for line in sys.stdin:
        i += 1
        if i < 4 or not line.strip():
            continue
#         if i == 1 or i == 3 or not line.strip():
#             continue
        line = line.decode('utf-8')
        words = analysis.filtering_by_tag(line)
        sys.stdout.write(' '.join(words))
        sys.stdout.write('\n')
