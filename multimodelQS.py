"""
Purpose: This demo shows using relational and native access side-by-side in a Python application,
connecting to InterSystems IRIS.

To test: Run to see how to populate and retrieve data using PyODBC. Then uncomment the lines to execute storeAirfare and
checkAirfare to see how to create a custom data structure using the Native API.
"""


import pyodbc
import irisnative


# List of airports
AIRPORTS = [
    ("Boston Logan International", "BOS", "02128"),
    ("Philadelphia International", "PHL", "19153"),
    ("Austin-Bergstrom International", "AUS", "78719"),
    ("San Francisco International", "SFO", "94128"),
    ("Chicago O'hare International", "ORD", "60666")
]

# List of locations of the airports above
LOCATIONS = [
    ("02128", "Boston", "MA", '0', '0'),
    ("19153", "Philadelphia", "PA", '0', '0'),
    ("78719", "Austin", "TX", '0', '0'),
    ("94128", "San Francisco", "CA", '0', '0'),
    ("60666", "Chicago", "IL", '0', '0'),
] 


# Connect to InterSystems IRIS
def connect_to_iris():
    # Login credentials
    driver = "{InterSystems ODBC}"
    ip = "localhost"
    port = 51773
    namespace = "USER"
    username = "SuperUser"
    password = "SYS"

    # Connect to InterSystems IRIS using PyODBC
    connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}'\
        .format(driver, ip, port, namespace, username, password)
    pyodbc_connection = pyodbc.connect(connection_string)

    # Connect to InterSystems IRIS using the Native API
    nativeapi_connection = irisnative.createConnection(ip, port, namespace, username, password)

    print("Connected to InterSystem IRIS")
    return pyodbc_connection, nativeapi_connection


# Remove old table if exist
def delete_old_table(cursor, table_name):
    drop_table = "DROP TABLE {}".format(table_name)
    cursor.execute(drop_table)


# Populate airport tables in the InterSystems IRIS database
def populate_airports(connection):
    # Create cursor
    cursor = connection.cursor()

    # Create Demo.Location table in the InterSystems IRIS database
    create_locations = """
        CREATE TABLE Demo.Location(
            zip varchar(5) PRIMARY KEY, 
            city varchar(50), 
            state varchar(50),
            longitude varchar(50), 
            latitude varchar(50)
        )
    """
    try:
        cursor.execute(create_locations)
    except:
        delete_old_table(cursor, "Demo.Location")
        cursor.execute(create_locations)

    # Create Demo.Airport table in the InterSystems IRIS database
    create_airports = """
        CREATE TABLE Demo.Airport (
            name varchar(50) unique, 
            code varchar(3) PRIMARY KEY,
            location Demo.Location
          )
        """
    try:
        cursor.execute(create_airports)
    except:
        delete_old_table(cursor, "Demo.Airport")
        cursor.execute(create_airports)

    # Inset locations into Demo.Location table in the InterSystems IRIS database
    insert_locations = """
        Insert into Demo.Location
        (zip, city, state, longitude, latitude)
        VALUES (?, ?, ?, ?, ?)
    """
    for zip, city, state, longitude, latitude in LOCATIONS:
        cursor.execute(insert_locations, zip.encode('utf-8'), city.encode('utf-8'), state.encode('utf-8'),
                       longitude.encode('utf-8'), latitude.encode('utf-8'))

    # Inset airport into Demo.Airport table in the InterSystems IRIS database
    insert_airports = """
        Insert into Demo.Airport
        Select ?, ?, Demo.Location.id
        FROM Demo.Location 
        where Demo.Location.zip = ?
    """
    for name, code, zip in AIRPORTS:
        cursor.execute(insert_airports, name.encode('utf-8'), code.encode('utf-8'), zip.encode('utf-8'))

    connection.commit()


# Display all airports using PyODBC
def get_airports(connection):
    print("Name\t\t\t\tCode\tLocation")

    # Create a cursor
    cursor = connection.cursor()

    # This query uses a special shorthand notation (->, known as an implicit join)
    # to retrieve data from a related table without requiring you to think about how to join tables
    rows = cursor.execute("SELECT name, code, location->city, location->state, location->zip FROM Demo.Airport")

    # Display all airports
    for row in rows:
        print("{}\t{}\t{}, {} {}".format(row.name, row.code, row.city, row.state, row.zip))


# Create a custom data structure to store airport distance and airfare information in a graph-like structure.
def store_airfare(iris_native):
    stored_global = "^airport"
    # Store distance, routes, and airfares between airports
    iris_native.set("1698", stored_global, "BOS", "AUS")
    iris_native.set("450", stored_global, "BOS", "AUS", "AA150")
    iris_native.set("550", stored_global, "BOS", "AUS", "AA290")

    iris_native.set("280", stored_global, "BOS", "PHL")
    iris_native.set("200", stored_global, "BOS", "PHL", "UA110")

    iris_native.set("1490", stored_global, "BOS", "BIS")
    iris_native.set("700", stored_global, "BOS", "BIS", "AA330")
    iris_native.set("710", stored_global, "BOS", "BIS", "UA208")

    print("\nStored fare and distance data in {} global.".format(stored_global))


# Simple interactive method using IRIS native API to consult the data structure populated in storeAirfare()
def check_airfare(iris_native):
    stored_global = "^airport"
    # Prompt for input
    from_airport = input("Enter departure airport: (e.g. BOS)")
    to_airport = input("Enter destination airport: (e.g. AUS)")

    # ^airport(from, to) = distance
    print("\nPrinted to {} global. The distance in miles between {} and {} is {}."
          .format(stored_global, from_airport, to_airport, iris_native.getString("^airport", from_airport, to_airport)))

    # Now loop through routes: ^airport(from, to, flight) = fare
    is_defined = iris_native.isDefined(stored_global, from_airport, to_airport)
    if is_defined == 11 or is_defined == 1:
        print("The following routes exist for this path:")
        iterator = iris_native.iterator(stored_global, from_airport, to_airport)
        for flight_number, fare in iterator:
            print(" -{}: {} USD".format(flight_number, fare))
    else:
        print("No routes exist for this path.")


def run():
    # Get connections for PyODBC and the Native API
    pyodbc_connection, nativeapi_connection = connect_to_iris()

    # Populate and retrieve data using PyODBC
    populate_airports(pyodbc_connection)
    get_airports(pyodbc_connection)

    # Uncomment the following lines to store and retrieve data natively using the Native API
    # iris_native = irisnative.createIris(nativeapi_connection)
    # store_airfare(iris_native)
    # check_airfare(iris_native)


if __name__ == '__main__':
    run()
