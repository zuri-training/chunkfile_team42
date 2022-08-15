# chunkfile_team42


Team42 is engaged in building a platform that manipulates files with emphasis on chunking large csv and json files.

# Welcome

Welcome to Splita doc,we are working to create a simple and user friendly platform that splits csv and json files. Below is a short guide to help you through the splitting process.


# Our Solution


Are you running out of storage because your file sizes are too large? Are large files slowing your system down? Are you looking for a way to solve these problems? Solution: Splita. Splita is a free web platform that lets you split large csv and json files into small sizes we call chunks. The chunked sizes can be manually selected so that users can set their own chunk size.You can upload files from your local machine or your cloud service provider straight to Splita to start the process.After splitting your files you have a choice to immediately download your chunks or save them to a cloud service provider of your choice (Google Drive,Dropbox or one drive).


Splita is powered by Django framework, HTML, CSS, Javascript and MYSQL.


Splita is a free web platform,however to be able to perform all the above ,the platform will require you to Sign up or log in first. Authenticated users will be redirected to a dashboard that lets you split your files as you wish. Unauthenticated users can however go through our landing page and documentation to better understand  the service. 

# Technical Issues

Splita has been designed to be user-friendly and we have tried to tackle any technical issues. However, in the event where you face an unfortunate technical issue,contact support and our technical support team will contact you and we will be able to come up with a solution as fast as possible. 

## How to use?

> - Login/signup on our website

>- Upload a file

>- Specify the chunk size by the number of rows you want

>- Click on the chunk button

>- The file will be chunked and saved as .zip, ready for download


If you want to run our project locally, you can do so by running the following commands:

Clone the project

```
  git clone https://github.com/zuri-training/chunkfile_team42
```

Go to the project directory

```


cd splita

```

Create a Virtual Environment

```

python -m venv venv

```

Activate Virtual Environment

```

venv\scripts\activate

```

Install Dependencies

```

pip install -r requirements.txt

```

make migrations using
```
 python manage.py makemigrations

```

Migrate the database using 

```
python manage.py migrate

```

create superuser using

```
python manage.py createsuperuser

```

Finally, Start The Server using 
```
python manage.py runserver
```

​
## Developers Tools
>This site was built using the following tools:
>* HTML
>* CSS
>* jAVASCRIPT
>* PYTHON(Django)
​
