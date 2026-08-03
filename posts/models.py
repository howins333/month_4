from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

# #CREATE
# Post.objects.create()
# post = Post(tittle='title#1', description='description_to-blog')
# post.save()

# #READ
# post = Post.object.filter(title='title').first()

# #UPDATE
# post.tittle = "Howins"
# post.save()

# #DELETE
# post.delete()
