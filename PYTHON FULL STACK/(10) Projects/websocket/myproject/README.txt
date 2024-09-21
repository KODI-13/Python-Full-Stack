Requirements
- Python version 3.10.1  to install PMClient library

step 1 == install virtual environment using """pip install env""" command

step 2 == we have to create virtual environment folder using """py -m venv myenv""" command

step 3 ==  after creeating virtual environment you have to activate the virtual environment 
           for these you have to go in cmd and using commands you have to go inside in the Scripts folder and reach to  activate file
           e.g
            """myenv\Scripts\activate.bat"""  

step 4 == you have to download django using """pip install django""" command
          we can intstall this in virtual environment or in entire system
          we must have to activate venv before intall django

step 5 == we have to project folder with the help of django-admin using 
            """django-admin startproject myproject"""
            "django-admin" command gives the sub-command of django (*NOTE = if you don't know the commands of django)

step 6 == after creating myproject we have to create myapp in the myproject folder with the help of python manager.py 
         to access mange.py first we need to change directory and enter to myproject folder 
         to do this use following command 
         """cd myproject"""

step 7 == after changing directory we will create myapp in the myproject folder with the help of python manager.py  using following command
            """py manage.py startapp myapp"""


step 8 == now install your app (i.e myapp) by writing its name in INSTALLED APP of setiings.py

step 9 == create a urls.py in myapp in which crate a url that will call the function inside of views.py

step10 == after calling function a request will be recived as an output we will reder render request with an html page

step10 == load javascript in html page (html page location --> myapp/templates/myapp) 


                                  TO RUN THIS PROJECT 

step 11 == just have to provide websocket url in javascriptfile at this location
            const socket = new WebSocket('ws://your-websocket-server-url');   // just have to provide websocket server url

step 12 == then have to add api url in views.py in follwing function 

            def connect_to_websocket(self):
                # just have to Replace it with the actual endpoint and any other necessary configuration
                ws_url = "wss://paytm_money_api_url"                

step 13 == and finally have to add token which is recived FROMb << paytm money API DOCUMENTATION  >>
            def home(request):
                # just have to replace 'token' with the actual token you receive for the day
                token = 'token'

step 14 ==  to check if our project implementation wse following command
            """py manage.py runserver"""