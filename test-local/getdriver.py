import os
import platform
import re
import stat
import subprocess
import sys
import zipfile

import requests

sys_platform = platform.system()
page = requests.get('https://chromedriver.chromium.org/downloads/')

# Installed version
if sys_platform == 'Windows':
    cmd = (r'dir /B/AD "C:\Program Files (x86)\Google\Chrome\Application\" | '
           r'findstr /R /C:"^[0-9].*\..*[0-9]$"')
    versions_list = (subprocess.check_output(cmd, shell=True)
                     .decode().strip().split('\r\n'))
    installed_version = sorted(
        versions_list,
        key=lambda s: [int(i) for i in s.split('.')]
    )[-1]
elif sys_platform == 'Linux':
    cmd = 'google-chrome --version'
    installed_version = os.popen(cmd).read().strip().split()[-1]
else:
    cmd = (r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome '
           '--version')
    installed_version = os.popen(cmd).read().strip().split()[-1]

# Available version
print(f'Version: {installed_version}')
search_str = '.'.join(installed_version.split('.')[:-1])
check_ver = int(search_str.split('.')[0])
if check_ver > 72:
    version = re.search(rf'{search_str}.\d+', page.text).group()
elif check_ver > 70:
    version = '2.46'
elif check_ver > 69:
    version = '2.45'
elif check_ver > 68:
    version = '2.44'
elif check_ver > 67:
    version = '2.42'
elif check_ver > 66:
    version = '2.41'
elif check_ver > 65:
    version = '2.40'
elif check_ver > 64:
    version = '2.38'
elif check_ver > 63:
    version = '2.37'
elif check_ver > 62:
    version = '2.36'
elif check_ver > 61:
    version = '2.35'
elif check_ver > 60:
    version = '2.34'
elif check_ver > 59:
    version = '2.33'
elif check_ver > 56:
    version = '2.28'
elif check_ver > 53:
    version = '2.25'
elif check_ver > 52:
    version = '2.24'
elif check_ver > 50:
    version = '2.22'
elif check_ver > 43:
    version = '2.19'
elif check_ver > 41:
    version = '2.15'
else:
    print('Driver not found')
    sys.exit()

# Zip name
if sys_platform == 'Windows':
    filename = 'chromedriver_win32.zip'
elif sys_platform == 'Linux':
    filename = 'chromedriver_linux64.zip'
else:
    filename = 'chromedriver_mac64.zip'

# Download
url = f'https://chromedriver.storage.googleapis.com/{version}/{filename}'
print(f'Url: {url}')
reply = requests.get(url)
open(filename, 'wb').write(reply.content)

# Unzip
with zipfile.ZipFile(filename, 'r') as zip:
    zip.printdir()
    zip.extractall()

# Set permission
if sys_platform != 'Windows':
    os.chmod('chromedriver', stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)

# Delete
os.remove(filename)
