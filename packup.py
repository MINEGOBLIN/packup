#!/usr/bin/python3

from pathlib import Path
from shutil import *
import argparse, sys, datetime

"""
You must specify the folder you want to backup and where you want the 
backup to be stored.
"""

parser = argparse.ArgumentParser(
    description=f'Backup script, specify the directory you want to archive and where to store it.',
    prog='Packup.py')
parser.add_argument('-s', '--src', required=True, help='Source path (Directory you want to zip and store.)')
parser.add_argument('-d', '--dest', required=True, help='Destination path (Directory where you want the zip stored.)')
args = parser.parse_args()

destination_zip_location = Path(args.dest)
source_directory = Path(args.src)
if source_directory.is_dir():
    print(f'{source_directory} verified, continuing with archiving.')
else:
    print(f'{source_directory} is not a valid source. You must specify a valid directory\nExiting!')
    sys.exit(0)
if destination_zip_location.is_dir():
    print(f'{destination_zip_location} verified, continuing with archiving.')
else:
    print(f'{destination_zip_location} is not a valid destination. You must specify a valid directory\nExiting!')
    sys.exit(0)

archives = list(destination_zip_location.glob('*.zip*'))
if len(archives) >= 3:
    oldest = min(archives, key=lambda a: a.stem)
    Path(oldest).unlink()

zip_name = f'{source_directory.name}-{datetime.date.today().strftime("%Y-%m-%d")}'
make_archive(str(destination_zip_location / zip_name), 'zip', source_directory)