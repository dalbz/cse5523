import json
import urllib2
import sys
from time import sleep

if (sys.argv[1] == 'artists'):

    data = json.load(urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&limit=' + sys.argv[2] + '&api_key=56b26f4bbdd972b4460ca2ab0b53e63a&format=json'))

    f = open('data/artistList.txt', 'w')

    for artist in data['artists']['artist']:
        
        name = (artist['name'] + '\n').encode('UTF-8')
        
        f.write(name)

    f.close()

    print 'Artist list pulled'

if (sys.argv[1] == 'tags'):

    lines = [line.strip() for line in open('data/artistList.txt')]

    f1 = open('data/tagStrings.txt', 'w')
    f2 = open('data/tagCounts.txt', 'w')

    for line in lines:
        if (line != ''):

            sleep(0.5)

            print line

            htmlsafe = urllib2.quote(line, '')
            data = json.load(urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=' + htmlsafe + '&api_key=56b26f4bbdd972b4460ca2ab0b53e63a&format=json'))     

            for tag in data['toptags']['tag']:
                
                f1.write((tag['name'] + ',').encode('UTF-8'))
                f2.write((tag['count'] + ',').encode('UTF-8'))

            f1.write('\n')
            f2.write('\n')

    f1.close() 
    f2.close() 

    print 'Tag data pulled'

if (sys.argv[1] == 'classify'):

    artists = [line.strip() for line in open('data/artistList.txt')]

    f = open('data/classification.txt', 'w')

    for artist in artists:

        print artist
        q = raw_input()

        if (q == 'y'):
            f.write('1\n')
        else:
            f.write('-1\n')

    f.close()
