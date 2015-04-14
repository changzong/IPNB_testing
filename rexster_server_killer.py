import sys
import os

if __name__ == '__main__':
    PATH = os.path.join(sys.argv[1], 'rexster.xml')
    import psutil
    for proc in psutil.process_iter():
        proc_dict = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
        if proc_dict['name'] is not None and proc_dict['name'].lower() == 'java.exe':
            string = PATH.lower()
            for item in proc_dict['cmdline']:
                if item.lower().strip() == string:
                    os.kill(proc_dict['pid'], 9)
                    