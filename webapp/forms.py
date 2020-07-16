from django import forms
from webapp.models import Topic
from django.core import validators


class CreateTopicForm(forms.ModelForm):

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
                                 validators.MaxLengthValidator(0)])

    class Meta:
        model = Topic
        fields = ['name', 'botcatcher']
        labels = {
            'name': 'Give your topic a name',
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].isupper() != True:
            raise forms.ValidationError(
                "Topic names must start with an uppercased character")
        return name
