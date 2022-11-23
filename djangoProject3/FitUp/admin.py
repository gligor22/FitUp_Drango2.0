from django.contrib import admin
from .models import Client, Coach, Reservation, Training, Payment
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name",]


class CoachAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "rate",]


class ReservationAdmin(admin.ModelAdmin):
    list_display = ["client", "training", ]


class TrainingAdmin(admin.ModelAdmin):
    list_display = ["type", "duration_min", "Coach"]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["client", "price", "date", "num_trainings_per_week", ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Payment, PaymentAdmin)
