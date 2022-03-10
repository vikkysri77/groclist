from django.shortcuts import render

from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.


# def index(request):
#     type_list = Type.objects.all().order_by('items__price')
#     response = HttpResponse()
#     heading1 = '<p>' + 'Different Types: ' + '</p>'
#     response.write(heading1)
#     for item_types in type_list:
#         para = '<p>' + str(item_types.id) + ': ' + str(item_types) + '</p>'
#         response.write(para)
#     return response

def index(request):
    item_list = Item.objects.all().order_by('-price')[:7]
    response = HttpResponse()
    heading1 = '<p>' + 'Item list in descending order: ' + '</p>'
    response.write(heading1)
    for item_types in item_list:
        para = '<p>' + str(item_types) + '</p>'
        response.write(para)
    return response


def about(request):
    response = HttpResponse()
    sampletext = "This is an Online Grocery Store"
    response.write(sampletext)
    return response


def detail(request, type_no):

    item_queryset = get_list_or_404(Item.objects,  type_id__exact=type_no)

    # print(item_queryset)
    # response = HttpResponse()
    # item_queryset = Item.objects.all().filter( type=type_no)
    #
    # for item in item_queryset:
    #     para = '<p>' + str(item.id) + ': ' + str(item.name) + '</p>'
    #     response.write(para)
    #
    # return response

    return HttpResponse(item_queryset)

