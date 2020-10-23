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
    _checkCorners(parms)
    
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
 

def _checkCorner(parms):
    isCorner = True
    cubeFaces = [parms['cube'][x:x+9] for x in range(0,len(parms['cube']),9)]
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
    #front top left vs back top right
    if(front[0] == back[0] or front[1] == back[1] or front[2] == back[2]
        or front[3] == back[3] or front[4] == back[4] or front[5] == back[5]
        or front[6] == back[6] or front[7] == back[7] or front[8] == back[8]
        or front[9] == back[9] or front[10] == back[10] or front[11] == back[11]
        or front[12] == back[12]):
        isCorner = False 
    return isCorner

def _checkEdge(parms):
    isEdge = {'status':''}
     
    
    return isEdge