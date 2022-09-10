from sys import settrace
from tkinter import E
from django.shortcuts import render

def home(request):
    if request.method == "POST":
        #import pdb; pdb.set_trace()
        print(request.POST)
    return render(request, "index.html")