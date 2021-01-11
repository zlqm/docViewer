import setuptools

with open('README.rst') as f:
    long_description = f.read()

setuptools.setup(
    name='docViewer',
    version='1.0.0',
    author='Abraham',
    author_email='abraham.liu@hotmail.com',
    description='document tool',
    install_requires=[
        'click',
        'p_config>=1.2.0',
        'docutils',
        'requests',
        'tornado',
    ],
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'scripts/renderDoc',
        'scripts/previewDoc',
    ],
)
