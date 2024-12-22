from django import forms
from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)




class WebPageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()



class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=WebPage.objects.all())
    author=forms.CharField(max_length=100)
    date=forms.DateField()



class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class WebPageModelForm(forms.ModelForm):
    class Meta:
        model=WebPage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['url','name']
        #labels={'topic_name':'TPN','name':'Person_name'}
        #widgets={'url':forms.PasswordInput()}
        #widgets={'name':forms.Textarea}
        help_texts={'topic_name':'select option which u like'}




class AccessModelForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
        #fields=['name']
        #exclude=['name','author']