def count_vowels(txt):
    vowels=['a','e','i','o','u']
    count=0
    for i in txt:
        if i in vowels:
            count+=1
    print(count)

count_vowels('Celebration')


import unittest

class Test(unittest.TestCase):

   def test_count_vowels(self):
       Test.assert_equals( count_vowels ( "Celebration" ),5 )
       Test.assert_equals ( count_vowels ( "Palm" ),1 )
       Test.assert_equals ( count_vowels ( "Prediction" ),4 )
       Test.assert_equals ( count_vowels ( "Suite" ),3 )
       Test.assert_equals ( count_vowels ( "Quote" ),3 )
       Test.assert_equals ( count_vowels ( "Portrait" ),3 )
       Test.assert_equals ( count_vowels ( "Steam" ),2 )
       Test.assert_equals ( count_vowels ( "Tape" ),2 )
       Test.assert_equals ( count_vowels ( "Nightmare" ),3 )
       Test.assert_equals ( count_vowels ( "Convention" ),4 )