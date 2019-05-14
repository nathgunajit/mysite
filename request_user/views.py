from django.shortcuts import render, redirect, get_object_or_404
from request_user.models import RequestUser
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RequestUserForm
from .forms import RequestUserFormModel

def index(request):
    return render(request, 'request_user/form.html')


def register(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        if request.POST.get('name') and request.POST.get('email'):
            request_user = RequestUser()
            request_user.name = request.POST.get('name')
            request_user.email = request.POST.get('email')
            request_user.mobile_no = request.POST.get('mobile_no')
            request_user.address = request.POST.get('address')
            request_user.description = request.POST.get('description')
            request_user.pin_code = request.POST.get('pin_code')
            request_user.services_need = request.POST.get('services_need')
            request_user.booking_date = request.POST.get('booking_date')
            request_user.services_cat_id = request.POST.get('services_cat_id')
            request_user.services_id = request.POST.get('services_id')
            request_user.veg_non_veg = request.POST.get('veg_non_veg')
            request_user.status = request.POST.get('status')
            request_user.save()
            return render(request, 'request_user/form.html')
    else:
        return render(request, 'request_user/form.html')

def formRegister(request):
     form = RequestUserFormModel(request.POST or None)
     if form.is_valid():
         obj=form.save(commit=False)
         obj.save()
         form = RequestUserFormModel()
     template_name='forms.html'
     context={
             'title': "Registration",
             'form': form
     }
     return render(request, template_name, context)

#without Model Form
#
# def formRegister(request):
#     form = RequestUserForm(request.POST or None)
#     if form.is_valid():
#         #print(form.cleaned_data)
#         #type 1
#         # name=form.cleaned_data['name']
#         #obj=RequestUser.objects.create(name=name)
#         #type 2
#         # obj=RequestUser()
#         # obj.name=name
#
#         #obj = RequestUser.objects.create(** form.cleaned_data) #form all data insert
#
#         form = RequestUserForm()
#     template_name='forms.html'
#     context={
#             'title': "Registration",
#             'form': form
#     }
#     return render(request, template_name, context)



# def formRegister(request):
#     if request.method == 'POST':
#         form = RequestUserForm(request.POST or None)
#         print(form.cleaned_data)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             #obj=RequestUser.objects.create(** form.cleaned_data)
#             # form.save()
#             #obj = RequestUser.objects.create(title=title)
#             obj= RequestUser()
#             obj.name=name
#             obj.save()
#             template_name='forms.html'
#             context={'form':form}
#
#     return render(request, template_name, context)


def listing(request):
    request_user = RequestUser.objects.filter(status=1)
    context = {
        'request_user': request_user,
    }
    return render(request, 'request_user/listing.html', context)


def details(request,id):
    try:
        request_user = RequestUser.objects.get(id=id)
    except RequestUser.DoesNotExist:
      raise Http404("Data Not Found")

    context = {
        'request_user': request_user,
    }
    return render(request, 'request_user/details.html', context)
