import hashlib
import RCube.check as check
#from test.test_set import faces
rotations = ['f','F','b','B','r','R', 't','T','u','U']

def _rotate(parms):
    if(not('cube' in parms)): 
        return {'status': 'error: Cube key missing'}
    if(parms['cube'] == ''): 
        return {'status': 'error: Cube value missing'}
    if(not('integrity' in parms)): 
        return {'status': 'error: Integrity key missing'}
    if(parms['integrity'] == ''): 
        return {'status': 'error: Integrity value missing'}
    if(not('side' in parms)):
            return {'status': 'error: Rotation key missing'}
    if(parms['side'] == ''):
            return {'status': 'error: Rotation value missing'}
    if(not(parms['side'] in rotations)):
            return {'status': 'error: Rotation value not in library'}
   
    cubeIsValid = check._check(parms)
    facesofCube = [parms['cube'][i:i+9] for i in range(0, len(parms['cube']), 9)]
   
    if('error' in cubeIsValid['status']): 
        return cubeIsValid
    #Front
    elif (parms['side'] == 'f' or parms['side'] == 'F'):
        rotateCube = _frontRotation(facesofCube, parms['side'])
    #Back
    elif (parms['side'] == 'b' or parms['side'] == 'B'):
        rotateCube = _backRotation(facesofCube, parms['side'])
    #Left
    elif (parms['side'] == 'l' or parms['side'] == 'L'):
        rotateCube = _leftRotation(facesofCube, parms['side'])
    #Right
    elif (parms['side'] == 'r' or parms['side'] == 'R'):
        rotateCube = _rightRotation(facesofCube, parms['side'])
    #Top
    elif (parms['side'] == 't' or parms['side'] == 'T'):
        rotateCube = _topRotation(facesofCube, parms['side'])
    #Under
    elif (parms['side'] == 'u' or parms['side'] == 'U'):
        rotateCube = _underRotation(facesofCube, parms['side'])
        
    cubeBytes = bytes(rotateCube['rotateCube'], 'utf-8')
    integrity = hashlib.sha256(cubeBytes).hexdigest().upper()
    return(integrity)
    print(rotateCube['rotateCube'])
    #return {'status':'rotated','cube': rotateCube['rotateCube'], 'integrity':integrity}
    
def _frontRotation(facesofCube = [], direction =''):
    if(len(facesofCube == 0)):
        return {'error': 'missing input'}
    if(direction == ''): 
        return {'error': 'missing input'}
    rotateCube = ''
    #Make cube lists to manipulate characters
    for face in range(0,6):
        facesofCube[face] = list(facesofCube[face])
    
    top = [facesofCube[4][6], facesofCube[4][7], facesofCube[4][8]]
    bottom = [facesofCube[5][0], facesofCube[5][1], facesofCube[5][2]]
    left = [facesofCube[3][2], facesofCube[3][5], facesofCube[3][8]]
    right = [facesofCube[1][0], facesofCube[1][3], facesofCube[1][6]]
    #Upper and lower case check
    if (direction.islower()):
        #right rotation
        index = 0
        for cubeFace in top:
            facesofCube[1][index] = face
            if index == 6: break
            index += 3 #Get indices 0,3 and 6
        for cubeFace in left:
            facesofCube[4][index] = face
            index += 1 #Get indices 6,7 and 8
        index = 0
        for cubeFace in right:
            facesofCube[5][index] = face
            if index == 2: break
            index += 1 #Get indices 0,1 and 2
        for cubeFace in bottom:
            facesofCube[3][index] = face
            index += 3 #Get indices 2,5 and 8
    else:
        #left rotation
        index = 0
        for cubeFace in bottom:
            facesofCube[1][index] = face
            if index == 6: break
            index += 3 #Get indices 0,3 and 6
        for cubeFace in right:
            facesofCube[4][index] = face
            index += 1 #Get indices 6,7 and 8
        index = 0
        for cubeFace in left:
            facesofCube[5][index] = face
            if index == 2: break
            index += 1 #Get indices 0,1 and 2
        for cubeFace in top:
            facesofCube[3][index] = face
            index += 3 #Get indices 2,5 and 8 
    
    facesofCube[0] = _centerRotation(facesofCube[0], direction)
    for cubeFace in facesofCube:
        rotateCube += ''.join(cubeFace)
    return{'rotateCube':rotateCube}
    
def _backRotation(facesofCube = [], direction =''):
    if(len(facesofCube == 0)): return {'error': 'missing input'}
    if(direction == ''): return {'error': 'missing input'}
        
    rotateCube = ''
    for face in range(0,6):
        facesofCube[face] = list(facesofCube[face])
        
        #Make cube lists to maniputlate characters
    center = 2
    top = [facesofCube[4][0], facesofCube[4][1], facesofCube[4][2]]
    bottom = [facesofCube[5][6], facesofCube[5][7], facesofCube[5][8]]
    left = [facesofCube[1][2], facesofCube[1][5], facesofCube[1][8]]
    right = [facesofCube[3][0], facesofCube[3][3], facesofCube[3][6]]

    #Upper and lower case check
    if (direction.islower()):
        #right rotation
        index = 0
        for cubeFace in top:
            facesofCube[3][index] = face
            if index == 6: break
            index += 3 #Get indices 0,3 and 6
        index = 6
        for cubeFace in right:
            facesofCube[5][index] = face
            index += 1 #Get indices 6,7 and 8
        index = 2
        for cubeFace in bottom:
            facesofCube[1][index] = face
            index += 3 #Get indices 0,1 and 2
        for cubeFace in left:
            facesofCube[4][index] = face
            index += 1 #Get indices 2,5 and 8
    else:
        #left rotation
        index = 0
        for cubeFace in bottom:
            facesofCube[3][index] = face
            if index == 6: break
            index += 3 #Get indices 0,3 and 6
        index = 6
        for cubeFace in left:
            facesofCube[5][index] = face
            index += 1 #Get indices 6,7 and 8
        index = 2
        for cubeFace in right:
            facesofCube[1][index] = face
            index += 3 #Get indices 0,1 and 2
        index = 0
        for cubeFace in top:
            facesofCube[4][index] = face
            index += 1 #Get indices 2,5 and 8 
    
    facesofCube[center] = _centerRotation(facesofCube[center], direction)
    for cubeFace in facesofCube:
        rotateCube += ''.join(cubeFace)
    return{'rotateCube':rotateCube}
    
def _leftRotation(facesofCube = [], direction =''):
    if(len(facesofCube == 0)): 
        return {'error': 'missing input'}
    if(direction == ''): 
        return {'error': 'missing input'}
        
    rotateCube = ''
    for face in range(0,6):
        facesofCube[face] = list(facesofCube[face])
        
    #Make cube lists to maniputlate characters
    top = [facesofCube[4][0], facesofCube[4][3], facesofCube[4][6]]
    bottom = [facesofCube[5][0], facesofCube[5][3], facesofCube[5][6]]
    left = [facesofCube[2][2], facesofCube[2][5], facesofCube[2][8]]
    right = [facesofCube[0][0], facesofCube[0][3], facesofCube[0][6]]

    #Upper and lower case check
    if (direction.islower()):
        #right rotation
        index = 0
        for cubeFace in top:
            facesofCube[0][index] = face
            index += 3 #Get indices 0,3 and 6
        index = 0
        for cubeFace in right:
            facesofCube[5][index] = face
            index += 3 #Get indices 6,7 and 8
        index = 2
        for cubeFace in bottom:
            facesofCube[2][index] = face
            index += 3 #Get indices 0,1 and 2
        index = 0
        for cubeFace in left:
            facesofCube[4][index] = face
            index += 3 #Get indices 2,5 and 8
    else:
    #left rotation
        index = 0
        for cubeFace in bottom:
            facesofCube[0][index] = face
            index += 3 #Get indices 0,3 and 6
        index = 0
        for cubeFace in left:
            facesofCube[5][index] = face
            index += 3 #Get indices 6,7 and 8
        index = 2
        for cubeFace in top:
            facesofCube[2][index] = face
            index += 3 #Get indices 0,1 and 2
        index = 0
        for cubeFace in right:
            facesofCube[4][index] = face
            index += 3 #Get indices 2,5 and 8 
    
    facesofCube[3] = _centerRotation(facesofCube[3], direction)
    for cubeFace in facesofCube:
        rotateCube += ''.join(cubeFace)
    return{'rotateCube':rotateCube}
    
def _rightRotation(facesofCube = [], direction =''):
    if(len(facesofCube == 0)): return {'error': 'missing input'}
    if(direction == ''): return {'error': 'missing input'}
        
    rotateCube = ''
    for face in range(0,6):
        facesofCube[face] = list(facesofCube[face])
        
    #Make cube lists to manipulate characters
    top = [facesofCube[4][2], facesofCube[4][5], facesofCube[4][8]]
    bottom = [facesofCube[5][2], facesofCube[5][5], facesofCube[5][8]]
    left = [facesofCube[0][2], facesofCube[0][5], facesofCube[0][8]]
    right = [facesofCube[2][0], facesofCube[2][3], facesofCube[2][6]]

    #Upper and lower case check
    if (direction.islower()):
        #right rotation
        index = 0
        for cubeFace in top:
            facesofCube[2][index] = face
            index += 3 #Get indices 0,3 and 6
        index = 2
        for cubeFace in right:
            facesofCube[5][index] = face
            index += 3 #Get indices 6,7 and 8
        index = 2
        for cubeFace in bottom:
            facesofCube[0][index] = face
            index += 3 #Get indices 0,1 and 2
        for cubeFace in left:
            facesofCube[4][index] = face
            index += 3 #Get indices 2,5 and 8
    else:
        #left rotation
        index = 0
        for cubeFace in bottom:
            facesofCube[2][index] = face
            index += 3 #Get indices 0,3 and 6
        index = 2
        for cubeFace in left:
            facesofCube[5][index] = face
            index += 3 #Get indices 6,7 and 8
        index = 2
        for cubeFace in top:
            facesofCube[0][index] = face
            index += 3 #Get indices 0,1 and 2
        index = 0
        for cubeFace in right:
            facesofCube[4][index] = face
            index += 3 #Get indices 2,5 and 8 
    
    facesofCube[1] = _centerRotation(facesofCube[1], direction)
    for cubeFace in facesofCube:
        rotateCube += ''.join(cubeFace)
    return{'rotateCube':rotateCube}
    
def _topRotation(facesofCube = [], direction =''):
    if(len(facesofCube == 0)): 
        return {'error': 'missing input'}
    if(direction == ''): 
        return {'error': 'missing input'}
        
    rotateCube = ''
    for face in range(0,6):
        facesofCube[face] = list(facesofCube[face])
        
    #Make cube lists to manipulate characters
    top = [facesofCube[2][0], facesofCube[2][1], facesofCube[2][2]]
    bottom = [facesofCube[0][0], facesofCube[0][1], facesofCube[0][2]]
    left = [facesofCube[3][0], facesofCube[3][1], facesofCube[3][2]]
    right = [facesofCube[1][0], facesofCube[1][1], facesofCube[1][2]]

    #Upper and lower case check
    if (direction.islower()):
        #right rotation
        index = 0
        for cubeFace in top:
            facesofCube[1][index] = face
            index += 1 #Get indices 0,3 and 6
        index = 0
        for cubeFace in right:
            facesofCube[0][index] = face
            index += 1 #Get indices 6,7 and 8
        index = 0
        for cubeFace in bottom:
            facesofCube[3][index] = face
            index += 1 #Get indices 0,1 and 2
        index = 0
        for cubeFace in left:
            facesofCube[2][index] = face
            index += 1 #Get indices 2,5 and 8
    else:
    #left rotation
        index = 0
        for cubeFace in bottom:
            facesofCube[1][index] = face
            index += 1 #Get indices 0,3 and 6
        index = 0
        for cubeFace in left:
            facesofCube[0][index] = face
            index += 1 #Get indices 6,7 and 8
        index = 0
        for cubeFace in top:
            facesofCube[3][index] = face
            index += 1 #Get indices 0,1 and 2
        index = 0
        for cubeFace in right:
            facesofCube[2][index] = face
            index += 1 #Get indices 2,5 and 8 
    
    facesofCube[4] = _centerRotation(facesofCube[4], direction)
    for cubeFace in facesofCube:
        rotateCube += ''.join(cubeFace)
    return{'rotateCube':rotateCube}
    
def _underRotation(facesofCube = [], direction =''):
    if(len(facesofCube == 0)): return {'error': 'missing input'}
    if(direction == ''): return {'error': 'missing input'}
        
    rotateCube = ''
    for face in range(0,6):
        facesofCube[face] = list(facesofCube[face])
        
    #Make cube lists to manipulate characters
    top = [facesofCube[0][6], facesofCube[0][7], facesofCube[0][8]]
    bottom = [facesofCube[2][6], facesofCube[2][7], facesofCube[2][8]]
    left = [facesofCube[3][6], facesofCube[3][7], facesofCube[3][8]]
    right = [facesofCube[1][6], facesofCube[1][7], facesofCube[1][8]]

    #Upper and lower case check
    if (direction.islower()):
        #right rotation
        index = 6
        for cubeFace in top:
            facesofCube[1][index] = face
            index += 1 #Get indices 0,3 and 6
        index = 6
        for cubeFace in right:
            facesofCube[3][index] = face
            index += 1 #Get indices 6,7 and 8
        index = 6
        for cubeFace in bottom:
            facesofCube[3][index] = face
            index += 1 #Get indices 0,1 and 2
        index = 6
        for cubeFace in left:
            facesofCube[0][index] = face
            index += 1 #Get indices 2,5 and 8
    else:
        #left rotation
        index = 6
        for cubeFace in bottom:
            facesofCube[0][index] = face
            index += 1 #Get indices 0,3 and 6
        index = 6
        for cubeFace in left:
            facesofCube[2][index] = face
            index += 1 #Get indices 6,7 and 8
        index = 6
        for cubeFace in top:
            facesofCube[3][index] = face
            index += 1 #Get indices 0,1 and 2
        index = 6
        for cubeFace in right:
            facesofCube[0][index] = face
            index += 1 #Get indices 2,5 and 8 
    
    facesofCube[5] = _centerRotation(facesofCube[5], direction)
    for cubeFace in facesofCube:
        rotateCube += ''.join(cubeFace)
    return {'rotateCube': rotateCube}
    
def _centerRotation(face = [], direction = ''):
    if(len(face) == 0): 
        return{'error':'missing input'}
    if(direction == ''): 
        return {'error': 'missing input'}
    cutCenter = list()
    temp = list()
    for cubies in face:
        temp.append(cubies)
        if (len(temp) == 3):
            cutCenter.append(temp)
            temp = list()
    #Reverse the string and rotate it.
    if (direction.islower()):
        rotateCenter = list(zip(*cutCenter[::-1]))
    #Rotate string and the reverse it
    else:
        rotateCenter = list(zip(*cutCenter))[::-1]
    
    onlyCenter = []
    for sides in rotateCenter:
            for cubies in sides:
                    onlyCenter.append(cubies)
    return onlyCenter
