from setuptools import setup, find_packages

setup(
    name='plotfree',
    version='0.1',
    description="A tool for badly monitoring memory usage",
    long_description=open('README.md').read(),
    author='Dominic Rodger',
    author_email='internet@dominicrodger.com',
    url='http://github.com/dominicrodger/plotfree',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    scripts=['plotfree/bin/plotfree-update.py', ],
    install_requires=[
        "psutil==0.7.0",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
    ],
    test_suite='plotfree.tests',
)
