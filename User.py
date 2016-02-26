from Functions import *
import time

starttime = time.time()

userList = []

crawled = set()

animeSet = loadSet('./animelist.txt')
(crawled, userList) = load('./userlist.txt')

while True:
    page = urllib2.urlopen('http://myanimelist.net/users.php').read()
    soup = BeautifulSoup(page);

    for link in soup.find_all('a'):
        if link.get('href').startswith('/profile/'):
            user = link.get('href').split('/')[2]
            if not user in crawled:
                cnt = getCount(user, animeSet)
                if cnt >= 100:
                    append('./userlist.txt', user)
                    userList += [user]
                crawled.add(user)
                print str(cnt) + " " + user
    print "\nRefresh\n"