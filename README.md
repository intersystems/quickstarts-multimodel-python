# quickstarts-multimodel-python

## In this repository
.  
├── LICENSE  
├── multimodelQS.py  
└── README.md  

## Guided tutorial
For a guided tutorial using this sample, visit [Accessing Data in Python Using Multiple Data Models](https://learning.intersystems.com/course/view.php?name=PythonMultiModel) on the InterSystems learning site. 

## How to use this sample on your own
This code shows relational, and native access from a Python application to InterSystems IRIS. Airport data is stored using objects, retrieved using SQL, and a custom data structure is created using the Native API to handle route information between airports.

1. Start with an installation of Python and a running instance of InterSystems IRIS.
2. Download the Python DB-API driver for your system from the [InterSystems Drivers Download page](https://intersystems-community.github.io/iris-driver-distribution/)
3. Place the driver in your InterSystems IRIS installation directory according to the [Connection Your Application documentation page](https://docs.intersystems.com/components/csp/docbook/DocBook.UI.Page.cls?KEY=ADRIVE#ADRIVE_python)
4. Clone this repository and open it in your preferred IDE.
5. Edit multimodelQS.py. Update the connection information on lines 36-41 with information about your InterSystems IRIS server so that a connection can be established.
6. Run multimodelQS.py. If all works correctly, you will see a list of airports output. 
7. If you would like to see how to store data using globals in Python:
    1. find and uncomment the following lines:  
    ```
    # store_airfare(iris_native, "^airport")  
    # check_airfare(iris_native, "^airport")  
    ```
    2. Run the script again.
    3. Enter departure airport: **BOS**  
    4. Enter destination airport: **AUS**  
    The output should say:  
        >Printed to ^airport global. The distance in miles between BOS and AUS is: 1698.  
        >The following routes exist for this path:  
        >  -AA150: 450 USD  
        >  -AA290: 550 USD  
    
        Other routes may be null.