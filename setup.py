from setuptools import setup, find_packages

setup(
    name='c2dn',
    version='0.1.0',
    author='Alex Doe',
    author_email='alex@doe.sh',
    packages=find_packages(),
    url='https://github.com/alexdoesh/c2dn',
    description='Clip2Net Downloader',
    long_description='Clip2Net Downloader',
    install_requires=[
        'requests==2.28.2',
        'lxml==4.9.2',
        'tqdm==4.64.1',
    ],
    entry_points={
        'console_scripts': [
            'c2dn=c2dn.cli:main',
        ],
    },
)
