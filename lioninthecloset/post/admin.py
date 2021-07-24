from django.contrib import admin
from .models import *

admin.site.register(Item)
admin.site.register(User)
admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Combination)