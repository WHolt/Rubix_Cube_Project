import hashlib
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
    face2 = ''
    for face in cubeFaces:
        face2 += face
            
    
            
    
    
    bytestring = bytes(parms['cube'], 'utf-8')
    integrity = hashlib.sha256(bytestring).hexdigest().upper()
    if not(parms['integrity'] == integrity):
        result['status'] = 'error: Wrong Integrity Value'
    return result

def _checkCorner(parms):
    isCorner = {'status':''}
    cube = parms['cube']

         
    return isCorner

def _checkEdge(parms):
    isEdge = False 
#    try:
#    except:
    return isEdge