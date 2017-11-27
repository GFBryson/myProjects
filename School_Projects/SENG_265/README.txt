SENG 256 Assignment 4 -Testing Data README

This zip file contains 3 separate test input files (to read from stdin) and corresponding expected output.  The input files, in*.html, contain various HTML tables.  Their corresponding out*.txt files have the expected output  

To run the tests use the following command :
python3 converter.py < in1.html > your_out1.txt

You can then compare the expect output with your output using diff, using the following command:
diff your_out1.txt out1.txt