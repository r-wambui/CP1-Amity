[![Build Status](https://travis-ci.org/r-wambui/CP1-Amity.svg?branch=master)](https://travis-ci.org/r-wambui/CP1-Amity)
# CP1-Amity
CP1-Amity is an application which allocates people to offices and livingspaces at random
![Screen shot](/designs/amity.png)
## Installation
Prepare directory for the folder
```
$mkdir ~/Amity
$cd ~/Amity
```
Activate the virtual environment
```
venv/bin/activate
```
Clone the repo
```
https://github.com/r-wambui/CP1-Amity.git
```
Install the requirements
```
pip install -r requirements.txt
```
Launch the project
```
python app.py -i
```
## Usage
``` create_room <room_name> <room_type>``` Creates a room where the the type can only be an office or a livingspace 

```add_person<first_name> <last_name> <job_type> [<want_accomodation>]``` Adds a person to the system with their names and job types, assigns vacant offices and livingspace at random. A person can choose to have accomodation or not.

 ```reallocate_person <first_name> <last_name> <room_name>``` Checks for available rooms,  a person was allocated and reallocates the person by their names to the avilable rooms.
 
 ```print_room <room_name>```Displays on the screen the occupants/ status of the room requested.
 
```print_allocations [--o=filename]```  Prints a list of allocations onto the screen, the optional  --o  option outputs the registered allocations to a txt file.

```print_unallocated [-o=filename]``` Prints a list of unallocated people to the screen. display if they are waiting to be allocated to the office or a livingspace. The optional  --o  option outputs the registered allocations to a txt file

```load_people```  Adds people to rooms from a txt file.

```print_room <room_name>``` Prints the names of all the people in  room_name  on the screen.

```save_state [--db=db_name]```Save all application data to the database 'database.db', or optionally, a user-defined database.

```load_state <db_name>``` Loads data from a database into the application.


