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
        "<h1>Form Handling</h1>"'<p>Нет ключа сесии</p>')
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
        "<h1>Form Handling</h1>"'<p>зашли не из форми</p>')
    print("""</body></html>""")

else:
    ses = Sessions().refresh(usid, syskey)
    if not ses:
        print('''Content-type:text/html\r\n\r\n''')
        print("""<!DOCTYPE HTML>
</html>
<html>
<head>
    <meta charset="utf-8">
    <title>LOGED </title></head>
<body>


<h1>
<a href=\"/cgi-bin/logout.py?usid={}&seskey={}\">LOGOUT</a>
IT IS UPLOAD.</h1>

</body>
</html>
    """.format(usid, syskey))
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
            "<h1>Form Handling</h1>"'<p>проблема с session refrech</p>''<a href="http:/index.html">To begin</a>')
        print("""</body></html>""")
