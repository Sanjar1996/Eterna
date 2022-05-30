from django.db import models
from django.utils.translation import get_language
from PIL import Image as pilim

from config import settings

class YangiliklarModel(models.Model):
    sub_title_uz = models.CharField(max_length=255)
    sub_title_ru = models.CharField(max_length=255)
    sub_title_en = models.CharField(max_length=255)

    title_uz = models.CharField(max_length=255) 
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()

    data = models.DateTimeField(auto_now=False)
    image = models.ImageField()

    def __str__(self):
        return self.title_uz

    @property
    def sub_title(self):
        return getattr(self, 'sub_title_{}'.format(get_language()))

    @property
    def title(self):
        return getattr(self, 'title_{}'.format(get_language()))

    @property
    def text(self):
        return getattr(self, 'text_{}'.format(get_language()))



class XodimModels(models.Model):
    fullname_uz = models.CharField(max_length=255)
    fullname_ru = models.CharField(max_length=255)
    fullname_en = models.CharField(max_length=255)

    lavozim_uz = models.CharField(max_length=255)
    lavozim_ru = models.CharField(max_length=255)
    lavozim_en = models.CharField(max_length=255)

    qabul_uz = models.CharField(max_length=255)
    qabul_ru = models.CharField(max_length=255)
    qabul_en = models.CharField(max_length=255)

    brith_day = models.DateField(blank=True)
    image = models.ImageField()
    facebook = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    tel_raqam = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.fullname_uz

    @property
    def qabul(self):
        return getattr(self, 'qabul_{}'.format(get_language()))

    @property
    def lavozim(self):
        return getattr(self, 'lavozim_{}'.format(get_language()))

    @property
    def fullname(self):
        return getattr(self, 'fullname_{}'.format(get_language()))

class FloraTypeModel(models.Model):
    type_uz = models.CharField(max_length=45)
    type_ru = models.CharField(max_length=45)
    type_en = models.CharField(max_length=45)

    def __str__(self):
        return self.type_uz

    @property
    def type(self):
        return getattr(self, 'type_{}'.format(get_language()))

class FloraModel(models.Model):
    flora_types = models.ForeignKey(FloraTypeModel, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=45)
    name_ru = models.CharField(max_length=45)
    name_en = models.CharField(max_length=45)

    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    subtitle_uz = models.CharField(max_length=255)
    subtitle_ru = models.CharField(max_length=255)
    subtitle_en = models.CharField(max_length=255)

    info_uz = models.TextField()
    info_ru = models.TextField()
    info_en = models.TextField()
    image = models.ImageField()
    data = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name_uz

    @property
    def name(self):
        return getattr(self, 'name_{}'.format(get_language()))

    @property
    def subtitle(self):
        return getattr(self, 'subtitle_{}'.format(get_language()))