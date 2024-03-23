from django import forms
from .models import Quote, Tag


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']