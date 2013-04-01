# -*- coding: utf8 -*-
import urllib
from bs4 import BeautifulSoup, Comment, Tag


def preprocess(soup):
    for style in soup.find_all('style'):
        style.extract()

    for style in soup.find_all('script'):
        style.extract()

    for style in soup.find_all('link'):
        style.extract()

    for style in soup.find_all('class'):
        style.extract()

    for style in soup.find_all('meta'):
        style.extract()

    for style in soup.find_all('base'):
        style.extract()

    for style in soup.find_all('em'):
        style.extract()

    for style in soup.find_all('form'):
        style.extract()

    for style in soup.find_all('iframe'):
        style.extract()

    for style in soup.find_all('noscript'):
        style.extract()
        
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]



def replaceprocess(soup):
    for a in soup.findAll('div'):
        a.name = 'table'

    for a in soup.findAll('body'):
        a.name = 'table'

    for a in soup.findAll('ul'):
        a.name = 'table'

    for a in soup.findAll('span'):
        a.name = 'table'

    for style in soup.find_all('p'):
        style.replaceWithChildren()

    for style in soup.find_all('li'):
        style.replaceWithChildren()


def denoising(soup):
    for style in soup.find_all('table'):
        if style.text.find(u'，') == -1:
            style.extract()
        else:
            linkNum = len(style.find_all('a'))
            textNum = len(style.text)
            if textNum == 0:
                style.extract()
            else:
                if linkNum * 1.0 / textNum > 0.1:
                    style.extract()
                else:
                    print linkNum, textNum
                    
                
            
            #raw_input('>>>')
            #print style.contents.count("<a")
            #    print style.text
    

    #soup.div.string.wrap(soup.new_tag("b"))

    #for a in soup.findAll('div'):
    #    print dir(a)
    #    new_tag = soup.new_tag("table")
    #    new_tag.string = a.text
        #print a.text
        
    #    a.replaceWith(new_tag)
       
        #print a
        #a.replaceWith(new_tag)
        #print a
        #print soup.table
    
    #new_tag = soup.new_tag("table")
    #print new_tag
    #print soup.div
    #soup.div.replaceWith(new_tag)
        #p = Tag(soup, 'p', [('id', 1)]) #create a P element
        #print p
        #a.replaceWith(p)   #Put it where the A element is


def extract(soup):
    textNum = len(soup.text)
    linkNum = len(soup.find_all('a'))
    rate = linkNum * 1.0 / textNum
    print 'raw rate is', rate
    text = u''
    desTag = None
    for tag in soup.find_all('table'):
        tmpNum = len(tag.text)
        tmpLink = len(tag.find_all('a'))
        tmpRate = tmpLink * 1.0 / textNum
        print 'rate is', tmpRate, rate
        if  tmpRate <= rate:
            text = tag.text
            rate = tmpRate
            desTag = tag
            #print text
    #print tag
    #print dir(tag)
    print type(desTag)
    #print type(desTag.contents[0])
    from  html2text import html2text
    text = html2text(unicode(desTag))
    # text
    f = open('test2.txt', 'w')
    f.write(text.encode('utf8'))
    f.close()
        
'''
soup = BeautifulSoup("<p><c>I wish I was bold.</c></p>")
#print dir(soup.p)
soup.p.name = 'test'
#soup.p.replaceWithChildren()
print soup.prettify()


raw_input(">>>")
soup.p.wrap(soup.new_tag("div"))
print soup.prettify()
raw_input(">>>")
'''

#url = 'http://ent.163.com/13/0319/06/8QAD0IQB00031H2L.html'

#url = 'http://bbs.whnet.edu.cn/cgi-bin/bbsnewtcon?board=Job&file=M.1363656496.A#'

#url = 'http://bbs.whnet.edu.cn/cgi-bin/bbsnewtcon?board=Job&file=M.1363923374.A'
#url = 'http://news.sina.com.cn/c/2013-03-19/174326578518.shtml'

#url = 'http://bbs.whu.edu.cn/wForum/disparticle.php?boardName=Job&ID=1110472305&pos=5'
#url = 'http://job.hust.edu.cn/show/article.htm?id=22428'
url = 'http://job.hb.qq.com/1212/3925.html'
#url = 'http://bbs.whu.edu.cn/wForum/disparticle.php?boardName=JobInfo&ID=30766&pos=17'
rsp = urllib.urlopen(url)

data =  rsp.read()
#print data



soup = BeautifulSoup(data, fromEncoding="gb18030")
preprocess(soup)



replaceprocess(soup)
f = open('test.txt', 'w')
f.write(soup.prettify().encode('gbk', 'ignore'))
f.close()

denoising(soup)



extract(soup)

#print soup.prettify().encode('utf8')


