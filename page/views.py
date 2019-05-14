from django.shortcuts import render, redirect
from banner.models import Banner
from page.models import Page
from category.models import Category,SubCategory
from countries.models import Countries, Cities, Location
from venue.models import Venue
from testimonial.models import Testimonial
from blog.models import Blog
from wedding_images.models import WeddingImages
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
# Create your views here.


def home(request):
    try:
        banners = Banner.objects.get(id=1)
    except Banner.DoesNotExist:
    #except ObjectDoesNotExist:
        banners = None
    # block_home = Page.objects.all().filter(pk__in=[1, 2, 3], status=1, display_home=1).order_by('-id') #order by desc
    block_home = Page.objects.all().filter(pk__in=[1, 2, 3], status=1).order_by('id')
    subcategory = SubCategory.objects.filter(status=1).order_by("name")
    location = Location.objects.filter(status=1).order_by("name")
    header = Page.objects.get(id=5)
    # header = Page.objects.get(name='Home Header')
    venue = Venue.objects.filter(status=1, display_home=1, is_latest=1).order_by("title")
    subcategory_home = SubCategory.objects.filter(status=1, display_home=1).order_by("name")
    # sub_count = Venue.objects.values('subcategory').filter(status=1).order_by('subcategory').annotate(count=Count('subcategory'))
    #sub_count = Venue.objects.raw('SELECT COUNT(id) as count_total, subcategory_id, image FROM wp_venue WHERE status=1 GROUP BY subcategory_id')
    # status = 1
    # sub_count = Venue.objects.raw('SELECT COUNT(id) as count_total, id, '
    #                               'subcategory_id, image FROM wp_venue WHERE status = %s GROUP BY subcategory_id', [status])

    sub_count= Venue.objects.raw('SELECT V.id, COUNT(V.id) as count_total,V.subcategory_id,V.image, S.image '
                                      'FROM wp_venue AS V JOIN wp_subcategory AS S ON V.subcategory_id=S.id WHERE '
                                      'V.status=1 GROUP BY V.subcategory_id ORDER BY V.id DESC LIMIT 5')

    #sub_count_new = Venue.objects.select_related('subcategory').filter(status=1).order_by('subcategory').annotate(count=Count('subcategory'))
    #Book.objects.select_related('author__hometown').get(id=4)

    wedding_pics = WeddingImages.objects.all().filter(status=1, display_home=1).order_by('-id')[0:3]
    home_it_works = Page.objects.all().filter(pk__in=[6, 7, 8], status=1).order_by('id')
    testimonials = Testimonial.objects.all().filter(status=1, display_home=1).order_by('-id')[0:3]
    blogs = Blog.objects.all().filter(status=1, display_home=1).order_by('-id')[0:4]
    pages = Page.objects.all().filter(status=1, display_home=1).order_by('id')

    context = {
        #'sub_count_new': sub_count_new,
        'sub_count': sub_count,
        'wedding_pics': wedding_pics,
        'pages': pages,
        'blogs': blogs,
        'testimonials': testimonials,
        'home_it_works': home_it_works,
        'subcategory_home': subcategory_home,
        'venue': venue,
        'banners': banners,
        'block_home': block_home,
        'header': header,
        'location': location,
        'subcategory': subcategory
    }
    return render(request, 'page/home.html', context)


def home_search(request):
    template = 'page/search.html'
    if request.method == 'POST':
        sub_cat = request.POST['subcategory']
        loc = request.POST['location']
        if sub_cat and loc:
            match = Venue.objects.filter(Q(subcategory=sub_cat), Q(loc_id=loc)).order_by("title")
            #  match = Venue.objects.filter(Q(name__icontains=variable) | Q(title__icontains=variable) | Q(loc__icontains=variable)).order_by("title")
            # i means means not sensitive
            #pages=pagination(request, match, num=1)
            context = {
                # 'iteams': pages[0],
                # 'page_range': pages[1]
                'match': match
            }
            if match:
                return render(request, template, context)
            else:
                messages.error(request, 'No Result Found')
                return redirect('/search/')
        else:
            return redirect('/search/')
    return render(request, template)

