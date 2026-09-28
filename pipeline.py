"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

def setup_logging(verbose = False):
    """Set up logging for the pipeline"""
    logging.basicConfig(level = logging.INFO,
                        format = "%(asctime)s %(levelname)-8s %(message)s",
                        datefmt = "%H:%M:%S")

    if verbose == True:
        logger.setLevel(logging.DEBUG)

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description = "")

    parser.add_argument("--input",
                        "-i",
                        required = True,
                        help = "Path to input file")

    parser.add_argument("--output",
                        "-o",
                        required = True,
                        help = "Path to output file")

    parser.add_argument("--format",
                        default = "csv",
                        help = "Output format: csv or json")

    parser.add_argument("--verbose",
                        "-v",
                        action = "store_true",
                        help = "Enable verbose logging")

    args = parser.parse_args()

    return args.input, args.output, args.format, args.verbose

def validate_input(filepath):
    """Check whether the input path exists and is a file"""
    if Path(filepath).is_file():
        logger.info(f"Input file validated: {filepath}")
        return True
    else:
        logger.error(f"Input file not found: {filepath}")
        return False

def main():
    """Main pipeline function"""
    # argument parser
    arguments = parse_arguments()
    arguments_input = arguments[0]
    arguments_output = arguments[1]
    arguments_format = arguments[2]
    arguments_verbose = arguments[3]

    # logging
    setup_logging(arguments_verbose)
    logger.debug(f"Arguments parsed: input = {arguments_input}, "
                 f"output = {arguments_output}, "
                 f"format = {arguments_format}, "
                 f"verbose = {arguments_verbose}")

    # validate input file
    input_valid = validate_input(arguments_input)
    if not input_valid:
        sys.exit(1)

if __name__ == "__main__":
    main()