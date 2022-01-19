from setuptools import setup

setup(
    name='testgear-importer-allure',
    version='1.0.0',
    description='Allure report importer for TestGear',
    long_description=open('README.md', "r").read(),
    long_description_content_type="text/markdown",
    url='https://pypi.org/project/testgear-importer-allure/',
    author='Pavel Butuzov',
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=['testgear_importer_allure'],
    package_data={'testgear_importer_allure': ['../connection_config.ini']},
    package_dir={'testgear_importer_allure': 'src'},
    install_requires=['testgear-api-client'],
    entry_points={'console_scripts': ['testgear = testgear_importer_allure.__main__:console_main']}
)
