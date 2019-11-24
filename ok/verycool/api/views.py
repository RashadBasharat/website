from django.shortcuts import render
from django.http import JsonResponse

def test(r):
    return JsonResponse({
        "hello": "World"
    })
