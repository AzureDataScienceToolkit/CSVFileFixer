import csv, argparse

parser = argparse.ArgumentParser(description="Removes or replaces unnecesary EOL characters in CSV files.")
parser.add_argument('input', type=str, help='name of input file')
parser.add_argument('output', type=str, help='name of output file')
parser.add_argument('--replace', type=str, default=" ", help="character to replace EOL with (default \' \')")
parser.add_argument('--delimiter', type=str, default=",", help='delimiter (default \',\')')
parser.add_argument('--quote', type=str, default='"', help='quote character (default \'"\')')
parser.add_argument('-v', help="verbose-prints some useful information", action="store_true")
args = parser.parse_args()

error_counter = 0

with open(args.input) as csvfile:
    if args.delimiter == "\\t": args.delimiter = "\t"
    linereader = csv.reader(csvfile, delimiter=args.delimiter, quotechar=args.quote)
    if args.output:
        linewriter = csv.writer(file(args.output, "wb"), delimiter=args.delimiter, quotechar=args.quote)
    else:
        linewriter = None

    for line in linereader:
        for field_no in range(len(line)):
            if line[field_no].find("\n") > -1:
                line[field_no] = line[field_no].replace("\n", args.replace)
                error_counter += 1
        linewriter.writerow(line)

if args.v:
    print "Job done. Number of characters fixed: " + str(error_counter)

