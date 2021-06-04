from apps.hotel.models import Hotel
from apps.notification.serializers import NotificationSerializer
from config.celery import app
from core.utils import create_model


@app.task
def notification(rent_id, type, hotel_id):
    notificationData = {'rent': rent_id, 'type': type, 'hotel': hotel_id}
    create_model(notificationData, NotificationSerializer)
    hotel = Hotel.objects.filter(id=hotel_id).prefetch_related('staff',).first()
    staffs = hotel.staff.all()
    for staff in staffs:
        print("Gửi thông báo cho nhân viên khách sạn. {id}".format(id=staff.id))