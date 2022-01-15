from django.db import models
from django.utils.translation import gettext_lazy as _

from image_repository.models.user import User


class ImageManager(models.Manager):
    @staticmethod
    def search_image_characteristics(height, width, color):
        pass

    @staticmethod
    def search_image_by_text(name):
        pass

    @staticmethod
    def search_images_with_image(image):
        pass

    @staticmethod
    def add_image(user_id, image):
        pass

    @staticmethod
    def add_images(user_id, images):
        pass

    def calculate_height_width(self, image) -> (int, int):
        pass

    def calculate_color(self, image):
        pass


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    height = models.PositiveIntegerField(blank=False)
    width = models.PositiveIntegerField(blank=False)

    class Color(models.TextChoices):
        RED = 'RED', _('Red')
        BLUE = 'BLU', _('Blue')
        GREEN = 'GRN', _('Green')
        WHITE = 'WHT', _('White')
        BLACK = 'BLK', _('Black')

    color = models.CharField(max_length=3, choices=Color.choices, blank=False)
    image = models.ImageField(upload_to='images', height_field='height', width_field='width', blank=False,
                              help_text='Please add a image')

    class Permission(models.IntegerChoices):
        PRIVATE = 0, _('Private')
        PUBLIC = 1, _('Public')

    permission = models.SmallIntegerField(choices=Permission.choices, blank=False, default=Permission.PRIVATE)
    last_updated = models.DateTimeField(auto_now_add=True, blank=False)

    objects = ImageManager()

    def __str__(self):
        return self.name
