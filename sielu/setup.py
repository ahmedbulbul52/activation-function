from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='sielu',
    version='1.0.0',
    description='An activation function',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Bulbul Ahmed',
    author_email='ahmedbulbul52@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requires=['']
)