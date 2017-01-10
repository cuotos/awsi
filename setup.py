from setuptools import setup

def readme():
  with open("README.md") as f:
    return f.read()

setup(name='awsi',
      version='1.1',
      description='Amazon Web Services information and connection tool',
      long_description=readme(),
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
