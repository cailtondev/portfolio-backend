from django.http import JsonResponse
from .models import *
from django.views import View
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


class BaseAPIView(View):
    model = None
    fields = []

    def get_data(self):
        return self.model.objects.values('id', *self.fields)

    def get(self, request, *args, **kwargs):
        data = self.get_data()
        return JsonResponse(list(data), safe=False)


class HomeAPIView(BaseAPIView):
    model = Home
    fields = ['title']


class WebDevelopmentOfferAPIView(BaseAPIView):
    model = WebDevelopmentOffer
    fields = ['title', 'paragraph']


class WebDevelopmentCardAPIView(BaseAPIView):
    model = WebDevelopmentCard
    fields = ['offer', 'card_title', 'card_paragraph']


class WebDevelopmentTechnologiesAPIView(BaseAPIView):
    model = WebDevelopmentTechnologies
    fields = ['title', 'icon_link']


class WebDevelopmentProjectsAPIView(BaseAPIView):
    model = WebDevelopmentProjects
    fields = ['tag', 'title', 'paragraph',
              'image_link', 'alt_image', 'link_preview']


class ResumeMEAPIView(BaseAPIView):
    model = ResumeME
    fields = ["title", "paragraph"]


class ContactAPIView(BaseAPIView):
    model = Contact
    fields = ["title", "paragraph", "email", "phone", "address"]
