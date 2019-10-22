#!/usr/bin/env python3
import cgi
import cgitb

from classes import Sessions

cgitb.enable()

form = cgi.FieldStorage()
syskey = form.getfirst("seskey", "")
usid = form.getfirst("usid", "")

if not syskey:
    print('''Content-type:text/html\r\n\r\n
    <!DOCTYPE html>
        <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>login</title>
    </head>
    <body>''')
    print(
        "<h1>Form Handling</h1>"'<p>Нет ключа сесии</p>''<a href="http:/index.html">To begin</a>')
    print("""</body></html>""")

elif not usid:
    print('''Content-type:text/html\r\n\r\n
    <!DOCTYPE html>
        <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>login</title>
    </head>
    <body>''')
    print(
        "<h1>Form Handling</h1>"'<p>зашли не из форми</p>''<a href="http:/index.html">To begin</a>')
    print("""</body></html>""")

else:
    rez = Sessions().del_sessions(usid, syskey)
    if not rez:

        print("Content-type: text/html\n")

        print('''<!DOCTYPE HTML>
        </html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>LOGGOUT</title></head>
        <body>
        <h1>ви вийшли</h1>
        <a href="/">Перейти на головну сторінку</a>
        </body>
        </html>''')



    else:
        print('''Content-type:text/html\r\n\r\n
        <!DOCTYPE html>
            <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>login</title>
        </head>
        <body>''')
        print(
            "<h1>Form Handling</h1>"'<p>проблема с session del</p>''<a href="http:/index.html">To begin</a>')
        print("""</body></html>""")
