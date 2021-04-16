from ftplib import FTP

host = "ftp.ambient-studio.uz"
user = "test@ambient-studio.uz"
password = "Bacon#2020"

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    with open('test.txt', 'wb') as f:
        ftp.retrbinary("RETR " + "test.txt", f.write, 1024)

    with open('uploads.txt', 'rb') as f:
        ftp.storbinary('STOR ' + 'upload.txt', f)

    ftp.cwd("new")
    with open('specfile.txt', 'wb') as t:
        ftp.retrbinary('RETR '+'newfile.txt', t.write, 1024)
        

    ftp.quit()


