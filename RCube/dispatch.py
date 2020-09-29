import RCube.create as create
import RCube.check as check
import RCube.rotate as rotate
import RCube.scramble as scramble
import RCube.info as info

ERROR01 = 'error: no op is specified'
ERROR02 = 'error: parameter is not a dictionary'
ERROR03 = 'error: op is not legal'
STATUS = 'status'
OP = 'op'
OPS = {
    'create' : create._create,
    'check' : check._check,
    'rotate' : rotate._rotate,
    'scramble' : scramble._scramble,
    'info' : info._info,
    }

def _dispatch(parms = None):

    result = {}
    
    # Validate parm
    if(parms == None):
        result = {STATUS: ERROR01}
    elif(not(isinstance(parms, dict))):
        result = {STATUS: ERROR02}
    elif (not(OP in parms)):
        result = {STATUS: ERROR01}
    elif(not(parms[OP] in OPS)):
        result[STATUS] = ERROR03
    else:
        result = OPS[parms[OP]](parms)
    return result