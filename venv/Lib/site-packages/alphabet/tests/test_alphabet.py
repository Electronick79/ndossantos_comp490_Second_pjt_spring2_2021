from unittest import TestCase

from alphabet import alphabet

class TestAlphabet(TestCase):
    def test(self):

        key = "foobar"
        s = alphabet("python")
        t = s.obfuscate(key).obfuscate(key)
        self.assertTrue(s == t)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
