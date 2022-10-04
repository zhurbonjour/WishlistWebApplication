from django.db import models


def get_wish_image_filepath(self, *args, **kwargs):
    return f'wish_images/{self.pk}/{"wish_image.png"}'


def get_default_wish_image():
    return f'wish_images/default/default_wish_sticker.png'


class Wish(models.Model):
    """Конкретная заметка-пожелание юзера"""
    # id
    wish = models.CharField(max_length=100, name='wish')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=get_wish_image_filepath,
                              null=True,
                              blank=True,
                              default=get_default_wish_image)
    user = models.ForeignKey(to='account.Account',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.wish
