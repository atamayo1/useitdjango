from django.forms import ModelForm
from .models import Post, Comment

class  PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'fix_id']

class  CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'description', 'fix_id']

"""class LikeForm(ModelForm)
    class Meta:
        model = Like
        fields = ['like', 'fix_id']"""


