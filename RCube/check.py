import hashlib
def _check(parms):
    result = {'status': ''}
    try:
        if(parms['cube'] == '' or parms['cube'] == None): result['status'] = 'error: No Cube'
        if(parms['integrity'] == '' or parms['integrity'] == None): result['status'] = 'error: No Integrity Value'
        if (not(len(parms['cube']) == 54)): result['status'] = 'error: Wrong number of faces'
    except:
        return result
    for face in parms['cube']:
        if (parms['cube'].count(face) > 9): return {'status': 'error: Incorrect number of colors'}
    cubeFaces = [parms['cube'][x:x+9] for x in range(0,len(parms['cube']),9)]
    centerColors = ''
    for face in cubeFaces:
        result = 0
        
    #if (x is in centerColors): return {'status': 'error: Indistinct middle'}
    
    bytestring = bytes(parms['cube'], 'utf-8')
    integrity = hashlib.sha256(bytestring).hexdigest().upper()
    if not(parms['integrity'] == integrity):
        result['status'] = 'Wrong Integrity Value'
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