from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    students = [
        {
            'id' : 6,
            'name' : 'Sushil',
            'stream' : 'Science'
        }
    ]

    # return HttpResponse('<h2>Hey hie Sushil keep it up bro the job is very few days away</h2>')
    return HttpResponse(students)