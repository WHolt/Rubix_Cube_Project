import hashlib
def _check(parms):
    result = {'status': ''}
#     try:
#         if(parms['cube']== '' or parms['cube'] == None):
#             result['status'] = 'error: No Cube'
#     
#     except:
#         return result
#     try:
#     bytestring = bytes(output, 'utf-8')
#     result['integrity'] = hashlib.sha256(bytestring).hexdigest().upper()
    return result

def _checkCorner(parms):
    corner = {'status':''}
#     try:
#     except:
#         
    return corner

def _checkEdge(parms):
    edge = {'status':''}
#     try:
#     except:
    return edge