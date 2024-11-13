import time

from django.utils.deprecation import MiddlewareMixin


class TimeExecution(MiddlewareMixin):

    def process_request(self, request):
        self.start_time = time.time()
        print(self.start_time)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('It is processing')

    def process_template_response(self, request, response):
        print('It is processing template response before loading the context in the templates')
        return response

    def process_response(self, request, response):
        self.end_time = time.time()
        print(self.end_time)
        print(f'The needed time that view was executed is {self.end_time - self.start_time}')
        return response
