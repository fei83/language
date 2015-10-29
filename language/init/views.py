import random

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from wiki.models import Category, Page

 
def init(request):
    if User.objects.filter(username='admin'):
        context = {'init':False}
    else:
        context = {'init':True}

        # Delete everything
        User.objects.all().delete()
        Category.objects.all().delete()
        Page.objects.all().delete()

        # Create the 'admin' account
        admin = User()
        admin.username = 'admin'
        admin.first_name = '管理員'
        admin.set_password('admin')
        admin.email = 'admin@gmail.com'
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()

        # Python 
        pythonCategory = popCategory('Python')
        popPage(category=pythonCategory,
                title='官方Python教材',
                url='http://docs.python.org/2/tutorial/')
        popPage(category=pythonCategory,
                title='如何像電腦科學家一樣思考',
                url='http://www.greenteapress.com/thinkpython/')
        popPage(category=pythonCategory,
                title='10分鐘內學好Python',
                url='http://www.korokithakis.net/tutorials/python/')

        # Other languages
        languageCategory = popCategory('Other languages')
        popPage(category=languageCategory,
                title='C language',
                url='http://www.tutorialspoint.com/cprogramming/c_overview.htm')
        popPage(category=languageCategory,
                title='Java',
                url='https://www.java.com/zh_TW/')
    
        # Django
        djangoCategory = popCategory('Django')
        popPage(category=djangoCategory,
                title='官方Django教材',
                url='https://docs.djangoproject.com/en/1.5/intro/tutorial01/')
        popPage(category=djangoCategory,
                title='Django真讚',
                url='http://www.djangorocks.com/')
        popPage(category=djangoCategory,
                title='如何和Django跳探戈',
                url='http://www.tangowithdjango.com/')
    
        # Other frameworks
        frameCategory = popCategory('其他框架')
        popPage(category=frameCategory,
                title='Bottle框架',
                url='http://bottlepy.org/docs/dev/')
        popPage(category=frameCategory,
                title='Flask框架',
                url='http://flask.pocoo.org')

    # endif

    # Retrieve everything
    users = User.objects.all()
    categories = Category.objects.all().order_by('-likes')
    catsAndPages = []
    for category in categories:
        pages = Page.objects.filter(category=category).order_by('-views')
        tmpList = [category]
        for page in pages:
            tmpList.append(page)
        catsAndPages.append(tmpList)
    context.update({'users':users, 'catsAndPages':catsAndPages})
    return render(request, 'init/init.html', context)


def popCategory(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = random.randint(0,20)
    category.likes = random.randint(0,20)
    category.save()
    return category


def popPage(category, title, url, views=0):
    Page.objects.get_or_create(category=category, title=title,
                               url=url, views=views)[0]

