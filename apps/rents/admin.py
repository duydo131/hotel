from django.contrib import admin
from .models.rent import Rent
from .models.feedback import Feedback
from .models.rent_detail import RentDetail

admin.site.register(Rent)
admin.site.register(Feedback)
admin.site.register(RentDetail)
