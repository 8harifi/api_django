from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse("<h3>hello!</h3>\n<h4>this is the home page</h4>")
