# !!! This uses the https://newsapi.org/ api. TO comply with the TOU
# !!! we must link back to this site whenever we display results.
try:  # python3
    import urllib.request
    import urllib.parse
    import urllib.error
except ImportError:  # python2
    import urllib
import json
import webbrowser
import six
from .memory.memory import Memory

'''
    CLASS News
    To run the full news class run:
        news_options
        THEN
        get_news
    For quick news run:
        request_news

    example:
    n = News()
    n.news()
    OR
    n = News()
    n.quick_news()
'''


class News:
    def __init__(self, source="google-news", api_key="7488ba8ff8dc43459d36f06e7141c9e5"):
        self.apiKey = api_key
        self.source = source
        self.url = "https://newsapi.org/v1/articles?source=google-news&sortBy=top" \
                   "&apiKey=7488ba8ff8dc43459d36f06e7141c9e5"
        self.m = Memory()
    '''
        This is the defualt news function. It checks to see if the
        user has a preference and and goes through all choices.
    '''

    def news(self):
        self.news_options()
        self.get_news()

    '''
        This is the quickest way to get news it also has the
        least amount of options for the user.
    '''

    def quick_news(self):
        self.request_news()

    '''
        Gets and returns JSON data of news
    '''

    def get_news_json(self):
        try:
            response = urllib.request.urlopen(self.url)
        except AttributeError:
            response = urllib.urlopen(self.url)
        return json.loads(response.read().decode('utf-8'))

    '''
        This sets the users options and loads them from Memory
        if they exist
    '''

    def news_options(self):
        # check to see if user already has default news source
        if self.m.get_data('news-source'):
            print("your default news source is " +
                  self.m.get_data('news-source'))
            print("Would you like news from this source? (yes/no): ")
            if six.PY2:
                x = raw_input()
            else:
                x = input()
            if x == 'y' or x == 'yes':
                self.source = self.m.get_data('news-source')
            # if not set get users preference
            else:
                self.get_opt()
        else:
            self.get_opt()

    def get_opt(self):
        branch = set()
        _get_opt(self, branch)
        with open('get_opt@news.py.branch', 'a') as branch_file:
            branch_file.write('total: %s\n' % str(10))
            branch_file.write('activated: %s\n' % str(len(branch)))
            branch_file.write('set: %s\n' % str(branch))
            branch_file.write('--------------\n')


    def _get_opt(self, branch):
        # Other sources available here: https://newsapi.org/sources
        print("Select Source (1-5):")
        print("1: BBC")
        print("2: BUZZFEED")
        print("3: Google")
        print("4: Reddit")
        print("5: TechCrunch")

        if six.PY2:
            branch.add(110)
            i = int(raw_input())
        else:
            branch.add(113)
            i = int(input())
        if i == 1:
            branch.add(116)
            self.source = "bbc-news"
        elif i == 2:
            branch.add(119)
            self.source = "buzzfeed"
        elif i == 3:
            branch.add(122)
            self.source = "google-news"
        elif i == 4:
            branch.add(125)
            self.source = "reddit-r-all"
        elif i == 5:
            branch.add(128)
            self.source = "techcrunch"

        print("would you like to set this as your default? (yes/no): ")
        if six.PY2:
            branch.add(133)
            x = raw_input()
        else:
            branch.add(136)
            x = input()
        if x == 'y' or x == 'yes':
            branch.add(139)
            self.m.update_data('news-source', self.source)  # save to memory
            self.m.save()

    '''
        This sets the url and sends it to request_news()
    '''

    def get_news(self):
        u = "https://newsapi.org/v1/articles?source=" + \
            self.source + "&sortby=top&apiKey=" + self.apiKey
        self.request_news(u)


    def request_news(self, url=None):
        branch = set()
        self._request_news(self, branch, url)
        with open('request_news@news.py.branch', 'a') as branch_file:
            branch_file.write('total: %s\n' % str(14))
            branch_file.write('activated: %s\n' % str(len(branch)))
            branch_file.write('set: %s\n' % str(branch))
            branch_file.write('--------------\n')

    '''
        This has all the logic to request and parse the json.
        This function DOES NOT check user preferences.
        It also includes user interactions for getting more info on an articles
    '''

    def _request_news(self, branch, url=None):
        # check to see if a url was passed
        if url is None:
            branch.add(151)
            url = self.url
        try:
            response = urllib.request.urlopen(url)
            branch.add(155)
        except AttributeError:
            branch.add(157)
            response = urllib.urlopen(url)
        # Load json
        data = json.loads(response.read())
        article_list = {}
        index = 1
        # print articles with their index
        print("Top News Articles from " + self.source)
        for article in data['articles']:
            branch.add(166)
            # print (Fore.GREEN + str(index) + ": " + article['title'] + Fore.RESET)
            print(str(index) + ": " + article['title'])
            article_list[index] = article
            index += 1

        # Attribution link for News API to comply with TOU
        print("Powered by News API. Type NewsAPI to learn more")
        print("Type index to expand news\n")

        # Check to see if index or NewsAPI was enterd
        if six.PY2:
            branch.add(178)
            idx = raw_input()
        else:
            branch.add(181)
            idx = input()
        if idx.lower() == "newsapi":
            branch.add(184)
            webbrowser.open('https://newsapi.org/')
            return

        # check if we have a valid index
        try:
            int(idx)
            if int(idx) > index:
                branch.add(192)
                print("Not a valid index")
                return
            branch.add(195)
        except:
            branch.add(197)
            print("Not a valid index")
            return

        # if index valid print article description
        print(article_list[int(idx)]['description'])

        print("Do you want to read more? (yes/no): ")
        if six.PY2:
            branch.add(206)
            i = raw_input()
        else:
            branch.add(209)
            i = input()
        # if user wants to read more open browser to article url
        if i.lower() == "yes" or i.lower() == 'y':
            branch.add(213)
            webbrowser.open(article_list[int(idx)]['url'])
            return
        else:
            branch.add(217)
            return
