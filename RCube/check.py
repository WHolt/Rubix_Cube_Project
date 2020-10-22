import hashlib
def _check(parms):
    result = {'status': ''}    
    if(('cube' not in parms) or (parms['cube'] == '')):
        result['status'] = 'error: No Cube'
        return result
    if('integrity' not in parms or parms['integrity'] == ''): 
        result['status'] = 'error: No Integrity Value'
        return result
    if (not(len(parms['cube']) == 54)):
        result['status'] = 'error: Wrong number of faces'
        return result
    for face in parms['cube']:
        if (parms['cube'].count(face) > 9): return {'status': 'error: Incorrect number of colors'}
    cubeFaces = [parms['cube'][x:x+9] for x in range(0,len(parms['cube']),9)]
    centerColors = ''
    for face in cubeFaces:
        centerColors += face[4]
    for face in centerColors:
        if(centerColors.count(face) > 1): return {'status': 'error: Indistinct middle'}
    
    bytestring = bytes(parms['cube'], 'utf-8')
    integrity = hashlib.sha256(bytestring).hexdigest().upper()
    if not(parms['integrity'] == integrity):
        result['status'] = 'error: Wrong Integrity Value'
    return result

def _checkCorner(parms):
    isCorner = {'status':''}
    cube = parms['cube']
    #try:
   # except:
         
    return isCorner

def _checkEdge(parms):
    isEdge = False 
#    try:
#    except:
    return isEdge