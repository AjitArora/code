import os
import time
import threading
from Algorithm import GlobalFCFS
from Algorithm import StagewiseFCFS
from Algorithm import Random
import Params


processing_time = []
processed_applications_count = []
for i in xrange(0, Params.SIMULATION_COUNT):
	FCFS = GlobalFCFS(Params.APPLICANTS_COUNT)
	time.sleep(Params.SIMULATION_DURATION)
	ptime, count = FCFS.get_avg_processing_time_and_applications()
	processing_time.append(ptime)
	processed_applications_count.append(count)

print "For global FCFS Algo:"
print "Avg processing time: %s seconds"%(sum(processing_time)*1.0/len(processing_time))
print "Avg processed application: %s \n"%(sum(processed_applications_count)*1.0/len(processed_applications_count))

processing_time = []
processed_applications_count = []
for i in xrange(0, Params.SIMULATION_COUNT):
	sFCFS = StagewiseFCFS(Params.APPLICANTS_COUNT)
	time.sleep(Params.SIMULATION_DURATION)
	ptime, count = sFCFS.get_avg_processing_time_and_applications()
	processing_time.append(ptime)
	processed_applications_count.append(count)

print "For Stagewise FCFS Algo:"
print "Avg processing time: %s seconds"%(sum(processing_time)*1.0/len(processing_time))
print "Avg processed application: %s \n"%(sum(processed_applications_count)*1.0/len(processed_applications_count))

processing_time = []
processed_applications_count = []
for i in xrange(0, Params.SIMULATION_COUNT):
	random = Random(Params.APPLICANTS_COUNT)
	time.sleep(Params.SIMULATION_DURATION)
	ptime, count = random.get_avg_processing_time_and_applications()
	processing_time.append(ptime)
	processed_applications_count.append(count)

print "For Random Algo:"
print "Avg processing time: %s seconds"%(sum(processing_time)*1.0/len(processing_time))
print "Avg processed application: %s"%(sum(processed_applications_count)*1.0/len(processed_applications_count))

os._exit(1)
