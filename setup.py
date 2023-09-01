from setuptools import setup, find_packages

setup(
    name='tagger_md',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tagger_md = tagger_md.tagger:main',
        ],
    },
)