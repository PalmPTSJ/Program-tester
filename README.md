# Program-tester
Search for bugs in your program by generating testcases and comparing with brute-force solution to find the counter example.

How to use
---
1. Prepare your files. Here are the files you needed
- Reference program (brute-force or known to be correct)
- Target program to debug
- Testcase generator
- [OPTIONAL] Checker program (default_checker.py can be used in most cases)

2. Run the program with following arguments `python programTester.py <correct> <wrong> <testgen>`

3. The program will start generating testcases and test them with your reference and target program. If the answer from those two programs differ (by checker), the program will terminate.

4. If counter testcase was found, the testcase will be located at `tc/<Thread Name>.in`.

Additional options
---
- To run program with multiple threads, use `-t THREAD_COUNT`
- To run program in debug mode (program will echo the command it used to run), use `-v`