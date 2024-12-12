from setuptools import setup, find_packages

setup(
    name='competence-scoring-calculator',
    version='1',
    packages=find_packages(),
    description='a package used for calculating competence scores of employees',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mugabi Praise',
    author_email='mugabipraise4@gmail.com',
    url='https://github.com/MUGABI-PRAISE/competence-scoring-calculator.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
