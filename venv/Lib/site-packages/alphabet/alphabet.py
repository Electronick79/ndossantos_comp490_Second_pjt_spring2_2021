#!/usr/bin/env python

# alphabet: A string class enhancement.

# The MIT License (MIT)
# 
# Copyright (c) 2018-21 Roberto Reale
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from builtins import chr
from builtins import zip

import re


class alphabet(str):
    def __init__(self, *args, **kwargs):
        super(str, self).__init__() #*args, **kwargs)
        self.__encoding = 'utf-8'

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding):
        self.__encoding = encoding

    def detect_format(self):
        import magic
        with magic.Magic() as m:
            return m.id_buffer(self)

    def _init_google_translator(self):
        try:
            self.translator
        except:
            from googletrans import Translator
            self.translator = Translator()

    def detect_programming_language(self):
        """
        Detect programming language.
        """
        import pygments.lexers
        try:
            return pygments.lexers.guess_lexer(self).name
        except:
            return None

    def detect_natural_language(self):
        """
        Detect natural language.
        """
        self._init_google_translator()
        detected = self.translator.detect(self)
        self.confidence = detected.confidence
        return detected.lang
        
    def translate_natural_language(self, dest='en'):
        """
        Translate natural language.
        """
        self._init_google_translator()
        translated = self.translator.translate(self, dest)
        #self.src = translated.src
        #self.dest = translated.dest
        return translated.text

    def identify(self):
        format = self.detect_format()
        if not re.search('^(ASCII|UTF-8 Unicode) text', format):
            return format
        else:
            language = self.detect_programming_language()
            if not language or language == "Text only":
                language = self.detect_natural_language()
            return language
                
        
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
