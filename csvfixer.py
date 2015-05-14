import csv, argparse

parser = argparse.ArgumentParser(description="Replaces unnecesary EOL characters in CSV files.")
parser.add_argument('input', type=str, help='name of input file')
parser.add_argument('output', type=str, help='name of output file')
parser.add_argument('-v', help="verbose-prints some useful information", action="store_true")
args = parser.parse_args()

error_counter = 0

with open(args.input) as csvfile:
    linereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    linewriter = csv.writer(file(args.output, "wb"))

    for line in linereader:
        for field_no in range(len(line)):
            if line[field_no].find("\n") > -1:
                line[field_no] = line[field_no].replace("\n", " ")
                error_counter += 1
        linewriter.writerow(line)
if args.v:
    print "Number of characters replaced: " + error_counter

