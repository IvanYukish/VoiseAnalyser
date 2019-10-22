import time
import hashlib

time_delta = 60


class Usids:

    def get(self, login, password):
        try:
            if int(login) == int(password):
                usid = login
                return usid

        except ValueError:
            self.errors()

    @staticmethod
    def errors():
        print('error')


class Sessions:
    def new_sessions(self, usid):
        ses_key = hashlib.md5(str(usid).encode())
        time_sessions = round(time.time())
        with open("sessions.txt", "a") as somefile:
            somefile.write(f'{usid};{ses_key.hexdigest()};{time_sessions},')

        return ses_key.hexdigest()

    def del_sessions(self, usid, seskey):
        with open("sessions.txt", "r") as somefile:
            flag = False
            new_date = round(time.time())
            lst_ses = (','.join(list(somefile))).split(',')[:-1]
            item = f'{usid};{seskey}'
            for i in lst_ses:
                if item in i:
                    if (new_date - int(i.split(';')[2])) < time_delta:
                        flag = True
                        lst_ses.remove(i)
        if flag:
            with open("sessions.txt", "w") as somefile:
                somefile.write(
                    str(lst_ses).replace('[', '').replace(']', '').replace(
                        '\'', '').replace(' ', ''))
                somefile.write(',')
            return 0
        else:
            self.error()

    def refresh(self, usid, seskey):
        with open("sessions.txt", "r") as somefile:
            flag = False
            new_date = round(time.time())
            lst_ses = (','.join(list(somefile))).split(',')[:-1]
            item = f'{usid};{seskey}'
            for index, i in enumerate(lst_ses):
                if item in i:
                    if (new_date - int(i.split(';')[2])) < time_delta:
                        flag = True
                        lst_ses[index] = f'{item};{new_date}'

        if flag:
            with open("sessions.txt", "w") as f:
                f.write(
                    str(lst_ses).replace('[', '').replace(']', '').replace(
                        '\'', '').replace(' ', ''))
                f.write(',')

            return 0
        else:
            return self.error()

    def error(self):
        print('Error: session not found')
