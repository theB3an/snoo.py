from setuptools import setup, find_packages

setup(
    name='snoo.py',
    version='0.1',
    description='Tool for querying LDAP for msDS-MachineAccountQuota and SPNs',
    author='theB3an',
    url='https://github.com/your-repo/ldap-project',
    packages=find_packages(),
    install_requires=[
        'impacket',
    ],
    entry_points={
        'console_scripts': [
            'snoo.py=snoopy.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
