import argparse, os

def arg_parser():
    msg = 'This script will read a roster CSV file and build teams with ideal size and age/gender distribution'

    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument('input', help='Input CSV file path')
    parser.add_argument('cutoff', help='The age cutoff date for the season formatted MM/DD/YYYY')
    parser.add_argument('-o', '--output', help='Output text file path')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"{args.input} is not a valid file path")
        raise SystemExit(1)
    
    output = args.output or 'roster.txt'

    return [args.input, args.cutoff, output]