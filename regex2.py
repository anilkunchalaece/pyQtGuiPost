page = '''<q><imgclass="alignnonesize-mediumwp-image-5"src="http://pythonlayout.16mb.com/wp-content/uploads/2016/08/obama-300x300.jpg"alt="obama"width="300"height="300"/>identy this person?</q>'''

getQue = r"\<q\>(.+?)\<\/q\>"

getImg = r"src\=\"(.+?)\.jpg"

getImQue = r"\>(.+?)$"

import re

out =  re.findall(getQue,page.translate(None,'\t\n\r'))
img=  re.findall(getImg,out[0])
if img :
    print re.findall(getImQue,out[0])
    print 'Got Image'
else:
    print img
    print "it Does not have Image"
