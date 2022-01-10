import subprocess
from time import sleep

def cron_request():
    attempt = subprocess.check_output(['sh', 'curl_command.sh'], stderr=subprocess.PIPE, timeout=5.0)

    # decode the bytes to string
    attempt = attempt.decode('utf-8')

    # print output of curl command to cron_request.log
    with open('cron_response.log', 'a') as f:
        f.write(attempt)
        f.write('\n')
        f.close


if __name__ == '__main__':
    while True:
        try:
            cron_request()
        except:
            pass
        finally:
            sleep(0.5)