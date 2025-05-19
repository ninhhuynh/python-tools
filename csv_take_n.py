import csv
import argparse

def take_n_records_from_csv(input_file, output_file, n=5, delimiter=','):
    with open(input_file, newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=delimiter)
        writer = csv.writer(outfile, delimiter=delimiter)
        for i, row in enumerate(reader):
            if i >= (n+1):
                break
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description="Take N records from a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output CSV file")
    parser.add_argument("-n", type=int, default=5, help="Number of records to take (default: 5)")
    parser.add_argument("-d", "--delimiter", default='|', help="CSV delimiter (default: '|')")
    args = parser.parse_args()

    take_n_records_from_csv(args.input_file, args.output_file, args.n, args.delimiter)

if __name__ == "__main__":
    main()