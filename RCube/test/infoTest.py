'''
Created on Oct 6, 2020

@author: Cameron Holt
'''
import unittest
import RCube.info as info


class infoTest(unittest.TestCase):


    def test100_010_ShouldReturnMyUserName(self):
        expectedResult = {'user' : 'cwh0023'}
        parms = {'op': 'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_020_ShouldReturnMyUserNameWithExtraParms(self):
        expectedResult = {'user' : 'cwh0023'}
        parms = {'op': 'info', 'op':'create'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)
        