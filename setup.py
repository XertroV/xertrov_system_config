#!/usr/bin/python3

import os.path
import shutil
import argparse

BASHRC = os.path.expanduser("~/.bashrc")
XERTROVRC = os.path.expanduser("~/.xertrovrc")
DEFAULT_XERTROVRC = 'default_xertrovrc'
BASHRC_LINE = "source %s\n" % XERTROVRC

# setup parser
parser = argparse.ArgumentParser(description='xertrovrc installer')
parser.add_argument('--reinstall', help='reinstall xertrovrc', action='store_true')
# collect args
args = parser.parse_args()

def copy_xertrovrc():
  shutil.copyfile(DEFAULT_XERTROVRC, XERTROVRC)

def is_installed():
  with open(BASHRC, 'r') as f:
    if BASHRC_LINE not in f:
      return False
    return True

def install():
  with open(BASHRC, 'a') as f:
    f.write(BASHRC_LINE)
    
def main():
  if not is_installed() or args.reinstall:
    install()
    copy_xertrovrc()

if __name__ == "__main__":
  main()
