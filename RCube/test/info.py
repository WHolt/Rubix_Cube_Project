'''
Created on Oct 6, 2020

@author: capta
'''
import unittest
import RCube.info as info


class Test(unittest.TestCase):


    def test100_010_ShouldReturnMyUserName(self):
        expectedResult = {'user' : cwh0023}
        parms = {'op': 'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)
        