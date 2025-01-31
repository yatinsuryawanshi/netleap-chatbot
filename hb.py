

import json

def validate(slots):

if not slots['city']:

print("Inside Empty city") 
return {
'isValid': False, 
'violatedSlot': 'city' 
}



if not slots['checkindate']:

} 
return {
 'isValid': False, 
'violatedSlot: 'checkindate',
}

if not slots['nights']:

return { 
'isValid': False,
 'violatedSlot': 'nights'
}

if not slots['roomtype']:

return {

'isValid': False, 
'violatedSlot': 'roomtype'
}

return (isValid': True)
def lambda_handler(event, context):



slots event['sessionState']['intent']['slots']

intent event['sessionState']['intent']['name']


print(event['invocationSource'])

print(slots)


print(intent)


validation_result = validate(slots)


if event['invocationSource'] == 'DialogCodeHook':

if not validation_result['isValid']:

response {

"sessionState": {
"dialogAction": { 
 "slotToElicit": validation_result['violatedSlot'],
"type": "ElicitSlot"
},

"intent": {
'name':intent,
'slots':slots
}
}
}


else :
 response = {
"sessionState" :{
"dialogAction" : {
"type" : "Delegate"

},
 "intent": {
'name' :intent,
'slots':slots
}
}
}
return response