from builtins import None

def _create(parms):
    try:
        if parms['faces'] == '' or parms['faces'] == None:
            cube = 'gybwro'
        else
            cube = parm['faces']    
    except:
            cube = 'gybwro'    
    output = ''
    for face in cube:
        if (not(len(cube) == 6):
            return ('status': 'error: Incorrect length for faces') 
        if (cube.count(face) > 1):
                return ('status': 'error: Duplicate Faces')
        output += (face*9)
    bytestring = bytes['output'], 'utf-8')
    result['integrity'] = hashlib.sha256(bytestring).hexdigest().upper()
    return result