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
    cubeCheck = parms['cube']
    if (_checkCorner(cubeCheck) == {'status': 'Impossible corner'}):
        result['status'] = 'Impossible corner'
        return result
    #if (_checkEdge(cubeCheck) == {'status': 'Impossible edge'}):
    #    result['status'] = 'Impossible edge'
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
    cube = [cubeFaces[x:x+9] for x in range(0,len(cubeFaces),9)]
    centerColors = ''
    for face in cube:
        centerColors += face[4]
    #Order for corners is front/back, side, top/bottom
    frontTopLeft = cubeFaces[0] + cubeFaces[29] + cubeFaces[42]
    frontTopRight = cubeFaces[2] + cubeFaces[9] + cubeFaces[44]
    frontBottomLeft = cubeFaces[6] + cubeFaces[35] + cubeFaces[45]
    frontBottomRight = cubeFaces[8] + cubeFaces[15] + cubeFaces[47]
    backTopLeft = cubeFaces[18] + cubeFaces[11] + cubeFaces[38]
    backTopRight = cubeFaces[20] + cubeFaces[27] + cubeFaces[36]
    backBottomLeft = cubeFaces[24] + cubeFaces[17] + cubeFaces[53]
    backBottomRight = cubeFaces[26] + cubeFaces[33] + cubeFaces[51]
    #Corners vs opposite middles 0&2, 1&3 4&5. 
    if (frontTopLeft[0] in centerColors[2] or frontTopLeft[1] in centerColors[1] or frontTopLeft[2] in centerColors[5]
        or frontTopRight[0] in centerColors[2] or frontTopRight[1] in centerColors[3] or frontTopRight[2] in centerColors[5]
        or frontBottomLeft[0] in centerColors[2] or frontBottomLeft[1] in centerColors[1] or frontBottomLeft[2] in centerColors[4] 
        or frontBottomRight[0] in centerColors[2] or frontBottomRight[1] in centerColors[3] or frontBottomRight[2] in centerColors[4]
        or backTopLeft[0] in centerColors[0] or backTopLeft[1] in centerColors[3] or backTopLeft[2] in centerColors[5]
        or backTopRight[0] in centerColors[0] or backTopRight[1] in centerColors[1] or backTopRight[2] in centerColors[5]
        or backBottomLeft[0] in centerColors[0] or backBottomLeft[1] in centerColors[3] or backBottomLeft[2] in centerColors[4]
        or backBottomRight[0] in centerColors[0] or backBottomRight[1] in centerColors[1] or backBottomRight[2] in centerColors[4]):
        isCorner = {'status': 'Impossible corner'}
    else:
        isCorner = {'status': 'Corner exists'}
    return isCorner

def _checkEdge(string):
    isEdge = {'status':''}
    cubeFaces = string
    cube = [cubeFaces[x:x+9] for x in range(0,len(cubeFaces),9)]
    cc = '' #centerColors: 0front, 1right, 2back, 3left, 4top, 5under
    for face in cube:
        cc += face[4]
    ft = cubeFaces[1] + cubeFaces[43] #front top edge
    fl = cubeFaces[3] + cubeFaces[32] #front left edge
    fr = cubeFaces[5] + cubeFaces[12] #front right edge
    fu = cubeFaces[7] + cubeFaces[46] #front under edge
    bt = cubeFaces[19] + cubeFaces[37] #back top edge
    br = cubeFaces[21] + cubeFaces[14] #back left edge
    bl = cubeFaces[23] + cubeFaces[30] #back right edge
    bu = cubeFaces[25] + cubeFaces[52] #back under edge
    rt = cubeFaces[10] + cubeFaces[41] #right top edge 
    ru = cubeFaces[16] + cubeFaces[50] #right under edge
    lt = cubeFaces[28] + cubeFaces[39] #left top edge
    lu = cubeFaces[34] + cubeFaces[48] #left under edge
    #Edges vs opposite middles: 0(front) & 2(back) , 1(right) & 3(left), 4(top) & 5(under)
    if (ft[0] in cc[2] or ft[1] in cc[5] or fl[0] in cc[2] or fl[1] in cc[1] or fr[0] in cc[2]
        or fr[1] in cc[3] or fu[0] in cc[2] or fu[1] in cc[4] or bt[0] in cc[0] or bt[1] in cc[5]
        or bl[0] in cc[0] or bl[1] in cc[1] or br[0] in cc[0] or br[1] in cc[3] or bu[0] in cc[0]
        or bu[1] in cc[4] or rt[0] in cc[3] or rt[1] in cc[5] or ru[0] in cc[3] or ru[1] in cc[4]
        or lt[0] in cc[1] or lt[1] in cc[5] or lu[0] in cc[1] or lu[1] in cc[4]):
            isEdge = {'status': 'Impossible edge'}
    else:
        isEdge = {'status': 'Edge exists'}
    return isEdge