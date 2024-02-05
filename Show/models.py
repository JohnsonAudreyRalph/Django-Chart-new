# myapp/models.py
from django.db import models
from datetime import datetime, timedelta

class DateTimeRecord(models.Model):
    date_time = models.DateField(unique=True)

    def __str__(self):
        return str(self.date_time)

class HourlyData(models.Model):
    datetime_record = models.ForeignKey(DateTimeRecord, on_delete=models.CASCADE)
    hour_1_data = models.FloatField(null=True, blank=True)
    hour_2_data = models.FloatField(null=True, blank=True)
    hour_3_data = models.FloatField(null=True, blank=True)
    hour_4_data = models.FloatField(null=True, blank=True)
    hour_5_data = models.FloatField(null=True, blank=True)
    hour_6_data = models.FloatField(null=True, blank=True)
    hour_7_data = models.FloatField(null=True, blank=True)
    hour_8_data = models.FloatField(null=True, blank=True)
    hour_9_data = models.FloatField(null=True, blank=True)
    hour_10_data = models.FloatField(null=True, blank=True)
    hour_11_data = models.FloatField(null=True, blank=True)
    hour_12_data = models.FloatField(null=True, blank=True)
    hour_13_data = models.FloatField(null=True, blank=True)
    hour_14_data = models.FloatField(null=True, blank=True)
    hour_15_data = models.FloatField(null=True, blank=True)
    hour_16_data = models.FloatField(null=True, blank=True)
    hour_17_data = models.FloatField(null=True, blank=True)
    hour_18_data = models.FloatField(null=True, blank=True)
    hour_19_data = models.FloatField(null=True, blank=True)
    hour_20_data = models.FloatField(null=True, blank=True)
    hour_21_data = models.FloatField(null=True, blank=True)
    hour_22_data = models.FloatField(null=True, blank=True)
    hour_23_data = models.FloatField(null=True, blank=True)
    hour_24_data = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.datetime_record.date_time)

    def update_hourly_data(self, new_data):
        current_time = datetime.now().date()
        delta_time = current_time - self.datetime_record.date_time
        delta_days = delta_time.days

        if delta_days < 1:
            field_name = f"hour_{delta_days * 24 + 1}_data"
            setattr(self, field_name, new_data)
            self.save()
        else:
            new_record = HourlyData.objects.create(datetime_record=self.datetime_record)
            new_record.update_hourly_data(new_data)