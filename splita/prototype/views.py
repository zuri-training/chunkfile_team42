from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from zipfile import ZipFile
import pandas as pd
import os
import uuid


# Create your views here.
def splita(request):
    if request.method == "POST":

        file_settings = request.FILES['file']
        file_name = request.POST['file_name']
        if file_name == "":
            file_name = file_settings.name
        chunk_size = int(request.POST['chunk_size'])
        user = request.user

        if chunk_size == "" or file_settings is None:
            messages.error(request, "Fields cannot be empty!")
            return redirect('/')

        if file_settings.endswith(".csv", ".json"):
            counter = 0
            for chunks in pd.read_csv(file_settings, chunksize=chunk_size):
                with ZipFile(f"media/{file_name}-.zip", 'a') as zip:
                    file_name = f"{file_name}-" + str(counter) + ".csv"
                    zip.write(file_name,chunks.to_csv(file_name, index=False))
                os.remove(file_name)
                counter += 1

            csv_file = File.objects.create(user=user, file=f"{user}{file_name}-.zip")
            csv_file.save()

            messages.info(request, "Split completed")
            return redirect('/storage')

        messages.error(request, "Invalid file format, Please upload a valid csv or json file")
        return redirect('/dashboard')

    return render(request, 'dashboard.html')




