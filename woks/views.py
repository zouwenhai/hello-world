import markdown2

from django.shortcuts import render

from django.http import HttpResponse

from .models import Chapter


def index(request):
    chapters = Chapter.objects.filter().order_by('-rank')
    html = ''
    for chapter in chapters:
        html +='<hr />'
        html += markdown2.markdown(chapter.body)
        html +='<hr />'

    return HttpResponse(html)
