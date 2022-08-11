import csv
import json
import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import zipfile
from django.template import loader
import os
from .models import Document


# Create your views here.
@login_required(login_url='/login')
def dashboard(request):
    return render(request, "prototype/dashboard.html")


def splita(request):
    if request.method == "POST":
        # this is the data in the file
        file_settings = request.FILES['selectedfile']
        # this is the file name extracted from the file and should include the file extension
        file_name = file_settings.name
        # getting out the file extension from the file name
        file_ext = file_name.split('.')[1]
        # this is the chunk size as provided by the user
        chunk_size = int(request.POST['chunk_row_size'])
        #user = request.user

       # if chunk_size <= 0 or file_settings is None:
        #messages.error(request, "Fields cannot be empty!")
        # return redirect('prototype/dashboard.html')

        if file_ext in ("csv", "json"):
            data_set = pd.read_csv(file_settings, chunksize=chunk_size)
            counter = 0

            for chunk in data_set:
                with zipfile.ZipFile(f"media/{file_name}.zip", 'a') as zip_file:
                    file_name = file_name + str(counter) + f'.{file_ext}'
                    zip_file.write(chunk.to_csv(file_name, index=False))
                os.remove(file_name)
                counter += 1

            csv_file = Document.objects.create(docfile=f"{file_name}.zip")
            csv_file.save()

            messages.info(request, "Split completed")
            return render(request, 'prototype/storage.html')

        messages.error(
            request, "Invalid file format, Please upload a valid csv or json file")
        return redirect('prototype/dashboard.html')

    return render(request, 'prototype/dashboard.html')


def storage(request):
    template = loader.get_template('prototype/storage.html')
    return HttpResponse(template.render())
    # return render(request, 'prototype/storage.html')
    #mydocuments = Document.objects.all().values()
    #template = loader.get_template('storage.html')
    # context = {
    # 'mydocuments' : mydocuments,
    # }
    # return HttpResponse(template.render(context, request))
    # return render(request, (output))
