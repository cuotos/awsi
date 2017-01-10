from setuptools import setup

setup(name='awsi',
      version='1.1',
      description='AWSI',
      url='http://gitlab.com/cuotos/awsi',
      author='Dan Potepa',
      author_email='dan@danpotepa.co.uk',
      license='wtfpl',
      packages=['awsi'],
      install_requires=[
            'boto'
      ],
      entry_points = {
            'console_scripts': ['awsi=awsi.awsi:main'],
      },
      zip_safe=False
)
