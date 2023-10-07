import ftplib

def anonlogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' + str(hostname) + ' FTP Anonymous Login Succeeded.')
        ftp.quit()
        return True

    except Exception:
        print('\n [-] ' + str(hostname) + ' FTP Anonymous Login Fails.')
        return False


if __name__ == '__main__':
    anonlogin('5.253.61.53')
