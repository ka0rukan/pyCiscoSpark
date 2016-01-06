import requests
import json

#Helpers
def _url(path):
    return 'https://api.ciscospark.com/v1' + path

def findroomidbyname (at,roomname):
    room_dict = pyCiscoSpark.get_rooms(at)    
    for room in room_dict['items']:
        print room['title']
        if (room['title']==roomname):roomid = room['id']    
    return roomid

#GET Requests
def get_people(at,email="",displayname="",max=10):
    headers = {'Authorization':at}
    payload = {"max":max}
    if (email != ""):
        payload["email"]=email
    if (displayname != ""):
        payload["displayName"]=displayname
    print payload
    resp = requests.get(_url('/people'),params=payload, headers=headers)
    return json.loads(resp.text)

def get_persondetails(at,personId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/people/{:s}/'.format(personId)),headers=headers)
    return json.loads(resp.text)

def get_me(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/people/me'),headers=headers)
    return json.loads(resp.text)

def get_rooms(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/rooms'),headers=headers)
    return json.loads(resp.text)

def get_room(at,roomId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/memberships'),headers=headers)
    return json.loads(resp.text)

def get_memberships(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/memberships'),headers=headers)
    return json.loads(resp.text)

def get_membership(at,membershipId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/memberships/{:s}/'.format(membershipId)),headers=headers)
    return json.loads(resp.text)

def get_messages(at,roomId):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {'roomId':roomId}
    resp = requests.get(_url('/messages'),params=payload, headers=headers)
    return json.loads(resp.text)

def get_message(at,messageId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/messages/{:s}'.format(messageId)),headers=headers)
    return json.loads(resp.text)

def get_webhooks(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/webhooks'),headers=headers)
    return json.loads(resp.text)

def get_webhook(at,webhookId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/webhooks/{:s}'.format(webhookId)),headers=headers)
    return json.loads(resp.text)

#POST Requests
def post_createroom(at,title):
    headers = {'Authorization':at, "content-type":"application/x-www-form-urlencoded"}
    payload = {"title":title}
    resp = requests.post(url=_url('/rooms'),params=payload, headers=headers)
    return json.loads(resp.text)

def post_message(at,roomId,text):
    headers = {'Authorization':at, "content-type":"application/x-www-form-urlencoded"}
    payload = {'roomId':roomId, "text":text}
    resp = requests.post(url=_url('/messages'),params=payload, headers=headers)
    return json.loads(resp.text)

def post_file(at,roomId,url):
    headers = {'Authorization':at, "content-type":"application/x-www-form-urlencoded"}
    payload = {'roomId':roomId, "file":url}
    resp = requests.post(url=_url('/messages'),params=payload, headers=headers)
    return json.loads(resp.text)

def post_membership(at,roomId,personEmail,isModerator=True):
    headers = {'Authorization':at, "content-type":"application/x-www-form-urlencoded"}
    payload = {'roomId':roomId, "personEmail":personEmail, "isModerator":isModerator}
    resp = requests.post(url=_url('/memberships'),params=payload, headers=headers)
    return json.loads(resp.text)

def post_webhook(at,name,targetUrl,resource,event,filter):
    headers = {'Authorization':at, "content-type":"application/x-www-form-urlencoded"}
    payload = {'name':name, "targetUrl":targetUrl, "resource":resource, "event":event, "filter":filter}
    resp = requests.post(url=_url('/webhooks'),params=payload, headers=headers)
    return json.loads(resp.text)

#PUTS
def put_room(at,roomId,title):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {"title":title}
    resp = requests.put(url=_url('/rooms/{:s}'.format(roomId)),json=payload, headers=headers)
    return json.loads(resp.text)

def put_membership(at,membershipId,isModerator):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {"isModerator":isModerator}
    resp = requests.put(url=_url('/memberships/{:s}'.format(membershipId)),json=payload, headers=headers)
    return json.loads(resp.text)

def put_webhook(at,webhookId,name,targetUrl):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {"name":name, "targetUrl":targetUrl}
    resp = requests.put(url=_url('/webhooks/{:s}'.format(webhookId)),json=payload, headers=headers)
    return json.loads(resp.text)

#DELETES

def del_room(at,roomId):
    headers = {'Authorization':at, "content-type":"application/json"}
    resp = requests.delete(url=_url('/rooms/{:s}'.format(roomId)), headers=headers)
    return json.loads(resp.text)

def del_membership(at,membershipId):
    headers = {'Authorization':at, "content-type":"application/json"}
    resp = requests.delete(url=_url('/memberships/{:s}'.format(membershipId)), headers=headers)
    return json.loads(resp.text)

def del_message(at,messageId):
    headers = {'Authorization':at, "content-type":"application/json"}
    resp = requests.delete(url=_url('/messages/{:s}'.format(messageId)), headers=headers)
    return json.loads(resp.text)

def del_webhook(at,webhookId):
    headers = {'Authorization':at, "content-type":"application/json"}
    resp = requests.delete(url=_url('/webhooks/{:s}'.format(webhookId)), headers=headers)
    return json.loads(resp.text)



