import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# Create Staff table
query = """
    CREATE TABLE Staff(
    staffNo int64,
    staffName object,
    staffAddress object,
    staffPhone int64,
    staffDateOfBirth object,
    position object,
    salary float64,
    clinicNo int64,
    PRIMARY KEY(staffNo),
    FOREIGN KEY(clinicNo) REFERENCES Clinic(clinicNo)
    );
    """

# Execute query, the result is stored in cursor
#cursor.execute(query)

# Create Clinic table
query = """
    CREATE TABLE Clinic(
    clinicNo int64,
    clinicName object,
    clinicAddress object,
    clinicPhone int64,
    staffNo int64,
    PRIMARY KEY(clinicNo),
    FOREIGN KEY(staffNo) REFERENCES Staff(staffNo)
    );
    """
    
#cursor.execute(query)

# Create Pet table
query = """
        CREATE TABLE Pet(
        petNo int64,
        petName object,
        petDateOfBirth object,
        species object,
        breed object,
        color object,
        ownerNo int64,
        clinicNo int64,
        PRIMARY KEY(petNo),
        FOREIGN KEY(ownerNo) REFERENCES Owner(ownerNo),
        FOREIGN KEY(clinicNo) REFERENCES Clinic(clinicNo)   
        );
        """

#cursor.execute(query)

# Create Owner table
query = """
        CREATE TABLE Owner(
        ownerNo int64,
        ownerName object,
        ownerAddress object,
        ownerPhone int64,
        PRIMARY KEY(ownerNo)   
        );
        """

#cursor.execute(query)

# Create Exam table
query = """
        CREATE TABLE Exam(
        examNo int64,
        complaint object,
        description object,
        dateSeen object,
        actionsTaken object,
        petNo int64,
        staffNo int64,
        PRIMARY KEY(examNo),
        FOREIGN KEY(petNo) REFERENCES Pet(petNo),
        FOREIGN KEY(staffNo) REFERENCES Staff(staffNo)    
        );
        """
        
#cursor.execute(query)

# Insert Staff
query = """
    INSERT INTO Staff
    VALUES (1, "Person 1", "6473 Sherman Ave", 1258631594, "1981-09-24", "Nurse", 50000, 52);
    """

#cursor.execute(query)

# Insert Clinic
query = """
    INSERT INTO Clinic
    VALUES (52, "Clinic 52", "466 Prospect Blvd", 9391589634, 1);
    """
#cursor.execute(query)

# Insert Pet
query = """
        INSERT INTO Pet
        VALUES (578, "Max", "2013-05-12", "Dog", "Boxer", "Brown", 32, 52);
        """ 
#cursor.execute(query)

# Insert Owner
query = """
        INSERT INTO Owner
        VALUES (32, "Owner 1", "89 S Edmond Ave", 5493489657);
        """ 
#cursor.execute(query)

# Insert Exam
query = """
        INSERT INTO Exam
        VALUES (4789, "Broken ankle", "Needs surgery", "2022-12-05", "Pain medication prescribed", 578, 1);
        """
#cursor.execute(query)

# Select data
query = """
    SELECT *
    FROM Exam
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
