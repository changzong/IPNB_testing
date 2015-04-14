import fnmatch
import os
import subprocess
import sys
import glob

if __name__ == '__main__':
    searchpath = sys.argv[1]
    outputpath = sys.argv[2] + '\\jshintreport'
    #rcpath = outputpath + '\\pylintrc'
    for f in glob.glob(outputpath + "\\*.html"):
        os.remove(f)
    for root, dirnames, filenames in os.walk(searchpath):
        for filename in fnmatch.filter(filenames, '*.js'):
            filepath = os.path.join(root, filename)
            resultpath = os.path.join(outputpath, filename) + ".html"
            result = open(resultpath, "w")
            p = subprocess.Popen(["jshint", filepath], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.write(p.communicate()[0].encode('utf-8')) #encoding report content as unicode to avoid error from python(default is ascii)
            result.flush();