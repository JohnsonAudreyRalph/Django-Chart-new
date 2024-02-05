from datetime import datetime, timedelta
from .models import HourlyData, DateTimeRecord
import random

def my_periodic_task():

    number = random.randint(0, 100)


    # Đặt code của công việc cần thực hiện ở đây
    current_time = datetime.now()
    dt_record, created = DateTimeRecord.objects.get_or_create(date_time=current_time.date())
    hourly_data, created = HourlyData.objects.get_or_create(datetime_record=dt_record)

    current_hour = current_time.hour
    field_name = f"hour_{current_hour}_data"
    setattr(hourly_data, field_name, number)  # Đặt giá trị mới tại đây
    hourly_data.save()
    print("Đã lưu")


# mkdir -p yourapp/management/commands
