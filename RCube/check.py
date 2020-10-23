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
    #Run tests to confirm that is a rubik's cube
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
    #Check integrity
    bytestring = bytes(parms['cube'], 'utf-8')
    integrity = hashlib.sha256(bytestring).hexdigest().upper()
    if not(parms['integrity'] == integrity):
        result['status'] = 'error: Wrong Integrity Value'
        return result
    #Check Corners and Edges
    #if (_checkCorner(parms['cube']) == {'status': 'Impossible corner'}):
    #    result['status'] = 'Impossible corner'
    #    return result
        
        
    #Check which pattern is on the cube
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
 

def _checkCorner(string):
    isCorner = {'status':''}
    cubeFaces = string
    #cubeFaces = [cube[x:x+9] for x in range(0,len(cube),9)]
    centerColors = ''
    for face in cubeFaces:
        centerColors += face[4]
    frontTopLeft = cubeFaces[0] + cubeFaces[29] + cubeFaces[42]
    frontTopRight = cubeFaces[2] + cubeFaces[44] + cubeFaces[9]
    frontBottomLeft = cubeFaces[6] + cubeFaces[45] + cubeFaces[35]
    frontBottomRight = cubeFaces[8] + cubeFaces[15] + cubeFaces[47]
    backTopLeft = cubeFaces[11] + cubeFaces[38] + cubeFaces[18]
    backTopRight = cubeFaces[20] + cubeFaces[36] + cubeFaces[27]
    backBottomLeft = cubeFaces[17] + cubeFaces[24] + cubeFaces[53]
    backBottomRight = cubeFaces[26] + cubeFaces[33] + cubeFaces[51]
    front = frontTopLeft + frontTopRight + frontBottomLeft + frontBottomRight
    back = backTopLeft + backTopRight + backBottomLeft + backBottomRight
    #Corners vs opposite middles 0&2, 1&3 4&5
    if (frontTopLeft[0] in centerColors[2] or frontTopRight[1] in centerColors[1] or frontTopRight[2] in centerColors[5]):
        isCorner = {'status': 'Impossible corner'}
    return isCorner

def _checkEdge(parms):
    isEdge = {'status':''}
     
    
    return isEdge