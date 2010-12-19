#!/usr/bin/python

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,StringIO

#Icefilms.info v0.3 - anarchintosh 8/12/2010

#get settings
selfAddon = xbmcaddon.Addon(id='plugin.video.icefilms')
FlattenSrcType = selfAddon.getSetting('flatten-source-type')
FlattenMega = selfAddon.getSetting('flatten-megaupload')
DisableAtoZ = selfAddon.getSetting('AtoZ-list')

#access settings by using example boolean below:
#if DisableAtoZ == 'true':
#        print 'lol'

        
#useful global strings:
iceurl = 'http://www.icefilms.info/'


def CATEGORIES():
        addDir('TV Shows',iceurl+'tv/a-z/1',50,'http://i1224.photobucket.com/albums/ee364/froggermonster1/tvshows.png')
        addDir('Movies',iceurl+'movies/a-z/1',51,'http://i1224.photobucket.com/albums/ee364/froggermonster1/movies.png')
        addDir('Music',iceurl+'music/a-z/1',52,'http://i1224.photobucket.com/albums/ee364/froggermonster1/music.png')
        addDir('Stand Up Comedy',iceurl+'standup/a-z/1',53,'http://i1224.photobucket.com/albums/ee364/froggermonster1/standup.png')
        addDir('Other',iceurl+'other/a-z/1',54,'http://i1224.photobucket.com/albums/ee364/froggermonster1/other.png')


def TVCATEGORIES(url):
        caturl = iceurl+'tv/'        
        setmode = '11'
        if DisableAtoZ == 'false':
                addDir('A-Z Directories',caturl+'a-z/1',10,'')
        if DisableAtoZ == 'true':
                addDir('A-Z List',caturl+'a-z/',13,'')                
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def MOVIECATEGORIES(url):
        caturl = iceurl+'movies/'        
        setmode = '2'
        if DisableAtoZ == 'false':
                addDir('A-Z Directories',caturl+'a-z/1',1,'')
        if DisableAtoZ == 'true':
                addDir('A-Z List',caturl+'a-z/',3,'')
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def MUSICCATEGORIES(url):
        caturl = iceurl+'music/'        
        setmode = '2'
        addDir('A-Z List',caturl+'a-z/1',setmode,'')
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def STANDUPCATEGORIES(url):
        caturl = iceurl+'standup/'        
        setmode = '2'
        addDir('A-Z List',caturl+'a-z/1',setmode,'')
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def OTHERCATEGORIES(url):
        caturl = iceurl+'other/'        
        setmode = '2'
        addDir('A-Z List',caturl+'a-z/1',setmode,'')
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def MOVIEA2ZList(url):
        MOVIEINDEX(url+'1')
        MOVIEINDEX(url+'A')
        MOVIEINDEX(url+'B')
        MOVIEINDEX(url+'C')
        MOVIEINDEX(url+'D')
        MOVIEINDEX(url+'E')
        MOVIEINDEX(url+'F')
        MOVIEINDEX(url+'G')
        MOVIEINDEX(url+'H')
        MOVIEINDEX(url+'I')
        MOVIEINDEX(url+'J')
        MOVIEINDEX(url+'K')
        MOVIEINDEX(url+'L')
        MOVIEINDEX(url+'M')
        MOVIEINDEX(url+'N')
        MOVIEINDEX(url+'O')
        MOVIEINDEX(url+'P')
        MOVIEINDEX(url+'Q')
        MOVIEINDEX(url+'R')
        MOVIEINDEX(url+'S')
        MOVIEINDEX(url+'T')
        MOVIEINDEX(url+'U')
        MOVIEINDEX(url+'V')
        MOVIEINDEX(url+'W')
        MOVIEINDEX(url+'X')
        MOVIEINDEX(url+'Y')
        MOVIEINDEX(url+'Z')
        
        
def TVA2ZList(url):
        TVINDEX(url+'1')
        TVINDEX(url+'A')
        TVINDEX(url+'B')
        TVINDEX(url+'C')
        TVINDEX(url+'D')
        TVINDEX(url+'E')
        TVINDEX(url+'F')
        TVINDEX(url+'G')
        TVINDEX(url+'H')
        TVINDEX(url+'I')
        TVINDEX(url+'J')
        TVINDEX(url+'K')
        TVINDEX(url+'L')
        TVINDEX(url+'M')
        TVINDEX(url+'N')
        TVINDEX(url+'O')
        TVINDEX(url+'P')
        TVINDEX(url+'Q')
        TVINDEX(url+'R')
        TVINDEX(url+'S')
        TVINDEX(url+'T')
        TVINDEX(url+'U')
        TVINDEX(url+'V')
        TVINDEX(url+'W')
        TVINDEX(url+'X')
        TVINDEX(url+'Y')
        TVINDEX(url+'Z')

        
def MOVIEA2ZDirectories(url):
        setmode = '2'
        caturl = iceurl+'movies/a-z/'
        addDir ('#1234',caturl+'1',setmode,'')
        addDir ('A',caturl+'A',setmode,'')
        addDir ('B',caturl+'B',setmode,'')
        addDir ('C',caturl+'C',setmode,'')
        addDir ('D',caturl+'D',setmode,'')
        addDir ('E',caturl+'E',setmode,'')
        addDir ('F',caturl+'F',setmode,'')
        addDir ('G',caturl+'G',setmode,'')
        addDir ('H',caturl+'H',setmode,'')
        addDir ('I',caturl+'I',setmode,'')
        addDir ('J',caturl+'J',setmode,'')
        addDir ('K',caturl+'K',setmode,'')
        addDir ('L',caturl+'L',setmode,'')
        addDir ('M',caturl+'M',setmode,'')
        addDir ('N',caturl+'N',setmode,'')
        addDir ('O',caturl+'O',setmode,'')
        addDir ('P',caturl+'P',setmode,'')
        addDir ('Q',caturl+'Q',setmode,'')
        addDir ('R',caturl+'R',setmode,'')
        addDir ('S',caturl+'S',setmode,'')
        addDir ('T',caturl+'T',setmode,'')
        addDir ('U',caturl+'U',setmode,'')
        addDir ('V',caturl+'V',setmode,'')
        addDir ('W',caturl+'W',setmode,'')
        addDir ('X',caturl+'X',setmode,'')
        addDir ('Y',caturl+'Y',setmode,'')
        addDir ('Z',caturl+'Z',setmode,'')



def TVA2ZDirectories(url):
        setmode = '11'
        caturl = iceurl+'tv/a-z/'
        addDir ('#1234',caturl+'1',setmode,'')
        addDir ('A',caturl+'A',setmode,'')
        addDir ('B',caturl+'B',setmode,'')
        addDir ('C',caturl+'C',setmode,'')
        addDir ('D',caturl+'D',setmode,'')
        addDir ('E',caturl+'E',setmode,'')
        addDir ('F',caturl+'F',setmode,'')
        addDir ('G',caturl+'G',setmode,'')
        addDir ('H',caturl+'H',setmode,'')
        addDir ('I',caturl+'I',setmode,'')
        addDir ('J',caturl+'J',setmode,'')
        addDir ('K',caturl+'K',setmode,'')
        addDir ('L',caturl+'L',setmode,'')
        addDir ('M',caturl+'M',setmode,'')
        addDir ('N',caturl+'N',setmode,'')
        addDir ('O',caturl+'O',setmode,'')
        addDir ('P',caturl+'P',setmode,'')
        addDir ('Q',caturl+'Q',setmode,'')
        addDir ('R',caturl+'R',setmode,'')
        addDir ('S',caturl+'S',setmode,'')
        addDir ('T',caturl+'T',setmode,'')
        addDir ('U',caturl+'U',setmode,'')
        addDir ('V',caturl+'V',setmode,'')
        addDir ('W',caturl+'W',setmode,'')
        addDir ('X',caturl+'X',setmode,'')
        addDir ('Y',caturl+'Y',setmode,'')
        addDir ('Z',caturl+'Z',setmode,'')      

def CLEANUP(name):
# clean names of annoying garbled text
                name=re.sub('&#xC6;','AE',name)
                name=re.sub('&#x27;',"'",name)
                name=re.sub('&#xED;','i',name)
                name=re.sub('&frac12;',' 1/2',name)
                name=re.sub('&#xBD;',' 1/2',name)
                name=re.sub('&#x26;','&',name)
                name=re.sub('&#x22;','',name)
                name=re.sub('</a>','',name)
                name=re.sub('<b>HD</b>',' *HD 720p*',name)
                name=re.sub('&#xF4;','o',name)
                name=re.sub('&#xE9;',"e",name)
#                name=re.sub('&#x27;',"'",name)
                return name

def MOVIEINDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
# below is the original scraper that ignores HD tags.
#        match=re.compile('<img class=star><a href=/(.+?)>(.+?)</a>').findall(link)
        match=re.compile('<img class=star><a href=/(.+?)>(.+?)<br>').findall(link)
        for url,name in match:
                name=CLEANUP(name)
                addDir(name,iceurl+url,100,'')

def TVINDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<img class=star><a href=/(.+?)>(.+?)</a>').findall(link)
        for url,name in match:
                name=CLEANUP(name)
                addDir(name,iceurl+url,12,'')



def TVEPISODES(url):
# displays all episodes, with no unnecessary sub-directories for seasons. (this means it works even for 'the daily show with jon stewart' etc...)
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<img class=star><a href=/(.+?)>(.+?)</a>').findall(link)
        for url,name in match:
                name=CLEANUP(name)
                addDir(name,iceurl+url,100,'')

                
def LOADMIRRORS(url):
# This proceeds from the file page to the separate frame where the mirrors can be found,
# then executes code to scrape the mirrors
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('/membersonly/components/com_iceplayer/(.+?)" width=').findall(link)
        match[0]=re.sub('%29',')',match[0])
        match[0]=re.sub('%28','(',match[0])
        for url in match:
            mirrorpageurl = iceurl+'membersonly/components/com_iceplayer/'+url
        GETMIRRORS(mirrorpageurl)



def GETMIRRORS(url):
# This scrapes the megaupload mirrors from the separate url used for the video frame.
# It also displays them in an informative fashion to user.
# Displays in three directory levels: HD or DVDRip, Source, PART
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
#old scrape all mega links code
#        mulink=re.compile('http://www.megaupload.com/(.+?)>').findall(link)
#        for url in mulink:
#                fullmulink = 'http://www.megaupload.com/'+url
#                addDir(fullmulink,fullmulink,110,'')

#strings for checking the existence of categories
        dvdrip=re.compile('<div class=ripdiv><b>DVDRip / (.+?)</b>').findall(link)
        hd720p=re.compile('<div class=ripdiv><b>HD (.+?)</b>').findall(link)
        dvdscreener=re.compile('<div class=ripdiv><b>DVD Sc(.+?)</b>').findall(link)
        r5r6=re.compile('<div class=ripdiv><b>R5/(.+?) DVDRip</b>').findall(link)
        #hacky buffers
        outputone = StringIO.StringIO()
        outputone.write(dvdrip)
        dvdrip = outputone.getvalue()

        outputone = StringIO.StringIO()
        outputone.write(hd720p)
        hd720p = outputone.getvalue()

        outputone = StringIO.StringIO()
        outputone.write(dvdscreener)
        dvdscreener = outputone.getvalue()

        outputone = StringIO.StringIO()
        outputone.write(r5r6)
        r5r6 = outputone.getvalue()

        #set values to false by default

        
        #check that these categories exist, if they do set values to true.
        if len(dvdrip) >3:
                dvdrip = 'true'
        if len(hd720p) >3:
                hd720p = 'true'
        if len(dvdscreener) >3:
                dvdscreener = 'true'
        if len(r5r6) >1:
                r5r6 = 'true'
        #check that these categories exist, if they dont set values to false.
        if len(dvdrip) <1:
                dvdrip = 'false'
        if len(hd720p) <1:
                hd720p = 'false'
        if len(dvdscreener) <1:
                dvdscreener = 'false'
        if len(r5r6) <1:
                r5r6 = 'false'
     
        #only detect and proceed directly to adding sources if flatten sources setting is true
        if FlattenSrcType == 'true':
                #check if there is more than one directory
                if dvdrip == 'true' and hd720p == 'true':
                        only1 = 'false'
                if dvdrip == 'true' and dvdscreener == 'true':
                        only1 = 'false'
                if dvdrip == 'true' and r5r6 == 'true':
                        only1 = 'false'
                if dvdscreener == 'false' and r5r6 == 'false':
                        only1 = 'false'
                if hd720p == 'true' and dvdscreener == 'false':
                        only1 = 'false'
                if r5r6 == 'true' and hd720p == 'true':
                        only1 = 'false'
                #check if there is only one directory      
                if dvdrip == 'true' and hd720p == 'false' and dvdscreener == 'false' and r5r6 == 'false':
                        only1 = 'true'
                        DVDRip(url)
                if dvdrip == 'false' and hd720p == 'true' and dvdscreener == 'false' and r5r6 == 'false':
                        only1 = 'true'
                        HD720p(url)
                if dvdrip == 'false' and hd720p == 'false' and dvdscreener == 'true' and r5r6 == 'false':
                        only1 = 'true'
                        DVDScreener(url)
                if dvdrip == 'false' and hd720p == 'false' and dvdscreener == 'false' and r5r6 == 'true':
                        only1 = 'true'
                        R5R6(url)
                #add directories of source categories if only1 is false
                if only1 == 'false':
                        addCatDir(url,dvdrip,hd720p,dvdscreener,r5r6)
        #if flattensources is set to false, don't flatten                
        if FlattenSrcType == 'false':
                addCatDir(url,dvdrip,hd720p,dvdscreener,r5r6)     
                
def addCatDir(url,dvdrip,hd720p,dvdscreener,r5r6):
        if dvdrip == 'true':
                addDir('DVDRip',url,101,'')
        if hd720p == 'true':
                addDir('HD 720p',url,102,'')
        if dvdscreener == 'true':
                addDir('DVD Screener',url,103,'')
        if r5r6 == 'true':
                addDir('R5/R6 DVDRip',url,104,'') 
        
def PART(scrap,sourcenumber):
        #check for sources containing multiple parts
        source=re.compile('<p>Source #'+sourcenumber+': (.+?)PART 1(.+?)</i><p>').findall(scrap)
        for sourcescrape1,sourcescrape2 in source:
                sourcescrape=sourcescrape1+'PART 1'+sourcescrape2
                part=re.compile('&url=http://www.megaupload.com/?(.+?)>PART (.+?)</a>').findall(sourcescrape)
                for murl,name in part:
                        megaurl='http://www.megaupload.com/'+murl
                        partname='PART '+name
                        fullname='Source #'+sourcenumber+' | ['+partname+']'
                        if FlattenMega == 'true':
                                VIDEOLINKS(fullname,megaurl)
                        if FlattenMega == 'false':
                                addDir(fullname,megaurl,110,'')
        outputone = StringIO.StringIO()
        outputone.write(source)
        source10 = outputone.getvalue()

        #if scraper for multiple parts returns nothing....
        if len(source10) <5:
                #check if source exists
                source3=re.compile('Source #'+sourcenumber+': ').findall(scrap)
                outputone = StringIO.StringIO()
                outputone.write(source3)
                source3 = outputone.getvalue()
                if len(source3) >0:
                        #find corresponding '<a rel=?' entry and add as a one-link source
                        source5=re.compile('<a rel='+sourcenumber+'.+?&url=(.+?)>Source #'+sourcenumber+':').findall(scrap)
                        for url in source5:
                                fullname='Source #'+sourcenumber+' | [Full]'
                                if FlattenMega == 'true':
                                        VIDEOLINKS(fullname,url)
                                if FlattenMega == 'false':
                                        addDir(fullname,url,110,'')

                
def SOURCE(scrape):
#check for sources containing multiple parts or just one part
        PART(scrape,'1')
        PART(scrape,'2')
        PART(scrape,'3')
        PART(scrape,'4')
        PART(scrape,'5')
        PART(scrape,'6')
        PART(scrape,'7')
        PART(scrape,'8')
        PART(scrape,'9')
        PART(scrape,'10')
        PART(scrape,'11')
        PART(scrape,'12')
        PART(scrape,'13')
        PART(scrape,'14')
        PART(scrape,'15')
        PART(scrape,'16')

                
def DVDRip(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
#string for all text under standard def border
        defcat=re.compile('<div class=ripdiv><b>DVDRip / Standard Def</b>(.+?)</div>').findall(link)
        #hacky buffer
        outputone = StringIO.StringIO()
        outputone.write(defcat)
        defcat = outputone.getvalue()
        SOURCE(defcat)

def HD720p(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
#string for all text under hd720p border
        defcat=re.compile('<div class=ripdiv><b>HD 720p</b>(.+?)</div>').findall(link)
        #hacky buffer
        outputone = StringIO.StringIO()
        outputone.write(defcat)
        defcat = outputone.getvalue()
        SOURCE(defcat)


def DVDScreener(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
#string for all text under dvd screener border
        defcat=re.compile('<div class=ripdiv><b>DVD Screener</b>(.+?)<p></div>').findall(link)
        #hacky buffer
        outputone = StringIO.StringIO()
        outputone.write(defcat)
        defcat = outputone.getvalue()
        catdef = defcat+'<p></div>'
        SOURCE(catdef)

def R5R6(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
#string for all text under r5/r6 border
        defcat=re.compile('<div class=ripdiv><b>R5/R6 DVDRip</b>(.+?)<p></div>').findall(link)
        #hacky buffer
        outputone = StringIO.StringIO()
        outputone.write(defcat)
        defcat = outputone.getvalue()
        catdef = defcat+'<p></div>'        
        SOURCE(catdef)

def VIDEOLINKS(partname,url):
# loads megaupload page and scrapes and adds videolink, passes through partname.
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        avimatch=re.compile('id="downloadlink"><a href="(.+?).avi" class=').findall(link)
        for url in avimatch:
                fullurl=url+'.avi'                          
                addLink(partname,fullurl,'')
        #pretend to XBMC that divx is avi
        match1=re.compile('id="downloadlink"><a href="(.+?).divx" class=').findall(link)
        for surl in match1:
                sullurl=surl+'.avi'
                addLink(partname,sullurl,'')

def VIDEOLINKSWITHFILENAME(url):
# loads megaupload page and scrapes and adds videolink, and name of uploaded file from it
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        avimatch=re.compile('id="downloadlink"><a href="(.+?).avi" class=').findall(link)
        for url in avimatch:
                fullurl=url+'.avi'                          
                #get filname
                matchy=re.compile('id="downloadlink"><a href=".+?megaupload.com/files/.+?/(.+?).avi" class=').findall(link)
                for urlfilename in matchy:
                        addLink('VideoFile | '+urlfilename,fullurl,'')
        #pretend to XBMC that divx is avi
        match1=re.compile('id="downloadlink"><a href="(.+?).divx" class=').findall(link)
        for surl in match1:
                sullurl=surl+'.avi'
                #get filename
                matchy=re.compile('id="downloadlink"><a href=".+?megaupload.com/files/.+?/(.+?).divx" class=').findall(link)
                for urlfilename in matchy:
                        addLink('VideoFile | '+urlfilename,sullurl,'')
        

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()

elif mode==50:
        print ""+url
        TVCATEGORIES(url)

elif mode==51:
        print ""+url
        MOVIECATEGORIES(url)

elif mode==52:
        print ""+url
        MUSICCATEGORIES(url)

elif mode==53:
        print ""+url
        STANDUPCATEGORIES(url)

elif mode==54:
        print ""+url
        OTHERCATEGORIES(url)

elif mode==1:
        print ""+url
        MOVIEA2ZDirectories(url)

elif mode==3:
        print ""+url
        MOVIEA2ZList(url)

elif mode==2:
        print ""+url
        MOVIEINDEX(url)
        
elif mode==10:
        print ""+url
        TVA2ZDirectories(url)

elif mode==13:
        print ""+url
        TVA2ZList(url)

elif mode==11:
        print ""+url
        TVINDEX(url)

elif mode==12:
        print ""+url
        TVEPISODES(url)

elif mode==100:
        print ""+url
        LOADMIRRORS(url)

elif mode==101:
        print ""+url
        DVDRip(url)

elif mode==102:
        print ""+url
        HD720p(url)

elif mode==103:
        print ""+url
        DVDScreener(url)

elif mode==104:
        print ""+url
        R5R6(url)

elif mode==110:
        print ""+url
        VIDEOLINKSWITHFILENAME(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
