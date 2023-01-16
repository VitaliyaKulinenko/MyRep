from celery import shared_task

from main.models import Timetable


@shared_task
def add_inf_to_timetable():
    c = Timetable(days_of_the_week='Wednesday', task='1 person')
    c.save()
