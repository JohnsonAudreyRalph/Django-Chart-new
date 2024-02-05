# yourapp/management/commands/run_periodic_task.py
import threading
import time
import schedule
from django.core.management.base import BaseCommand
from Show.utils import my_periodic_task

class Command(BaseCommand):
    help = 'Chạy công việc định kỳ mỗi phút'

    def handle(self, *args, **options):
        # Định nghĩa hàm để chạy công việc định kỳ
        def run_periodic_task():
            while True:
                my_periodic_task()
                time.sleep(6)  # Chờ 1 phút trước khi chạy lại # time.sleep(60 * 60)

        # Tạo một thread mới để chạy công việc định kỳ
        thread = threading.Thread(target=run_periodic_task)
        thread.daemon = True
        thread.start()

        # Sử dụng schedule để đặt lịch công việc mỗi phút
        schedule.every(0.1).minutes.do(my_periodic_task)
        # # Sử dụng schedule để đặt lịch công việc mỗi 60 phút
        # schedule.every(60).minutes.do(my_periodic_task)

        # In ra thông báo để xác nhận rằng công việc đã bắt đầu
        self.stdout.write(self.style.SUCCESS('Công việc đã bắt đầu chạy mỗi phút.'))

        # Lặp vô hạn để giữ thread chính sống
        while True:
            time.sleep(1)






# python manage.py run_periodic_task