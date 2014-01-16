# -*- coding: utf-8 -*-
import sys,os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pyHannanum.morpheme import Analyzer, NOUN_EXTRACTOR

if __name__ == '__main__':
    analysis = Analyzer()
    analysis.set_analysis_type(NOUN_EXTRACTOR)
    for line in sys.stdin:
        if line == '\n' or line.startswith('    '):
            continue
        line = line.decode('utf-8')
        line = analysis.filtering_by_tag(line)
        sys.stdout.write(' '.join(line))
        sys.stdout.write('\n')
