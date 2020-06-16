from setuptools import setup, find_packages


readme = open("README.md", "r")
changes = open("CHANGELOG.txt", "r")
long_description = readme.read() + '\n\n' + changes.read()
readme.close()
changes.close()


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='polyencryption',
    version='0.0.9',
    description='a simple encryption algorithm that encrypts .txt files using a polyalphabetic cypher. NOTE- this software is not intended for nor should be used for any security purposes',
    long_description=long_description,
    url='https://github.com/skelegorg/polyencryption',
    author='Andrew C',
    author_email='cumminand@outlook.com',
    license='MIT',
    classifiers=classifiers,
    keywords='encryption',
    packages=find_packages(),
    install_requires=['secrets']
)
