from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Author(models.Model):
    rating_author = models.IntegerField(default=0)

    user_author = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating1(self, value):
        t = 0
        for i in range(len(Post.objects.filter(author_id=value))):
            t += list(Post.objects.filter(author_id=value).values())[i]['rating_post']
        return t * 3

    def update_rating2(self, value):
        user = Author.objects.get(id=value).user_author_id

        t = 0
        for i in range(len(Comment.objects.filter(user_id=user))):
            t += list(Comment.objects.filter(user_id=user).values())[i]['rating_comment']
        return t

    def update_rating3(self, value):
        t = 0
        for i in range(1, len(Post.objects.filter(author_id=value)) + 1):
            for j in range(len(Comment.objects.filter(post_id=list(Post.objects.filter(author_id=value).values())[i-1]["id"]))):
                t += list(Comment.objects.filter(post_id=list(Post.objects.filter(author_id=value).values())[i-1]["id"]).values())[j]['rating_comment']
        return t

    def update_rating(self, value):
        self.rating_author = self.update_rating1(value) + self.update_rating2(value) + self.update_rating3(value)
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    change = models.BooleanField(default=False)
    rating_post = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categorys = models.ManyToManyField(Category, through="PostCategory")

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        print(self.content[:124], "...", sep="")


class Comment(models.Model):
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_comment = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

