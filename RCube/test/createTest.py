'''
Created on Oct 6, 2020

@author: Cameron Holt
'''
import unittest
import RCube.create as create

class createTest(unittest.TestCase):
#Happy path
    def test100_010_NominalValueOfFaces(self):
        expectedResult = {'cube': '111111111222222222333333333444444444555555555666666666', 'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED', 'status':'ok'}
        parms = {'op': 'create', 'faces' : '123456' }
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_020_NoValueSpecifiedForFaces(self):
        expectedResult = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 'status':'ok'}
        parms = {'op': 'create', 'faces' : None}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_030_FacesMissingAllTogether(self):
        expectedResult = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 'status':'ok'}
        parms = {'op': 'create'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test100_040_ExtraneousParms(self):
        expectedResult = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 'status':'ok'}
        parms = {'op': 'create', 'f' : '123456'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)    
    
    #def test100_050_
    #Sad Path 900
    
    def test900_010_IncorrectLengthForFaces(self):
        expectedResult = {'status': 'error: Incorrect length for faces'}
        parms = {'op': 'create', 'faces' : '1234567'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test900_020_DuplicateItemInFaces(self):
        expectedResult = {'status': 'error: Duplicate Faces'}
        parms = {'op': 'create', 'faces' : '123455'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test900_030_TooFewItemsInFaces(self):
        expectedResult = {'status': 'error: Incorrect length for faces'}
        parms = {'op': 'create', 'faces' : '12345'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)