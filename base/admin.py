from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Prize)
admin.site.register(Payment)
admin.site.register(Raffle)
