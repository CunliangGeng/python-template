import os
import sys

# To update the package version number, edit CITATION.cff
citationfile = os.path.join(sys.exec_prefix, 'citation/{{ cookiecutter.repo_name }}', 'CITATION.cff')
with open(citationfile, 'r') as cff:
    for line in cff:
        if 'version:' in line:
            __version__ = line.replace('version:', '').strip().strip('"')
