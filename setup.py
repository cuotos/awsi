from setuptools import setup

def readme():
  with open("README") as f:
    return f.read()

setup(name='awsi',
      version='1.3.2',
      description='AWS EC2 information and connection tool',
      long_description=readme(),
      url='http://gitlab.com/cuotos/awsi',
      author='Dan Potepa',
      author_email='dan@danpotepa.co.uk',
      license='wtfpl',
      packages=['awsi'],
      classifiers=[
            'Programming Language :: Python :: 2.7',
            'Topic :: Utilities'
      ],
      install_requires=[
            'boto'
      ],
      entry_points = {
            'console_scripts': ['awsi=awsi.awsi:main'],
      },
      zip_safe=False
)
