from django.contrib import admin
from .models import HourlyData

# Register your models here.
@admin.register(HourlyData)
class Model_admin(admin.ModelAdmin):
    list_display = ('id', 'datetime_record', 'hour_1_data', 'hour_2_data', 'hour_3_data', 'hour_4_data','hour_5_data','hour_6_data','hour_7_data','hour_8_data','hour_9_data','hour_10_data','hour_11_data','hour_12_data','hour_13_data','hour_14_data','hour_15_data','hour_16_data','hour_17_data','hour_18_data','hour_19_data','hour_20_data','hour_21_data','hour_22_data','hour_23_data','hour_24_data')