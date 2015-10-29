from django.shortcuts import render
from wiki.models import Category, Page


def wiki(request):  
    categories = Category.objects.order_by('-likes')        
    context = {'categories':categories}
    return render(request, 'wiki/wiki.html', context)


def about(request):
    return render(request, 'wiki/about.html')


def category(request, categoryNameSlug):
    print('here')
    context = {}
    try:
        category = Category.objects.get(slug=categoryNameSlug)
        context['category'] = category
        pages = Page.objects.filter(category=category)
        context['pages'] = pages
    except Category.DoesNotExist:
        context['categoryName'] = categoryNameSlug.replace('-', ' ')
    return render(request, 'wiki/category.html', context)

