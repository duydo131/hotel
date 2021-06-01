from celery import Celery

from apps.hotel.models import Hotel
from apps.notification.serializers import NotificationSerializer
from apps.users.models import User
from config.settings.base import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from core.utils import create_model

app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.task
def notification(rent_id, type, hotel_id):
    notificationData = {'rent': rent_id, 'type': type, 'hotel': hotel_id}
    serilizer = create_model(notificationData, NotificationSerializer)

    # 1 user chỉ đặt 1 khách sạn
    hotel = Hotel.objects.get(hotel_id)
    staffs = hotel.staff.all()
    for staff in staffs:
        print("Gửi thông báo cho nhân viên khách sạn. {id}".format(id=staff.id))
    #return serilizer
