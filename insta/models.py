from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile/", blank=True)
    def __str__(self):
        return self.user.username
    @classmethod
    def get_all(cls):
        profiles = Profile.objects.all()
        return profiles
    
class Image(models.Model):
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.caption
    @classmethod
    def get_all(cls):
        imgs = Image.objects.all()
        return imgs

    class Meta:
        ordering = ['-post_date']

class Comment(models.Model):
    '''
    Class that defines a Comment on a Post
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    post = models.ForeignKey(Image,on_delete=models.CASCADE)

    comment_content = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_post_comments(cls,post_id):
        '''
        Function that gets all the comments belonging to a single post

        Args:
            post_id : specific post

        Returns:
            comments : List of Comment objects for the specified post
        '''
        post_comments = Comment.objects.filter(post=post_id)

        return post_comments