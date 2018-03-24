from setuptools import setup, find_packages

setup(
    name="datamule",
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pyyaml',
    ],
    entry_points='''
        [console_scripts]
        datamule=datamule.core.cli:main
    ''',
)