from django import forms
from posts.models import Post, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control rounded-3",
                "placeholder": "Введите название категории..."
            })
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "category", "image")
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control rounded-3",
                "placeholder": "Введите заголовок поста"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control rounded-3",
                "rows": 4,
                "placeholder": "Напишите текст поста..."
            }),
            "category": forms.Select(attrs={
                "class": "form-select rounded-3"
            }),
            "image": forms.FileInput(attrs={
                "class": "position-absolute top-0 start-0 w-100 h-100 opacity-0",
                "id": "image",
                "accept": "image/*"
            })
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title == "banned word":
            raise forms.ValidationError("Это название запрещено!")
        return title