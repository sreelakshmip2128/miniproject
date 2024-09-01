# from django.contrib import admin
# admin.site.register(Registers)

# # Register your models here.
# from .models import Registers
# admin.site.register(Registers) #table registe

from django.contrib import admin
from .models import Registers , Organization # Ensure that this line is correct

admin.site.register(Registers)
admin.site.register(Organization)
