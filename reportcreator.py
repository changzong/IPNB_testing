import sys
import os
import time
import subprocess

time_stamp = '%4d%02d%02d%02d%02d%02d' % time.localtime()[0:6]
reportfile = 'report_' + time_stamp + '.html'
print reportfile
print sys.argv[0]
subprocess.Popen('runipy ' + sys.argv[1] + ' --html ' + '../../../IPythonNotebookTesting/report/' + reportfile)
quit()