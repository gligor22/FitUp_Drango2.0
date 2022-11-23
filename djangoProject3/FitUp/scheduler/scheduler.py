# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore
# from django.utils import timezone
# from django_apscheduler.models import DjangoJobExecution
# import sys
# from FitUp.models import Client, Reservation, Training, Coach, Payment
#
#
# def daily():
#     clients = Client.objects.filter()
#     for c in clients:
#         c.remaining = c.remaining-1
#         c.save()
#
#
# def weekly():
#     coaches = Coach.objects.filter()
#     for c in coaches:
#         c.num_week = 0
#         c.save()
#
#
# def monthly():
#     coaches = Coach.objects.filter()
#     for c in coaches:
#         c.num_month = 0
#         c.save()
#
#
# def yearly():
#     coaches = Coach.objects.filter()
#     for c in coaches:
#         c.num_year = 0
#         c.save()
#
#
# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_jobstore(DjangoJobStore(), "default")
#     scheduler.add_job(daily, 'interval', days=1, name='daily', jobstore='default')
#     scheduler.add_job(weekly, 'interval', days=7, name='weekly', jobstore='default')
#     scheduler.add_job(monthly, 'interval', months=1, name='monthly', jobstore='default')
#     scheduler.add_job(yearly, 'interval', years=1, name='yearly', jobstore='default')
#     scheduler.start()
#     print("Scheduler started...", file=sys.stdout)