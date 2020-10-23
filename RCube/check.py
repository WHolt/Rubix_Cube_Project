import hashlib
#from builtins import True, False
def _check(parms):
    result = {'status': ''}
    #Validating that the cube can be worked on Tests    
    if(('cube' not in parms) or (parms['cube'] == '')): 
        result['status'] = 'error: No Cube'
        return result
    if('integrity' not in parms or parms['integrity'] == ''): 
        result['status'] = 'error: No Integrity Value'
        return result
    if (not(len(parms['cube']) == 54)):
        result['status'] = 'error: Wrong number of faces'
        return result
    #Actually validating what's going on with the cube
    for face in parms['cube']:
        if (parms['cube'].count(face) > 9): return {'status': 'error: Incorrect number of colors'}
    qbbyColors = []
    [qbbyColors.append(x) for x in parms['cube'] if x not in qbbyColors]
    if not(len(qbbyColors) == 6): return {'status': 'error: Incorrect number of colors'}
    cubeFaces = [parms['cube'][x:x+9] for x in range(0,len(parms['cube']),9)]
    centerColors = ''    
    for face in cubeFaces:
        centerColors += face[4]
    for cubie in centerColors:
        if(centerColors.count(cubie) > 1): 
            return {'status': 'error: Indistinct middle'}
    bytestring = bytes(parms['cube'], 'utf-8')
    integrity = hashlib.sha256(bytestring).hexdigest().upper()
    if not(parms['integrity'] == integrity):
        result['status'] = 'error: Wrong Integrity Value'
        return result  
    checkFull = True
    checkCross = True
    checkSpot = True
    for face in cubeFaces:
        spotCheck = face[:4] + face[4+1:]
        if face[2]*9 != face:
            checkFull = False
        if (face[4] != face[1] or face[4] != face[3] or face[4] != face[5] or face[4] != face[7]):
            checkCross = False
        if spotCheck != face[2]*8:
            checkSpot = False
    if checkFull:
        result['status'] ='full'
    elif checkCross:
        result['status'] ='crosses'
    elif checkSpot:
        result['status'] ='spots'
    else:
        result['status'] = 'unknown'
    return result

def _checkCorner(parms):
    isCorner = {'status':''}
    cube = parms['cube']

         
    return isCorner

def _checkEdge(parms):
    isEdge = {'status':''}
     
    
    return isEdge