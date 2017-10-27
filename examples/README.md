# Program-tester Example

- cor.py is the reference program.
- wrong.py is the target program to debug. The program is designed to produce wrong answer if the input is equal to 9.
- testcaseGen.py is the testcase generator (generates single integer in range 0-9)

programTester.py and default_checker.py is retrieved from the repository.

Run the script with following command : `programTester.py cor.py wrong.py testcaseGen.py`

If you want to use multiple threads, run the script with `-t THREAD_COUNT`. 
For example: `programTester.py cor.py wrong.py testcaseGen.py -t 4` will start program with 4 threads.
