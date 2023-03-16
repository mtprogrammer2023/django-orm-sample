from django.db import models

# blank=True ===> ejbari hast ya na

class Post(models.Model):
   title = models.CharField(max_length=255)
   text = models.TextField(blank=True)
   is_enable = models.BooleanField(default=False)
   publish_date = models.DateField(null=True,blank=True)
   created_time = models.DateTimeField(auto_now_add=True)
   updated_time = models.DateTimeField(auto_now=True)

   def __str__(self):
        return '{} - {}'.format(self.pk,self.title)

class Comment(models.Model):
     post = models.ForeignKey(Post,on_delete=models.CASCADE)
     text = models.TextField()
     created_time = models.DateTimeField(auto_now_add=True)
     updated_time = models.DateTimeField(auto_now=True)
