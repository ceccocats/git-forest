import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='git-forest',  
     version='0.1',
     scripts=['git-forest'] ,
     author="Francesco Gatti",
     author_email="gattifrancesco@hotmail.it",
     description="manage subtree",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ceccocats/git-forest",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
          'argcomplete', 'argparse', 'pyyaml'
     ]
 )