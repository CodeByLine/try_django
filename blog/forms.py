from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'author',
        ]

# class RawBlogForm(forms.Form):
#     title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
#     description = forms.CharField(required=False, widget=forms.Textarea(  #widget override default
#         attrs={
#             "class": "new-class-name two",
#             "id" : "my-id-for",
#             "cols": 120
#             }
#         )
#     )
#     author       = forms.CharField()

#     class Meta:
#         model = Blog
#         fields = [
#             'title',
#             'description',
#             'author',
#         ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "cat" in title:
    #         raise forms.ValidationError("There must be 'cat' in title")
    #     if not "dog" in title:
    #         raise forms.ValidationError("There must be 'dog' in title")
    #     return title