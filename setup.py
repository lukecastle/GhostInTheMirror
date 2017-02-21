from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'Video_Looper',
      version           = '0.0.1,
      author            = 'Luke Castle
      author_email      = 'nuexlukecastle@outlook.com
      description       = 'Application to turn your Raspberry Pi into a dedicated looping video playback device, good for art installations, information displays, or just playing cat videos all day.',
      license           = 'GNU GPLv2',
      url               = 'https://github.com/lukecastle/GhostInTheMirror',
      install_requires  = ['pyudev'],
      packages          = find_packages())
