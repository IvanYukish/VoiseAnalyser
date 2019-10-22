#!/usr/bin/env python3
import cgi
import cgitb

from classes import Usids, Sessions

cgitb.enable()

form = cgi.FieldStorage()
action = form.getfirst('action')

login = form.getfirst('login')
password = form.getfirst('password')

if not (login and password and action):
    print('''Content-type:text/html\r\n\r\n
    <!DOCTYPE HTML>
    <html>
    <head><meta charset="utf-8"><title>LOGED </title></head>
    <body>
    <a href="http:/index.html">To begin</a>    
    <p>ВЫЗОВ НЕ ИЗ ФОРМЫ !!!!  ( или другая причина аварии )</p>

    </body>
    </html>''')

else:
    usid = Usids().get(login, password)
    if not usid:
        print(
            """Content-type: text/html\n
            <!DOCTYPE HTML>
            <html>
            <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
            </head>
            <body>""")
        print(
            "<a href=\"http:/index.html\">To begin</a>"
            "<p>Такий користувач не зареєестрований</p>")
        print("""</body></html>""")

    else:
        session = Sessions().new_sessions(usid)
        print(
            """Content-type: text/html\n
            <!DOCTYPE HTML>
            <html>
            <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title
            </head>
            <body>""")
        print("Вітаємо</p>")
        print(
            "<a href=\"/cgi-bin/logout.py?usid=USID&seskey=SESKEY\">LOGOUT</a>".format(
                usid, session)
        )
        print(
            "<p><a href = \"/cgi-bin/upload.py?usid={}&seskey={}\"> UPLOAD </a></p>".format(
                usid, session))

        print("""</body></html>""")
