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
cursor.execute(query)

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
cursor.execute(query)

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
cursor.execute(query)

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
cursor.execute(query)

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
cursor.execute(query)

# Insert Staff1
query = """
    INSERT INTO Staff
    VALUES (1, "Person 1", "6473 Sherman Ave", 1258631594, "1981-09-24", "Nurse", 50000, 52);
    """
cursor.execute(query)

# Insert Staff2
query = """
        INSERT INTO Staff
        VALUES (2, "Person 2", "9466 Saint Ter", 1972322548, "1983-11-21", "Nurse", 60000, 64);
        """
cursor.execute(query)

# Insert Staff3
query = """
        INSERT INTO Staff
        VALUES (3, "Person 3", "7364 Saddle Ct", 1598523367, "1979-06-02", "Technician", 70000, 64);
        """
cursor.execute(query)

# Insert Staff4
query = """
        INSERT INTO Staff
        VALUES (4, "Person 4", "818 W Gude Dr", 3648273658, "1991-03-12", "Nurse", 45000, 52);
        """
cursor.execute(query)

# Insert Clinic52
query = """
    INSERT INTO Clinic
    VALUES (52, "Clinic 52", "466 Prospect Blvd", 9391589634, 1);
    """
cursor.execute(query)

# Insert Clinic64
query = """
    INSERT INTO Clinic
    VALUES (64, "Clinic 64", "67 Blue Ridge Rd", 9391589634, 2);
    """
cursor.execute(query)

# Insert Pet1
query = """
        INSERT INTO Pet
        VALUES (578, "Max", "2013-05-12", "Dog", "Boxer", "Brown", 32, 52);
        """ 
cursor.execute(query)

# Insert Pet2
query = """
        INSERT INTO Pet
        VALUES (109, "Zeus", "2018-04-26", "Dog", "Beagle", "White", 56, 52);
        """ 
cursor.execute(query)

# Insert Pet3
query = """
        INSERT INTO Pet
        VALUES (288, "Bailey", "2017-07-28", "Cat", "Persian", "Orange", 32, 64);
        """ 
cursor.execute(query)

# Insert Pet4
query = """
        INSERT INTO Pet
        VALUES (432, "Apollo", "2016-10-03", "Dog", "Labradoodle", "Black", 78, 64);
        """ 
cursor.execute(query)

# Insert Owner1
query = """
        INSERT INTO Owner
        VALUES (32, "Owner 1", "89 S Edmond Ave", 5493489657);
        """ 
cursor.execute(query)

# Insert Owner2
query = """
        INSERT INTO Owner
        VALUES (56, "Owner 2", "6 Sligo Pkwy", 4865327716);
        """ 
cursor.execute(query)

# Insert Owner3
query = """
        INSERT INTO Owner
        VALUES (78, "Owner 3", "98 Wintergreen Ave", 9782334522);
        """ 
cursor.execute(query)

# Insert Exam1
query = """
        INSERT INTO Exam
        VALUES (4789, "Broken ankle", "Needs surgery", "2022-12-05", "Pain medication prescribed", 578, 1);
        """
cursor.execute(query)

# Insert Exam2
query = """
        INSERT INTO Exam
        VALUES (4066, "Vomiting", "Stomach flu", "2022-11-17", "Medication prescribed", 109, 2);
        """
cursor.execute(query)

# Insert Exam3
query = """
        INSERT INTO Exam
        VALUES (4165, "Not eating or drinking", "Performed x-rays", "2022-03-18", "Staying overnight", 432, 3);
        """
cursor.execute(query)

# Insert Exam4
query = """
        INSERT INTO Exam
        VALUES (4790, "Bump on back", "Tumor", "2022-12-05", "Medication prescribed", 288, 4);
        """
cursor.execute(query)

# Select data1
query = """
        SELECT p.ownerNo, ownerName, COUNT(*)
        FROM Pet p, Owner o
        WHERE p.ownerNo = o.ownerNo
        GROUP BY p.ownerNo;     
        """
cursor.execute(query)

# Select data2
query = """
        SELECT *
        FROM Exam
        WHERE dateSeen BETWEEN "2022-06-01" AND "2022-10-31";    
        """
cursor.execute(query)

# Select data3
query = """
        SELECT c.staffNo, staffName, clinicName
        FROM Clinic c, Staff s
        WHERE c.staffNo = s.staffNo
        """
cursor.execute(query)

# Select data4
query = """
        SELECT staffNo, staffName, position, salary
        FROM Staff
        WHERE salary > 50000
        """
cursor.execute(query)

# Select data5
query = """
        SELECT p.petNo, petName, ownerName, examNo, dateSeen
        FROM Pet p, Exam e, Owner o
        WHERE p.ownerNo = o.ownerNo AND p.petNo = e.petNo;
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
print(df['examNo'])

# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
