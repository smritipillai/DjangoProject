from django.db import models

class Category(models.Model):
    name =  models.CharField(max_length=50)

    class Meta:
        verbose_name= "Category"
        verbose_name_plural= "Categories"
    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length=50)

class post(models.Model):
    Title = models.CharField(max_length=100)
    Date = models.DateField()
    Author =  models.CharField(verbose_name="author name",
                                help_text="Enter Authorname",
                                max_length=30,
                                blank=True,
                                null=True)
    Content =  models.TextField(blank=True, null=True)
    Category = models.ForeignKey(Category,blank=True, null= True, on_delete=models.CASCADE )
    Tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.Title
