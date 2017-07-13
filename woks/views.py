import markdown2

from django.shortcuts import render

from django.http import HttpResponse

from .models import Chapter


def index(request):
    chapter = Chapter.objects.filter().first()
    html = markdown2.markdown(chapter.body)

    return HttpResponse(html)
