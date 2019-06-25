# Multi-Model QuickStart for Python Code Sample

This code shows multi-model access to InterSystems IRIS Data Platform in Python.

This sample is used in the [Multi-Model QuickStart](https://learning.intersystems.com/course/view.php?name=Multimodel). 
It shows relational, and native access from a Python application to InterSystems IRIS. 
Airport data is stored using objects, retrieved using SQL, and a custom data structure is created using the Native API 
to handle route information between airports.

## Run the Sample

1. In the integrated terminal, run the following lines to install the 
InterSystems IRIS driver for the Native API and PyODBC.
 
    * `cd /home/project/quickstarts-multimodel-python`
    * `pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl`  
    * `odbcinst -i -d -f pyodbc_wheel/odbcinst.ini`

2. Run multimodelQS.py  
    `python multimodelQS.py `  

## Output

If all works correctly, you will see a list of airports output. 
Data is stored and retrieved using PyODBC (relationally).  

If you would like to see how to store data natively using Python:
1. Find and uncomment the following lines:  
`# iris_native = irisnative.createIris(nativeapi_connection)`  
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
