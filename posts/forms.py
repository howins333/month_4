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
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите заголовок"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите описание",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title == "banned word":
            raise forms.ValidationError("Это название запрещено!")
        return title