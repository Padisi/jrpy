from setuptools import setup, find_packages

setup(
    name='jrpy',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy','pygame'],
    description='Hydrodynamics game',
    author='Pablo Diez Silva',
    author_email='pablodiezsilva@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
