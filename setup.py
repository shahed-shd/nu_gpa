from setuptools import setup, find_packages
import codecs
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='nu_gpa',
    version='1.0.1',
    description='A command line package to calculate GPA of semester results specially for professional courses like CSE, ECE, BBA etc. offered by National University, Bangladesh.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shahed-shd/nu_cse',
    author='Md. Shahedul Islam Shahed',
    author_email='shahed.shd777@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='gpa semester result nu nubd cse ece bba course education',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nu_gpa=nu_gpa:main',
        ],
    }
)


