# -*- coding: utf-8 -*-

import unittest

from pyHannanum.morpheme import Analyzer
from pyHannanum.morpheme import NOUN_EXTRACTOR,POS_SIMPLE_09, POS_TAGGER

class Test(unittest.TestCase):
    def setUp(self):    
        self.analyzer = Analyzer()
        
    def __test_pos_simple_09(self):
        analyzer = Analyzer()
        analyzer.set_analysis_type(POS_SIMPLE_09)
        s = u'학교에 가다.'
        self.assertEquals(['학교에', '가다', '.'], analyzer.get_words(s))

    def test_filtering_by_tag(self):
        analyzer = Analyzer() 
        analyzer.set_analysis_type(POS_TAGGER)
        s = u'롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다.'
        self.assertEquals(['롯데마트', '판매', '흑마늘', '양념', '치킨', '논란'],
                          analyzer.analysis(s, tags=['ncpa', 'ncn']))
                          
    def __test_noun_extractor(self):
        analyzer = Analyzer() 
        analyzer.set_analysis_type(NOUN_EXTRACTOR)
        s = u'롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다.'
        self.assertEquals(['롯데마트', '판매', '흑마늘', '양념', '치킨', '논란'],
                                  analyzer.analysis(s))

if __name__ == '__main__':
    unittest.main()
