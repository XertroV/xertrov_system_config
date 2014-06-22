#!/usr/bin/python3

import os
import stat
import shutil
import argparse

BASHRC = os.path.expanduser("~/.bashrc")
XERTROVRC = os.path.expanduser("~/.xertrovrc")
BASH_LOGOUT = os.path.expanduser("~/.bash_logout")
DEFAULT_XERTROVRC = 'default_xertrovrc'
XERTROV_LOGOUT = os.path.expanduser("~/.xertrov_logout")
DEFAULT_LOGOUT = 'xertrov_logout.sh'
BASHRC_LINE = "source %s\n" % XERTROVRC
LOGOUT_LINE = "bash ~/.xertrov_logout\n"
BASH_LOGOUT = os.path.expanduser("~/.bash_logout")

# setup parser
parser = argparse.ArgumentParser(description='xertrovrc installer')
parser.add_argument('--reinstall', help='reinstall xertrovrc', action='store_true')
# collect args
args = parser.parse_args()

def set_file_executable(filename):
  current_permissions = os.stat(filename)
  os.chmod(filename, current_permissions.st_mode | stat.S_IEXEC)

def copy_file(source, destination):
  shutil.copyfile(source, destination)

def copy_xertrovrc():
  copy_file(DEFAULT_XERTROVRC, XERTROVRC)

def is_installed():
  return contents_in_file(BASHRC_LINE, BASHRC)
    
def contents_in_file(target_line, filename):
  with open(filename, 'r') as f:
    if target_line in f:
      return True
    return False

def add_line_to_file(line, filename):
  with open(filename, 'a') as f:
    f.write(line)
    
def add_line_if_absent(line, filename):
  if not contents_in_file(line, filename):
    add_line_to_file(line, filename)

def install():
  add_line_if_absent(BASHRC_LINE, BASHRC)
  copy_xertrovrc()
    
def install_logout():
  add_line_if_absent(LOGOUT_LINE, BASH_LOGOUT)
  copy_file(DEFAULT_LOGOUT, XERTROV_LOGOUT)
    
    
def main():
  if not is_installed() or args.reinstall:
    install()
    install_logout()

if __name__ == "__main__":
  main()
