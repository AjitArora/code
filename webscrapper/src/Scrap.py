import threading
import Queue
import urllib2
import re
import os
from BeautifulSoup import BeautifulSoup
import time
import gevent
from gevent import Greenlet

def algo(url):
	try:
		#t = time.time()
		page = urllib2.urlopen(url).read()
		#print time.time()-t
	except Exception, fault:
		print "Error in urlopen for url: %s, error: %s"%(url, str(fault))
		return
	#soup = BeautifulSoup(page)
	#print soup.body.findAll(text=re.compile('^Exception$'))
	results = re.findall('(jquery.js)',page)
	if results:
		with open("accepted.csv", "a+") as myfile:
			myfile.write(url+"\n")
	else:
		with open("rejected.csv", "a+") as myfile:
			myfile.write(url+"\n")

class MyGreenlet(Greenlet):
	def __init__(self, gid, queue):
		Greenlet.__init__(self)
		self.queue = queue
		self.gid = gid

	def _run(self):
		url = self.queue.get()
		if url:
			algo(url)

class Worker(threading.Thread):
	def __init__(self, wid, queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.wid = wid
		self.greenlets_count = 32

	def run(self):
		greenlets = []
		gid = 0
		for x in xrange(0, self.greenlets_count):
			g = MyGreenlet(gid, self.queue)
			g.start()
			greenlets.append(g)
			gid+=1
		for greenlet in greenlets:
			greenlet.join()

	def get_greenlet_count(self):
		return self.greenlets_count

def read_input(file='seed_urls.txt'):
    with open(file) as f:
        for line in f:
            if len(line) > 0 and line != "\n":
                yield line.strip()
            else:
                return

def delete_output_files():
	try:
		os.remove("accepted.csv")
	except:
		pass
	try:
		os.remove("rejected.csv")
	except:
		pass

if __name__ == '__main__':
	delete_output_files()
	threads_count = 256
	threads = []
	i = 0
	q = Queue.Queue()
	greenlets_count = 0

	old_time = time.time()
	for x in range(0, threads_count):
		w = Worker(i, q)
		i+=1
		w.start()
		greenlets_count += w.get_greenlet_count()
		threads.append(w)
	for url in read_input():
		q.put(url)
	
	# Join
	for x in xrange(0, greenlets_count):
		q.put(None)
	for t in threads:
		t.join()
	print "total time taken: " + str(time.time()-old_time)