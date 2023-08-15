# PythonAPI
Django API testing purposes


Installing Python:
Download and install python for windows from the following link -> https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe
MAKE SURE TO CHECK THE OPTION "Add Python.exe to System PATH" ONCE IT SHOWS UP!!!

Exeucting the project:
1. Clone the repo in a folder
2. Open VS Code -> Open Folder -> Select folder where you cloned the repo
3. Go to myproject/settings.py line 79 and modify database configuration (The project uses mySQL DB)
4. Open a terminal and run the following commands:
   - env\Scripts\Activate #This will activate the virtual env
   - pip install -r requirements.txt #Install required libraries
   - python manage.py runserver #Run the server by default port 8000
  
You are all set!
Happy hacking!
