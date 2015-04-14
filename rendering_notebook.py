#!/usr/bin/env python

import os,sys,time
import subprocess
 
try:
    from IPython.kernel import KernelManager
except ImportError:
    from IPython.zmq.blockingkernelmanager import BlockingKernelManager as KernelManager
 
from IPython.nbformat.current import reads, NotebookNode

from IPython.html.notebookapp import NotebookApp

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        path = os.path.join(os.getcwd(), 'mace')
        command = "mace/ppa/runppa"
    else:
        path = os.path.join(os.getcwd(), 'mace', sys.argv[1])
        command = sys.argv[1] + "/mace/ppa/runppa"
    sys.path.append(path)
    sys.path.append(os.path.join(os.getcwd(), 'mace'))
    #sys.path.append('C:/ShapeSpace/'+sys.argv[1]+'/')
    import ppa
    NotebookApp.extra_static_paths = [os.path.join(ppa.location(),'notebook_static_files')]
    NotebookApp.pylab = 'inline'
    #NotebookApp().launch_instance()
    _spkw = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #p = subprocess.Popen(["ipython", "notebook"], **_spkw)
    p = subprocess.Popen(["python", command, "--port=9010"], **_spkw)
    time.sleep(5)
    #subprocess.Popen(["casperjs","C:/ShapeSpace/IPythonNotebookTesting/rendering_notebook.js"])