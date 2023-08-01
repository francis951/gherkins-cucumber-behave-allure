# Behave - Reports
All the available formatters in Behave are displayed with the command −
## behave --format help

Some of the common Behave reports are −

    1. Allure Report.

    2. Output JSON Report.

    3. JUnit Report

# JUnit Report
## behave --junit 
A folder called as the reports gets generated within the project, having the name TESTS-<feature file name>.xml.
# Report generation to a specific folder then run:
## behave --junit --junit-directory my_reports

# JSON Report
## behave -f json or you can run: behave -f json.pretty
 Report generation to a specific folder then run:
 # behave –f json.pretty –o my_reports.json

 # Allure Report
 To generate Allure reports in Behave, first we have to install Allure in the system. For installation from the command line in Linux, run the following commands one after the other −
For Windows, Allure is installed manually and then check if java is installed.

### After Allure has been installed, we have to get the Allure-Behave integration plugin for Python. For this, run the following command −

# pip install allure-behave

#### verify if Allure has been installed successfully, run: allure --version

## Report generation to a specific folder
## behave -f allure_behave.formatter:AllureFormatter -o my_allure

## Start the web server
### allure serve my_allure
