# -*- coding: utf-8 -*-
import sys,os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pyHannanum.morpheme import Analyzer, NOUN_EXTRACTOR

if __name__ == '__main__':
    analysis = Analyzer()
    analysis.set_analysis_type(NOUN_EXTRACTOR)
    for line in sys.stdin:
        s = line.decode('UTF-8')
        content = s.split('\t')
        d = analysis.filtering_by_tag(content[2])
        new_line = '%s\t%s\t%s\n' %(content[0].encode('utf-8'), content[0].encode('utf-8'),' '.join(d))        
        sys.stdout.write(new_line)
