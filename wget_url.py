#################################################
# use wget to download a file, 
# and then check it is success or not
# 
# Time: 20140813
# Usage: 
#   python wget_url.py http://www.baidu.com/swfupload.swf
#################################################

import sys
import os
import os.path

def download():
    url = sys.argv[1]

    if not os.path.exists('tmp/'):
        os.mkdir('tmp')

    print "[*] Downloading the file...."

    os.system("wget "+url)
    os.system("mv *.swf tmp/")

    swfname = url.split('/').pop()

    if open('tmp/'+swfname):
        return swfname
    else:
        print("[-] Download Failed!")

if __name__ == '__main__':
    download()
