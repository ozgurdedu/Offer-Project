from django import forms
from .models import Question, RFQ
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User

class CreateQuestionForm(forms.ModelForm):

    rfq = forms.ModelChoiceField(
        queryset=RFQ.objects.all(),
        widget=forms.Select(
            attrs={'class':'form-control'}
        )
        
    )    
    question = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Question'}),
        )
    answer_1 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Answer 1'}),
        )

    answer_2 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Answer 2'}),
        )
    answer_3 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Answer 3'}),
        )    
    answer_4 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Answer 4'}),
        )
    related_person = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required = True,
        widget= forms.SelectMultiple(
            attrs={'class':'form-control'}
        )
    )
        
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['question_created_by']