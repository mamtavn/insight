# insight

Insight Data Engineering Fellows Program - Coding Challenge

Contains 2 python scripts - word_count.py and running_median.py
Both are tested against Python2 and Python3

Both the scripts take 2 optional arguments - input directory and output directory.
If they are not specified wc_input and wc_output are assumed.
All the results are under the wc_output (or the output directory given) directory
Other than the FAQ, the scripts also assume that a word with no alphabet or number is a non-word. 
For e.g. >>> is not treated as a word. 

To run the scripts, type, run.sh from a unix shell
run.sh assumes that the python executable is available at /usr/bin/python
There are no external dependencies. All the imports are available in the standard python.
