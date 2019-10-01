# Multi-Model QuickStart for Python Code Sample

This code shows multi-model access to InterSystems IRIS Data Platform in Python.

This sample is used in the [Multi-Model QuickStart](https://learning.intersystems.com/course/view.php?name=Multimodel). 
It shows relational, and native access from a Python application to InterSystems IRIS. 
Airport data is stored using objects, retrieved using SQL, and a custom data structure is created using the Native API 
to handle route information between airports.

## To run in InterSystems Learning Labs or Evaluator Edition (on AWS, GCP, or Azure)

1. In the integrated terminal, run the following lines to install the 
InterSystems IRIS driver for the Native API and PyODBC.
 
    * `cd /home/project/quickstarts-multimodel-python`
    * `pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl`  
    * `odbcinst -i -d -f pyodbc_wheel/odbcinst.ini`

2. Run multimodelQS.py  
    * `python multimodelQS.py `  

## To run locally

1. Clone the repo and open in your Python IDE.
2. [Install *pyodbc* locally in your computer.](https://github.com/intersystems/quickstarts-python/blob/master/pyodbc_install.md)
3. In `multimodelQS.py`, change username, password, IP, port and namespace to point to your instance of InterSystems IRIS
4. In the integrated terminal, navigate to the *quickstarts-multimodel-python* directory: `cd quickstarts-multimodel-python`
5. Install the InterSystems IRIS driver for the Native API

| Operating System | Command |
| -- | :--: |  
| Window | `pip install nativeAPI_wheel\irisnative-1.0.0-cp34.cp35.cp36.cp37-none-win_amd64.whl` |
| Mac | `pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl`  |
| Linux | `pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl`

6. Install the InterSystems IRIS driver for PyODBC

| Operating System | Command |
| -- | :--: |  
| Local instance | InterSystems IRIS PyODBC driver is installed. You can skip this step. |
| Windows | `pyodbc_wheel\ODBC-2018.1.1.635.0-win_x64.exe` |
| Linux | `odbcinst -i -d -f pyodbc_wheel/linux/odbcinst.ini` |
| Mac | `odbcinst -i -d -f pyodbc_wheel/mac/odbcinst.ini` |

**Note**: Due to the dash(`-`) being different in each operating system, you might need to retype the command if you encounter errors.

7. Run multimodelQS.py.  
    * `python multimodelQS.py `  

## Output

If all works correctly, you will see a list of airports output. 
Data is stored and retrieved using PyODBC (relationally).  

If you would like to see how to store data natively using Python:
1. Find and uncomment the following lines:  
`# store_airfare(iris_native, "^airport")`  
`# check_airfare(iris_native, "^airport")`   
2. Enter departure airport: **BOS**
3. Enter destination airport: **AUS**

The output should say:  
>Printed to ^airport global. The distance in miles between BOS and AUS is: 1698.  
>The following routes exist for this path:  
>  -AA150: 450 USD  
>  -AA290: 550 USD 

Other routes may be null.

## Keep Exploring

To continue with another Python example with InterSystems IRIS, see the [Python QuickStart](https://learning.intersystems.com/course/view.php?name=Python%20QS).
