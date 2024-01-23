import datetime
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.warning(
        "Homepage was accessed at " + str(datetime.datetime.now()) + " hours!"
    )
    return render(request, "index.html")


def page1(request):
    return render(request, "page1.html")
