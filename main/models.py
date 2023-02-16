from django.db import models

class news(models.Model):
    news_id=models.AutoField(primary_key=True)
    s_title=models.CharField(max_length=50)
    head=models.CharField(max_length=50)
    author=models.CharField(max_length=50,default="")
    content=models.CharField(max_length=500)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='main/images',default="")

    def __str__(self):
        return self.s_title

class blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    b_title=models.CharField(max_length=100)
    author=models.CharField(max_length=50,default="")
    content=models.CharField(max_length=500)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='main/images',default="")

    def __str__(self):
        return self.b_title