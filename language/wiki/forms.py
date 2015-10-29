from django import forms
from wiki.models import Category, Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='類別名稱', help_text='請輸入類別名稱')

    class Meta:
        model = Category
        fields = ('name', )


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='頁面標題', help_text='請輸入頁面標題')
    url = forms.URLField(max_length=200, label='頁面網址', help_text='請輸入頁面網址')

    class Meta:
        model = Page
        exclude = ('category', )
