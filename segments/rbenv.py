import subprocess
import os
import os.path


def add_rbenv_segment():
    home = os.getenv('HOME')
    if os.path.isdir(home + '/.rbenv'):
        rvm_prompt = \
            subprocess.Popen(
                ['rbenv', 'version'],
                stdout=subprocess.PIPE
                ).communicate()[0].strip().split(' ')[0]
        if rvm_prompt:
            powerline.append('%s ' % rvm_prompt, Color.JOBS_FG, Color.JOBS_BG)

add_rbenv_segment()
