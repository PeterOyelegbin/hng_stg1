# hng_stage1
HNG Backend Stage 1 Task

## Task Description
* Setup a server (Host)

* Create an (GET) api endpoint that returns the following json response: {"slackUsername": String, "backend": Boolean, "age": Integer, "bio": String}
** SlackUsername should be a string datatype and your slack username
** Backend should be boolean datatype
** Age should be an integer datatype
** Bio(description about yourself) should be string datatype

* Push to Github

### Sample Input:
does not apply None

### Sample Response Format
{"slackUsername": String,
"backend": Boolean,
"age": Integer,
"bio": String}



# Backend Stage 2 Task

## Task Description
* Using the same server setup from stage one
* Create an (POST) api endoint that takes the following sample json:
'''
{ “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
'''
** Operation can either be addition, subtraction or mutiplication
** x can be a number and Integer datatype
** y can be a number and Integer datatype
* Based on the operation sent, perform a simple arithmetic operation on x and y
* Return a response with the result of the operation and your slack username
'''
{ “slackUsername”: String,
"operation_type" : Enum. value,
“result”: Integer }
'''

### Push to GitHub

## Sample Input
'''
{ “operation_type”: Enum <addition | subtraction | multiplication> ,
“x”: Integer,
“y”: Integer }
'''

## Sample Response Format
'''
{ “slackUsername”: String,
“result”: Integer,
“operation_type”: Enum.value }
'''
