# EOLFixer
Simple Python script that either removes or replaces EOL characters that may appear in CSV files.

##Script syntax
<code>
eolfixer.py [-h] [--replace REPLACE] [--delimiter DELIMITER] 
 [--quote QUOTE] [-v] input output                                     
                                                                    
Removes or replaces unnecesary EOL characters in CSV files.         
                                                                    
    positional arguments:                                               
        input                   name of input file                          
        output                  name of output file                         
                                                                    
    optional arguments:                                                 
         -h, --help             show this help message and exit             
        --replace REPLACE       character to replace EOL with (default ' ') 
        --delimiter DELIMITER   delimiter (default ',')                     
        --quote QUOTE           quote character (default '"')               
         -v                     verbose-prints some useful information      
</code>

##Basic usage examples

###Replacing EOLs with spaces in simple CSV files
<code>
eolfixer.py inputfile.csv outputfile.csv
</code>
###Replacing EOLs with spaces in TSV files
<code>
eolfixer.py inputfile.csv outputfile.csv --delimiter '\t'
</code>