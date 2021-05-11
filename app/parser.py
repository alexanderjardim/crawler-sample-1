import argparse

APP_DESCRIPTION = "Downloads .png files from a given URL and saves files to OUTPUT dir. Supports optional HTTP Basic Auth"

def parse(args):
    parser =  argparse.ArgumentParser(description=APP_DESCRIPTION)
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("-l", "--login")
    parser.add_argument("-p", "--password")
    
    if len(args) < 2:
        parser.print_help()
    return vars(parser.parse_args(args))