''' Default checker Program
Accept 2 arguments from argv as [outputFileName] [solFileName]
Print 'OK' if output and sol are the same, 'WRONG ANSWER' otherwise.

Default checker : Check only strings (stripped string line by line)
'''

import sys
if len(sys.argv) < 3 :
    print("Please supplied [outputFileName] [solFileName] as parameters.")
    exit(1)
outputFileName = sys.argv[1]
solFileName = sys.argv[2]

with open(outputFileName) as file:
    output = ' '.join([x.strip() for x in file.readlines()])

with open(solFileName) as file:
    sol = ' '.join([x.strip() for x in file.readlines()])

if output == sol : print("OK")
else : print("WRONG ANSWER")