'''
Created on Nov 17, 2020

@author: capta
'''
import unittest
import RCube.rotate as rotate

class Test(unittest.TestCase):


#Happy path
    def test100_010_RotateRandomCube(self):
        expectedResult = {'status':'rotated','cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED'}
        parms = {'op': 'rotate', 'side':'F','cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_020_RotateFullCube(self):
        expectedResult = {'status':'rotated', 'cube': 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy', 'integrity': '0F3BDBE402C16D85756959CDEE1649281296A8507CDDF29EC328C72CC758DA28'}
        parms = {'op': 'rotate', 'side':'f','cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_030_ExtraParms(self):
        expectedResult = {'status':'rotated','cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED'}
        parms = {'op': 'rotate', 'side':'b','cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
#Sad Path    
    def test900_010_CubeValueMissing(self):
        expectedResult = {'Status':'error: Cube value missing'}
        parms = {'op': 'rotate', 'side':'u', 'cube': '', 'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test900_020_CubeKeyMissing(self):
        expectedResult = {'status':'error: Cube key missing'}
        parms = {'op': 'rotate', 'side':'u','integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test900_030_RotationValueMissing(self):
        expectedResult = {'status': 'error: Rotation value missing'}
        parms = {'op': 'rotate', 'side':'','cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test900_040_RotationKeyMissing(self):
        expectedResult = {'status': 'error: Rotation key missing'}
        parms = {'op': 'rotate','cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test900_050_IntegrityValueMissing(self):
        expectedResult = {'status': 'error: Integrity value missing'}
        parms = {'op': 'rotate','side':'u','cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': ''}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)  
    def test900_060_IntegrityKeyMissing(self):
        expectedResult = {'status': 'error: Integrity key missing'}
        parms = {'op': 'rotate','cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo','side':'u'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
#         
# #unit tests
#     def test200_010_RotationValue_f(self):
#         expected = {'cube': 'ooooooooowggwggwggrrrrrrrrrbbybbybbywwwwwwbbbgggyyyyyy', 'integrity': '8449F88B8986E08AA51135B292FE968A6EB10050FC880348486EF853BC10A60B', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'f', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_020_RotationValue_F(self):
#         expected = {'cube': 'oooooooooyggyggyggrrrrrrrrrbbwbbwbbwwwwwwwgggbbbyyyyyy', 'integrity': '0725FE3DE940D22412488858679E49038627A91F615FE641A3CA897B08F14C09', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'F', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_030_RotationValue_r(self):
#         expected = {'cube': 'ooyooyooygggggggggrwwrwwrwwbbbbbbbbbwwwwwwooorrryyyyyy', 'integrity': 'E12EB8E84A67626CCC8AC3DDFB61D714B6BD7624ED08B9CAE2789FFE016276AF', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'r', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_040_RotationValue_R(self):
#         expected = {'cube': 'oowoowoowgggggggggyrryrryrrbbbbbbbbbwwwwwwrrroooyyyyyy', 'integrity': 'B621AC498B7852185B388A6F8A165D7D8086ABBEC7240ED2EF82CD41B34179A8', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'R', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_050_RotationValue_b(self):
#         expected = {'cube': 'oooooooooggyggyggyrrrrrrrrrwbbwbbwbbgggwwwwwwyyyyyybbb', 'integrity': 'CF7F7CA7F091782686E19721F50C78B9D46408A00A992E414D8B2D33C999D9B9', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'b', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_060_RotationValue_B(self):
#         expected = {'cube': 'oooooooooggwggwggwrrrrrrrrrybbybbybbbbbwwwwwwyyyyyyggg', 'integrity': '0734348E61CFFD1BFDDD3989819FC035ED5128230E2A04B4C1346BE1086934E1', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'B', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_070_RotationValue_l(self):
#         expected = {'cube': 'woowoowoogggggggggrryrryrrybbbbbbbbbrwwrwwrwwoyyoyyoyy', 'integrity': '50FAFE62BF3BB0CF259572E7992AC528A4DFEE0BEB8B0F4EAC768E68262262D1', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'l', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_080_RotationValue_L(self):
#         expected = {'cube': 'yooyooyoogggggggggrrwrrwrrwbbbbbbbbbowwowwowwryyryyryy', 'integrity': 'C323A402B51C4594101DB8EF9DD2808100987459684AB6C7B433D4A54D3DD605', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'L', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_090_RotationValue_t(self):
#         expected = {'cube': 'gggoooooorrrggggggbbbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'E03151E1977723626C4896A60618759D4821F62EAF753955D97B8B70DDA2DE0B', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 't', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def test200_100_RotationValue_T(self):
#         expected = {'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'T', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def testRotationValue_u(self):
#         expected = {'cube': 'oooooobbbggggggooorrrrrrgggbbbbbbrrrwwwwwwwwwyyyyyyyyy', 'integrity': 'BA29EA321B8E33BF21FFCFFBA10A0F81509AEC5208BC37179A4C613093B0FEFD', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'u', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)
#     
#     def testRotationValue_U(self):
#         expected = {'cube': 'oooooogggggggggrrrrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy', 'integrity': '72BD1F1E2822F5FE5A0EB5A75F6E926709A2FD455503016F549EC4E449F954B6', 'status': 'rotated'}
#         parms = {'op': 'rotate', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'side': 'U', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
#         actual = rotate._rotate(parms)
#         self.assertEqual(expected, actual)