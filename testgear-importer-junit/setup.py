from setuptools import setup

setup(
    name='testgear-importer-junit',
    version='1.2.4',
    description='Junit report importer for Test Gear',
    long_description=open('README.md', "r").read(),
    long_description_content_type="text/markdown",
    url='https://pypi.org/project/testgear-importer-junit/',
    author='Integration team',
    author_email='integrations@test-gear.io',
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=['testgear_importer_junit'],
    package_data={'testgear_importer_junit': ['../connection_config.ini']},
    package_dir={'testgear_importer_junit': 'src'},
    install_requires=['testgear-api-client>=2,<3'],
    entry_points={
        'console_scripts': [
            'testgear-junit = testgear_importer_junit.__main__:console_main'
        ]
    }
)
