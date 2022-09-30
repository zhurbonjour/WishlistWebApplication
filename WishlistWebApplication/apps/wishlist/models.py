from django.db import models


class Wish(models.Model):
    """Конкретная заметка-пожелание юзера"""
    # id
    wish = models.CharField(max_length=100, name='wish')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/images/%Y/%m/%d/', blank=True, null=True)
    user = models.ForeignKey(to='account.Account',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.wish
