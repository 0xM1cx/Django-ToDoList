from django.shortcuts import render
from django.http import HttpResponse



def index(response):
    return HttpResponse("<h1 style='text-align: center'>Student Dashboard Page</h1>")

def grades(response):
    return HttpResponse("<h1>Student Grades Page</h1>")
