import platform
from waflib import Configure

Configure.autoconfig = True

top = '.'
default_prefix = '/usr'

if platform.system() == 'Windows':
    out = 'out/windows'
elif platform.system() == 'Linux':
    out = 'out/linux'

projects = ['Example1', 'Example2']
modes = ['debug', 'release']
