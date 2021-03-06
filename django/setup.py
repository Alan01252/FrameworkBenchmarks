import subprocess
import sys
import setup_util
import os

def start(args):
  setup_util.replace_text("django/hello/hello/settings.py", "HOST': '.*'", "HOST': '" + args.database_host + "'")
  subprocess.Popen("gunicorn hello.wsgi:application -k gevent  -b 0.0.0.0:8080 -w " + str((args.max_threads * 2)) + " --log-level=critical", shell=True, cwd="django/hello")
  return 0
def stop():
  p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
  out, err = p.communicate()
  for line in out.splitlines():
    if 'gunicorn' in line:
      try:
        pid = int(line.split(None, 2)[1])
        os.kill(pid, 9)
      except OSError:
        pass

  return 0
