from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.http import Http404
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
from api.models import Fuzzer, Crash, Storage
from django.contrib.auth.models import User
import time


@login_required
def index(request):
    try:
        fuzzer = Fuzzer.objects.filter(owner=request.user)
        crash = Crash.objects.filter(owner=request.user)
        storage = Storage.objects.filter(owner=request.user)
        user = User.objects.all()
    except ObjectDoesNotExist:
        raise Http404

    context = {'crash': crash, 'fuzzer': fuzzer, 'storage': storage, 'user': user}
    return render(request, 'web/index.html', context)


@login_required
def fuzzer(request):
    try:
        fuzzer = Fuzzer.objects.filter(owner=request.user)
    except ObjectDoesNotExist:
        raise Http404
    active_time = datetime.now() - timedelta(minutes=5)
    context = {'fuzzer_list': fuzzer, 'active_time': active_time}
    return render(request, 'web/fuzzer.html', context)


@login_required
def fuzzer_detail(request, idx):
    try:
        fuzzer = Fuzzer.objects.get(owner=request.user, id=idx)
    except ObjectDoesNotExist:
        raise Http404
    context = {'fuzzer':fuzzer}
    return render(request, 'web/fuzzer_detail.html', context)


@login_required
def crash(request):
    try:
        crash = Crash.objects.filter(owner=request.user, is_dup_crash=False, parent_idx=0)
    except ObjectDoesNotExist:
        raise Http404
    context = {'crash_list':crash}
    return render(request, 'web/crash.html', context)


@login_required
def crash_detail(request, idx):
    try:
        crash = Crash.objects.get(owner=request.user, id=idx)
    except ObjectDoesNotExist:
        raise Http404
    context = {'crash':crash}
    return render(request, 'web/crash_detail.html', context)


@login_required
def storage(request):
    try:
        storage = Storage.objects.filter(owner=request.user)
    except ObjectDoesNotExist:
        raise Http404
    context = {'storage_list':storage}
    return render(request, 'web/storage.html', context)


@login_required
def storage_detail(request, idx):
    try:
        storage = Storage.objects.get(owner=request.user, id=idx)
    except ObjectDoesNotExist:
        raise Http404
    context = {'storage':storage}
    return render(request, 'web/storage_detail.html', context)


@login_required
def api_docs(request):
    context = {}
    return render(request, 'web/api_docs.html', context)


@login_required
def sweetmon_client(request):
    context = {}
    return render(request, 'web/sweetmon_client.html', context)


def error_not_found(request):
    return render(request, 'web/common/404.html')


def error_internal_error(request):
    return render(request, 'web/common/500.html')
