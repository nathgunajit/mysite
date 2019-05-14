from django.shortcuts import render, redirect, get_object_or_404
from category.models import Category
from django.http import Http404


def listing(request):
    category = Category.objects.filter(status=1)
    context = {
        'category': category,
    }
    return render(request, 'category/listing.html', context)


def details(request,id):
    #category = get_object_or_404(Category, pk=id)
    #category = Category.objects.get(pk=id)
    #category = Category.objects.get(id=id)
    #category=Category.objects.filter(name="Wedding Planning").first()
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
      raise Http404("Data Not Found")
    except ValueError:
        context = {
            'category': category,
            }
    return render(request, 'category/details.html', context)