from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # in add thumbanil
    # add in author
def ___str___(self):
    return self.titles

    def snippet(self):
        return self.body[:50] +'...'
