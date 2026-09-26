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

def setup_loggin(verbose = False):
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

def main():
    """Main pipeline function"""

if __name__ == "__main__":
    main()