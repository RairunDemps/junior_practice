from urllib.request import urlopen
from urllib.parse import urlparse, urlunparse
from urllib import robotparser

request_url = urlopen('https://www.geeksforgeeks.org/')
# print(request_url.read()) # big to print in console

parse_url = urlparse('https://www.geeksforgeeks.org / python-langtons-ant')
print(parse_url, end='\n')
unparse_url = urlunparse(parse_url)
print(unparse_url)

# trying to read the URL but with no internet connectivity
# try:
#     x = urlopen('https://www.google.com')
#     print(x.read())
# except Exception as e:
#     print(str(e))

# trying to read the URL and get HTTP Error
try:
    x = urlopen('https://www.google.com / search?q = test')
    print(x.read())
except Exception as e :
    print(str(e))

bot = robotparser.RobotFileParser()
x = bot.set_url('https://www.geeksforgeeks.org/robot.txt')
print("Where is robot.txt in geeksforgeeks.org", x)

y = bot.read()
print("Reads the files", y)

site_url = 'https://www.geeksforgeeks.org/'
z = bot.can_fetch('*', site_url)
print("We can crawl the main site ", site_url, z)

site_url = 'https://www.geeksforgeeks.org/wp-admin/'
w = bot.can_fetch('*', site_url)
print("We can crawl the main site ", site_url, w)
