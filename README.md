#Arachne

_WARNING: This project is still in it's nascent stage so needs a lot of manual configuration._


You can control your scrapy spiders through a flask app. All you have to do is upload your spiders into the __spiders/__ directory and controll them using the spiders web UI.


###Getting started:
Install dependencies (it still doesn't have all the dependencies)
```
pip install -r requirements.txt
```

Add a __config.ini__ file in the root folder of this project.
```ini
[global]
path = /your/path/to/arachne/
debug = True ; False on production
secret_key = AnyRandomStringYouPleaseButKeepItVeryVerySecret
server_name = local

[sqllite]
name = arachne

; This is for my SMTP logger
[mandrill] 
key = MANDRILL_API_KEY
from_email = your@email.com
from_name = Your Name
smtp_host = smtp.mandrillapp.com
smtp_to_user = your@email.com
smtp_username = your@email.com
```

Start running using the command
```
twistd -n web --port 8080 --wsgi app.app
```

Open your browser and goto the location [http://localhost:8080](http://localhost:8080)

__Here's how the UI looks for the sample spiders in the project__
![Image of sample](http://kirankoduru.github.io/img/side-projects/arachne.png)
