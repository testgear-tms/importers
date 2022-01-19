# TestGear TMS importers
![TestGear](https://raw.githubusercontent.com/testgear-tms/importers/main/images/banner.png)

# Allure report

## Getting Started

### Installation
```
pip install testgear-importer-allure
```

## Usage

### API client

To use importer you need to install `testgear-api-client`:
```
pip install testgear-api-client
```

### Configuration

Use the command `testgear --help` to view the configuration setup help:
```
testgear --url https://{DOMAIN} - location of the TestGear instance
testgear --privatetoken T2lKd2pLZGI4WHRhaVZUejNl
    1. go to the https://{DOMAIN}/user-profile profile
    2. copy the API secret key
testgear --projectid 5236eb3f-7c05-46f9-a609-dc0278896464
    1. create a project
    2. open DevTools -> network
    3. go to the project https://{DOMAIN}/projects/20/tests
    4. GET-request project, Preview tab, copy id field
testgear --configurationid 15dbb164-c1aa-4cbf-830c-8c01ae14f4fb
    1. create a project
    2. open DevTools -> network
    3. go to the project https://{DOMAIN}/projects/20/tests
    4. GET-request configurations, Preview tab, copy id field
```

### Importing

Use the command `testgear --resultsdir allure-results` to specify the directory with Allure report results.  
**Important:** This command initiates the import.

# Contributing

You can help to develop the project. Any contributions are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/testgear-tms/importers/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/testgear-tms/importers/blob/master/CODE_OF_CONDUCT.md) before posting your first idea as well.

# License

Distributed under the Apache-2.0 License. See [LICENSE](https://github.com/testgear-tms/importers/blob/master/LICENSE.md) for more information.

