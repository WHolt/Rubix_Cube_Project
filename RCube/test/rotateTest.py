'''
Created on Nov 17, 2020

@author: capta
'''
import unittest
import RCube.rotate as rotate

class Test(unittest.TestCase):


#Happy path
    def test100_010_RotateRandomCube(self):
        expectedResult = {'status':'rotated','cube': 'oggoggoggyggyrryrrrrrbbbbbbbbwoowoowwwwwwwgrrbooyyyyyy', 'integrity': '28DB9AFFF99873020CFE0315DF48F726CC758A35A403D75E28CDDE2ED297AF7A'}
        parms = {'op': 'rotate', 'side':'F','cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': 'C2541978094B8FF38D7F143F1E3608F90565CF6501215D597E7E3DDD5D4F65B4'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_020_RotateFullCube(self):
        expectedResult = {'status':'rotated', 'cube': 'ggoggoggowggwrrwrrrrrbbbbbbbbyooyooywwwwwwboogrryyyyyy', 'integrity': 'B66B9AF84D6C2C52B5CA005F981E3FC92E9EA78DDB815904769186F1752282C6'}
        parms = {'op': 'rotate', 'side':'f','cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': 'C2541978094B8FF38D7F143F1E3608F90565CF6501215D597E7E3DDD5D4F65B4'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_030_ExtraParms(self):
        expectedResult = {'status':'rotated','cube': 'oooggggggggyrryrrybbrbbrbbrwbbwoowoogrrwwwwwwyyyyyyboo', 'integrity': '8A799EC6B4599B137ABA4AB532541DC46004CFB90DF9FDCA026D4ECDFB5EF48F'}
        parms = {'op': 'rotate', 'side':'b','cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': 'C2541978094B8FF38D7F143F1E3608F90565CF6501215D597E7E3DDD5D4F65B4'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
#Sad Path    
    def test900_010_CubeValueMissing(self):
        expectedResult = {'status':'error: Cube value missing'}
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
    
    def test900_045_RotationValueFailed(self):
        expectedResult = {'status': 'error: Rotation value not in library'}
        parms = {'op': 'rotate', 'side':'p','cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
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
        
# #unit tests
    def unit_test100_RotationValue_f(self):
        expected = {'cube': 'ooooooooowggwggwggrrrrrrrrrbbybbybbywwwwwwbbbgggyyyyyy', 'integrity': '8449F88B8986E08AA51135B292FE968A6EB10050FC880348486EF853BC10A60B', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'f', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest105_RotationValue_F(self):
        expected = {'cube': 'oooooooooyggyggyggrrrrrrrrrbbwbbwbbwwwwwwwgggbbbyyyyyy', 'integrity': '0725FE3DE940D22412488858679E49038627A91F615FE641A3CA897B08F14C09', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'F', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest110_RotationValue_r(self):
        expected = {'cube': 'ooyooyooygggggggggwrrwrrwrrbbbbbbbbbwwowwowwoyyryyryyr', 'integrity': '84DF9D66A7A22B043BD6B77947DD548ADA1A74091E8F544E31C1DB2B8F4FE5FB', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'r', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest115_RotationValue_R(self):
        expected = {'cube': 'oowoowoowgggggggggyrryrryrrbbbbbbbbbrwwrwwrwwyyoyyoyyo', 'integrity': '112609867666974AACB5AF5F7FBCB3313AF5F8C9C0FEAA4A265089B692132F0B', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'R', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest120_RotationValue_b(self):
        expected = {'cube': 'oooooooooggyggyggyrrrrrrrrrwbbwbbwbbgggwwwwwwyyyyyybbb', 'integrity': 'CF7F7CA7F091782686E19721F50C78B9D46408A00A992E414D8B2D33C999D9B9', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'b', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest125_RotationValue_B(self):
        expected = {'cube': 'oooooooooggbggbggbrrrrrrrrrybbybbybbwwwwwwwwwyyyyyyggg', 'integrity': '89FED513C0F40F3AFFAB4A0C8B9E3D23A780C354AF5D2967D3C8ADA384D21BBE', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'B', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)

    def unittest130_RotationValue_l(self):
        expected = {'cube': 'woowoowoogggggggggrryrryrrybbbbbbbbbrwwrwwrwwoyyoyyoyy', 'integrity': '50FAFE62BF3BB0CF259572E7992AC528A4DFEE0BEB8B0F4EAC768E68262262D1', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'l', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest135_RotationValue_L(self):
        expected = {'cube': 'yooyooyoogggggggggrrwrrwrrwbbbbbbbbbowwowwowwryyryyryy', 'integrity': 'C323A402B51C4594101DB8EF9DD2808100987459684AB6C7B433D4A54D3DD605', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'L', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest140_RotationValue_t(self):
        expected = {'cube': 'gggoooooorrrggggggbbbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'E03151E1977723626C4896A60618759D4821F62EAF753955D97B8B70DDA2DE0B', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 't', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest145_RotationValue_T(self):
        expected = {'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'T', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest150_RotationValue_u(self):
        expected = {'cube': 'oooooobbbggggggooorrrrrrrrrbbbbbbrrrwwwwwwwwwyyyyyyyyy', 'integrity': 'B67C93781FD3959F10A958E403A441E50071A8ECE6E8FBA6B9BC2F23183F9663', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'u', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
    
    def unittest155_RotationValue_U(self):
        expected = {'cube': 'ooooooggggggggggggrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy', 'integrity': '2823610D1C54F7CCED00BE519197FD44D4766CA44C96F6EC2B6404675DCC747D', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'U', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
