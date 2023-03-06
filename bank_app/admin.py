from django.contrib import admin
from . models import Branches,District,Account,Details
# Register your models here.
admin.site.register(Branches)
admin.site.register(District)
admin.site.register(Account)
admin.site.register(Details)