# Doctest Function for Webapps
# Paul Gulley 2012 ANi

import doctest
import multiprocessing 

def testproc(file, queue): #Don't call this!
    results = doctest.testfile(file)
    if queue:
        queue.put(results)
        return 
    else:
        return results

def TimedTest(timeout, tile):
    queue = multiprocessing.Queue()
    docproc = multiprocessing.Process(target=testproc, args=(file, queue))
    docproc.start()
    docproc.join(timeout)
    if docproc.is_alive():
        docproc.terminate()
        return "Process Timeout after {0} seconds".format(timeout)
    else:
        results = queue.get()
        return results
