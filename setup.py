import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dwdpollen',
    version='0.1.0',
    author='Max Rosin',
    author_email='git@hackrid.de',
    description='API client for the "Deutscher Wetterdienst" to get the current pollen load in Germany',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ekeih/dwdpollen',
    packages=['dwdpollen'],
    install_requires=['requests', 'pytz'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
)
