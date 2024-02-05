from django.shortcuts import render
from .models import HourlyData, DateTimeRecord
from django.http import JsonResponse

def index(request):
    all_data = HourlyData.objects.values()
    all_date = DateTimeRecord.objects.values()

    # Tạo một từ điển để ánh xạ id với date_time
    date_mapping = {record['id']: record['date_time'] for record in all_date}

    # Thay thế giá trị datetime_record_id trong all_data
    for data_record in all_data:
        date_time = date_mapping.get(data_record['datetime_record_id'])
        if date_time:
            data_record['date_time'] = date_time.strftime("%m-%d-%Y")
        else:
            data_record['date_time'] = None  # hoặc xử lý theo ý bạn

    # print(all_data)
    return render(request, 'index.html', {'all_data': all_data})

def get_data_day(request):
    all_data = HourlyData.objects.values()
    all_date = DateTimeRecord.objects.values()
    date_mapping = {record['id']: record['date_time'] for record in all_date}
    for data_record in all_data:
        date_time = date_mapping.get(data_record['datetime_record_id'])
        if date_time:
            data_record['date_time'] = date_time.strftime("%m-%d-%Y")
        else:
            data_record['date_time'] = None
    # print(all_data)
    return JsonResponse(list(all_data), safe=False)




def char(request):
    return render(request, 'char.html')