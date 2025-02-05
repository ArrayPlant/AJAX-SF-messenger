from django import forms
from .models import Message, Profile


class MessageForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 3, 'cols': 80}), required=True)

    class Meta:
        model = Message
        fields = ['text',]


class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(label="ИМЯ", max_length=30)
    portrait = forms.ImageField(label="ФОТО ПРОФИЛЯ", required=False)

    class Meta:
        model = Profile
        fields = ['nickname', 'portrait']

        widgets = {
            'portrait': forms.FileInput(attrs={'accept': 'image/*'}),
        }
