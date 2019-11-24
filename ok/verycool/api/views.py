from django.shortcuts import render
from django.http import JsonResponse
import pymongo
from django.views.decorators.csrf import csrf_exempt
import json
from pprint import pprint

client = pymongo.MongoClient("mongodb+srv://admin:iZhYxwEzN42AXEv@cluster0-xg3ry.gcp.mongodb.net/test?retryWrites=true&w=majority")

db = client["durhack"]

def test(r):
    return JsonResponse({
        "hello": "World"
    })


@csrf_exempt
def create_user(r):
    j = json.loads(r.body)
    print("Got json")
    pprint(j)
    firebaseId = j["firebase"]

    search = {"firebaseToken": firebaseId }

    docs = db["users"].find(search).limit(1)

    print("Found users")
    print(docs)

    if docs.count() == 0:
        print("No user found, creating")
        d = {
            "firebaseToken": firebaseId,
            "applications": []
        }
        db["users"].insert({
            "applications": []
        })
        return JsonResponse(d)
    else:
        print("Got user")
        doc = docs.next()
        print(doc)
        return JsonResponse({
            "applications": doc["applications"]
        })

@csrf_exempt
def add_application(r):
    j = json.loads(r.body)
    print("Got json")
    pprint(j)
    firebaseId = j["firebase"]

    newvalues = { "$push": { "applications": {
        "name": j["name"],
        "address": j["address"],
        "minCreditAmount": j["minCreditAmount"],
        "minPaybackTime": j["minPaybackTime"],
        "dob": j["dob"],
        "howWillUse": j["howWillUse"],
        "reason": j["reason"],
        "howWillRepay": j["howWillRepay"],
    } } }

    db.users.update_one({"firebaseToken": firebaseId}, newvalues)

    user = db.users.find({"firebaseToken": firebaseId}).limit(1).next()

    return JsonResponse({
        "applications": user["applications"]
    })
    
