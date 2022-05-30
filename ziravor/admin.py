from django.contrib import admin
from .models import XodimModels, YangiliklarModel, FloraTypeModel, FloraModel


@admin.register(XodimModels)
class XodimAdmin(admin.ModelAdmin):
    field = ('__all__')


@admin.register(YangiliklarModel)
class YangiliklarAdmin(admin.ModelAdmin):
    field = ('sub_title', 'title', 'data', 'image', 'text')

@admin.register(FloraTypeModel)
class FloraTypeAdmin(admin.ModelAdmin):
    field = ('__all__')


@admin.register(FloraModel)
class FloraAdmin(admin.ModelAdmin):
    field = ('__all__')
