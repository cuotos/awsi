from setuptools import setup

setup(name='awsi',
      version='0.1',
      description='AWSI',
      url='http://gitlab.com/cuotos/awsi',
      author='Dan Potepa',
      author_email='dan@danpotepa.co.uk',
      license='wtfpl',
      packages=['awsi'],
      install_requires=[
            'boto'
      ],
      scripts=['bin/awsi'],
      zip_safe=False
)
