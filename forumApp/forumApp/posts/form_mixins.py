from datetime import time

from django import forms
from django.http import HttpResponseForbidden
from django.utils.timezone import localtime


class DisabledMixin(forms.Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field in self.disabled_fields or self.disabled_fields == '__all__':
                self.fields[field].disabled = True


class TimeDistrictMixin:
    start_time = time(9, 0)
    end_time = time(23, 0)
    forbidden_message = "Access restricted at this time. Try again later!"

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        local_time = localtime().time()

        if not (self.start_time <= local_time <= self.end_time):
            return HttpResponseForbidden(self.forbidden_message)

        return super().dispatch(request, *args, **kwargs)