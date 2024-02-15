from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render

from coursesapp.models import Content, Module


def index(request):
    module = Module.objects.get(pk=8)
    obj = ContentType.objects.get_for_model(module)
    # obj = ContentType.objects.get(app_label='coursesapp', model='module')
    lst = Content.objects.filter(content_type__pk=obj.pk, object_id=module.pk)
    print(lst)
    return HttpResponse("Hello")
