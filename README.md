#Arachne

Control your scrapy spiders through a flask app

```
twistd -n web --port 8080 --wsgi app.app
```


```ini
[global]
path = /your/path/to/arachne/
debug = True ; False on production
secret_key = AnyRandomStringYouPleaseButKeepItVeryVerySecret
server_name = local

[sqllite]
name = arachne

[mandrill]
key = MANDRILL_API_KEY
from_email = your@email.com
from_name = Your Name
smtp_host = smtp.mandrillapp.com
smtp_to_user = your@email.com
smtp_username = your@email.com
```
