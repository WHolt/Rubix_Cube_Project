# SoftwareProcessRCube
Software Process assignment: Rubik's cube

This project is the starter code for assignments in
COMP5700/5703/6700/6706  Software Process.

Notes:
1)  Pull this code to GitHub Classroom
2)  Change "manifest.yml" to reflect your AU username
    Line 3:  is -> name: umphrdaRubikCube    should be -> name: username-rcube
3)  "dispatch.py" is the dispatching function for the microservice.  It receives 
the query string portion of the URL in Python dictionary format and routes it to
methods that are stubbed.  You should not have to modify dispatch.py; you _will_,
ultimately, have to modify the stubbed methods.
    
    For example, an HTTP/HTTPS request consisting the URL below
         https://username-rcube.us-south.cf.appdomain.cloud/rcube?op=create
    will result in {'op':'create'} being passed to _dispatch() as the value of 
    "parm".  _dispatch(), in turn, calls _create().   _dispatch() converts the
    result is receives from _create() to a string, which is returned as the
    response to the HTTP/HTTPS request.
    
4)  Place your production code in the body of the "RCube" directory.
5)  Place your test code in the "test" directory

