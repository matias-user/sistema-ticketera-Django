from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from ticket.models import Ticket

import pandas as pd
# Create your views here.

class ExportTicketView(View):
    def get(self, request, *args, **kwargs):
        tickets = Ticket.objects.all().values()

        df = pd.DataFrame(list(tickets))

        for col in df.select_dtypes(include=['datetimetz']):
            df[col] = df[col].dt.tz_convert(None)

        response = HttpResponse(
            content_type= 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        response['Content-Disposition'] = 'attachment; filename=tickets.xlsx'

        df.to_excel(response, index=False)
        return response