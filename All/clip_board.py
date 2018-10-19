# -*- coding:utf-8 -*-
import subprocess

def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    #这里的data为bytes类型，之后需要转成utf-8操作
    return data
def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    p.communicate()

txt=str(getClipboardData(),'utf-8')
txt=txt.strip().replace('\r\n',' ').replace('\r',' ').replace('\n',' ')
print(txt)
#重新转成bytes型
data=bytes(txt,'utf8')
setClipboardData(data)
