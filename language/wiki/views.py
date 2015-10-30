from django.shortcuts import render
from wiki.models import Category, Page
from wiki.forms import CategoryForm


def wiki(request):  
    #categories = Category.objects.order_by('-likes')        
    context = {}
    return render(request, 'wiki/wiki.html', context)


def about(request):
    return render(request, 'wiki/about.html')


def category(request, categoryNameSlug):
    context = {}
    try:
        category = Category.objects.get(slug=categoryNameSlug)
        context['category'] = category
        pages = Page.objects.filter(category=category)
        context['pages'] = pages
    except Category.DoesNotExist:
        context['categoryName'] = categoryNameSlug.replace('-', ' ')
    return render(request, 'wiki/category.html', context)


def addCategory(request):
    template = 'wiki/addCategory.html'
    if request.method=='GET':
        return render(request, template, {'form':CategoryForm()})
    # request.method=='POST'
    form = CategoryForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save(commit=True)
    return wiki(request)    # Call function wiki()
