from django.shortcuts import render

from django.http import HttpResponse

from .forms import OrderItemForm, InterestForm
from .models import Type, Item
from django.shortcuts import get_object_or_404, get_list_or_404, render


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
    type_list = Type.objects.all().order_by('id')[:7]

    return render(request, 'myapp1/index.html', {'type_list': type_list})

    # This piece of code was done for previous lab
    # item_list = Item.objects.all().order_by('-price')[:7]
    # response = HttpResponse()
    # heading1 = '<p>' + 'Item list in descending order: ' + '</p>'
    # response.write(heading1)
    # for item_types in item_list:
    #     para = '<p>' + str(item_types) + '</p>'
    #     response.write(para)
    # return response


def about(request):
    sampletext = "This is an Online Grocery Store"
    return render(request, 'myapp1/about.html', {'sample_text': sampletext})
    # response = HttpResponse()
    # sampletext = "This is an Online Grocery Store"
    # response.write(sampletext)
    # return response


def detail(request, type_no):
    item_list = get_list_or_404(Item.objects, type_id__exact=type_no)

    type_of_item = get_object_or_404(Type, id=type_no)
    return render(request, 'myapp1/detail.html', {'type_of_items': type_of_item, 'item_list': item_list})

    # print(item_queryset)
    # response = HttpResponse()
    # item_queryset = Item.objects.all().filter(type_id__exact=type_no)
    #
    # for item in item_queryset:
    #     para = '<p>' + str(item.id) + ': ' + str(item.name) + '</p>'
    #     response.write(para)
    #
    # return response

    # return HttpResponse(item_queryset)


# def placeorder(request):
#     text = 'You can place your order here'
#     response = HttpResponse()
#     response.write(text)
#
#     return response

def placeorder(request):
  msg = ''
  itemlist = Item.objects.all()
  if request.method== 'POST':
      form = OrderItemForm(request.POST)
      if form.is_valid():
          order = form.save(commit=False)
          if order.itemsCount <= order.item.stock:
              order.status_options = 1
              order.item.stock = order.item.stock - order.itemsCount
              orderitem=Item.objects.get(name=order.item)
              orderitem.stock = orderitem.stock - order.itemsCount
              orderitem.save()
              order.save()
              msg = 'Your order has been placed successfully.'
          else:
              msg = 'We do not have sufficient stock to fill your order.'
              return render(request, 'myapp1/order_response.html', {'msg': msg})
  else:
      form = OrderItemForm()
  return render(request, 'myapp1/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist})

def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})

def itemdetail(request, item_id):
    msg = ''
    try:
        itemDetails = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        msg = 'Requested Item not found.'
        return render(request, 'myapp1/order_response.html', {'msg': msg})
    item_name = itemDetails.name
    item_price = itemDetails.price
    item_interested = itemDetails.interested
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interestselected = form.cleaned_data.get("interested")
            if interestselected == '1':
                itemDetails.interested = itemDetails.interested + 1
                itemDetails.save()
                item_interested = itemDetails.interested
            return render(request, 'myapp1/order_response.html',
                          {'msg': msg, 'item_Name': item_name, 'item_Price': item_price,
                           'item_Interested': item_interested})
    else:
        form = InterestForm()
        return render(request, 'myapp1/itemdetail.html',
                      {'form': form, 'msg': msg, 'item_name': item_name, 'item_price': item_price,
                       'item_interested': item_interested})