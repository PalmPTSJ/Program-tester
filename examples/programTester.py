import threading, os, sys, argparse, time

exitFlag = 0
testcaseCounter = 1
threadLock = threading.Lock()
class testerThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print(self.name+" started.")
        while True  :
            if exitFlag :
                break
            newTestcase(self.name)

def newTestcase(name) :
    global testcaseCounter, exitFlag
    
    inputFileName = "tc/"+name+".in"
    outputFileName = "tc/"+name+".out"
    solFileName = "tc/"+name+".sol"
    checkerResultFileName = "tc/"+name+".checked"
    if(args.verbose) :
        print('%s > "%s"' % (args.testgen, inputFileName))
    os.system('%s > "%s"' % (args.testgen, inputFileName)) # create new testcase
    
    if(args.verbose) :
        print('%s < "%s" > "%s"' % (args.cor, inputFileName, solFileName))
    os.system('%s < "%s" > "%s"' % (args.cor, inputFileName, solFileName)) # run correct program
    
    if(args.verbose) :
        print('%s < "%s" > "%s"' % (args.wrong, inputFileName, outputFileName))
    os.system('%s < "%s" > "%s"' % (args.wrong, inputFileName, outputFileName)) # run target program
    
    if(args.verbose) :
        print('%s "%s" "%s" > "%s"' % (args.checker, outputFileName, solFileName, checkerResultFileName))
    os.system('%s "%s" "%s" > "%s"' % (args.checker, outputFileName, solFileName, checkerResultFileName)) # run checker program
    
    # read checker status
    f = open(checkerResultFileName,"r")
    checkerStatus = f.read().strip()
    f.close()

    threadLock.acquire()
    if exitFlag == 1 :
        threadLock.release()
        return
        
    if checkerStatus == "OK" :
        print("[%s] Testcase %d : OK" % (name,testcaseCounter))
    else :
        print("[%s] Testcase %d : NOT OK" % (name,testcaseCounter))
        exitFlag = 1
    testcaseCounter += 1
    threadLock.release()

parser = argparse.ArgumentParser()
parser.add_argument("cor"               , help="Command to run the correct program.")
parser.add_argument("wrong"             , help="Command to run the incorrect (target) program.")
parser.add_argument("testgen"           , help="Command to run the testcase generator.")
parser.add_argument("-c","--checker"    , help="Command to run the checker program (default is 'python default_checker.py').",default='python default_checker.py')
parser.add_argument("-t","--thread"     , help="Number of threads to run (default is 1).",type=int,default=1)
parser.add_argument("-v", "--verbose"   , help="Verbose commands used to run the tester.",action="store_true")
args = parser.parse_args()

print("Creating tc folder ...")
if not os.path.exists('tc'): os.makedirs('tc')


threadList = []
for i in range(args.thread) :
    threadName = "Thread-"+str(i+1)
    print("Creating thread "+threadName)
    thread = testerThread(1,threadName)
    thread.daemon = True
    thread.start()
    threadList.append(thread)

while exitFlag == 0 :
    time.sleep(0.1)

print("Counter testcase found. Press ENTER to exit the program")
input()
