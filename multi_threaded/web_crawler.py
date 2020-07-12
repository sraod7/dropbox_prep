class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """
       return  []

import collections
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List


class Solution:
    def crawl(self, startUrl: str, htmlParser: HtmlParser) -> List[str]:
        queue = collections.deque()
        queue.append(startUrl)
        seen = {startUrl}
        domain = startUrl.split('http://')[1].split('/')[0]
        lock = threading.Lock()
        pool = ThreadPoolExecutor(max_workers=100)

        def helper(url_):
            lock.acquire()
            for url in htmlParser.getUrls(url_):
                if url not in seen and domain == url.split('http://')[1].split('/')[0]:
                    queue.append(url)
                    seen.add(url)
            lock.release()

        while queue:
            workers = []
            while queue:
                url = queue.popleft()
                workers.append(pool.submit(helper, (url)))

            for thread in workers:
                thread.result()

        pool.shutdown()

        return list(seen)