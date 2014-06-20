# -*- coding: utf-8 -*-
"""
This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation.
"""

import os
import string

classpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
            '../../', 'jar/jhannanum.jar'))
os.environ['CLASSPATH'] = classpath

from jnius import autoclass
POS_TAGGER, MORPH_ANALYZER, NOUN_EXTRACTOR, POS_SIMPLE_09, POS_SIMPLE_22 = range(1, 6)
jwkff = autoclass('kr.ac.kaist.swrc.jhannanum.hannanum.WorkflowFactory')
jboolean = autoclass('java.lang.Boolean')

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Analyzer(object):
    __metaclass__ = Singleton

    def __init__(self, analysis_type=POS_TAGGER):
        assert analysis_type in range(1, 6)
        self.anlysis_type = analysis_type
        self.wf = jwkff.getPredefinedWorkflow(analysis_type)
        self.wf.activateWorkflow(jboolean.TRUE)

    def set_analysis_type(self, analysis_type):
        self.anlysis_type = analysis_type
        self.wf = jwkff.getPredefinedWorkflow(analysis_type)
        self.wf.activateWorkflow(jboolean.TRUE)

    def analysis(self, sentences, tags=None, analysis_type=None):
        if analysis_type:
            self.set_analysis_type(analysis_type)
        return self.filtering_by_tag(sentences, tags=None)

    def _analysis(self, sentences):
        try:
            self.wf.analyze(sentences)
        except Exception as e:
            print(e)
        return self.wf.getResultOfDocument()

    def preprossing(self, rawresult):
        terms = filter(lambda x: len(x) > 1,
                       map(string.split, rawresult.split('\n\n')))
        word_taggedwords = []
        for term in terms:
            taggedword = []
            for r in term[1:]:
                taggedword.extend(r.split('+') if '+' in r else [r])
            word_taggedwords.append((term[0], taggedword))
        #print word_taggedwords
        return word_taggedwords

    def get_taggedwords(self, sentences):
        taggedwords = []
        for word_taggedword in self.preprossing(self._analysis(sentences)):
            taggedwords.extend(word_taggedword[1])
        return taggedwords

    def filtering_by_tag(self, sentences, tags=None):
        taggedwords = self.get_taggedwords(sentences)
        if tags:
            return [taggedword.split('/')[0] for taggedword in taggedwords if taggedword.split('/')[1] in tags]
        return [taggedword.split('/')[0] for taggedword in taggedwords]


    def get_words(self, sentences):
        word_taggedwords = self.preprossing(self._analysis(sentences))
        return [word_taggedword[0] for word_taggedword in word_taggedwords]

if __name__ == '__main__':
    sents = u'롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다.'
    analyzer = Analyzer(POS_TAGGER)
    for i in  analyzer.filtering_by_tag(sents, tags=['ncpa', 'ncn']):
        print(i)

