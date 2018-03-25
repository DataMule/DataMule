# DataMule
Light weight data transfer containers with Command-line interface
### Installation
DataMule requires Python 3 to run, navigate to the same directory as [setup.py](https://github.com/DataMule/DataMule/blob/master/setup.py) and do
```
$ pip install .
```
### Usage
To run the app, make sure you are in the same directory as before. And then run
```sh
$ datamule run nyu_staff postgres
```
To see all currently running data processes, run
```sh
$ datamule ps
```
To remove a dataset, run
```sh
$ datamule rm nyu_staff postgres
```
### Example yaml file
The yaml file is made by the community for the users. It specifies any protocol that the dataset could be retrieved from, which is what we used in our application.
```sh
get_data:
  protocol: 'rest'
  connectors:
    - connector:
        connection_string: 'https://sandbox.api.it.nyu.edu/staff-exp/users'
        table_name: "nyu_staff"
        delta:
          type: 'page'
          value: 1
        schema: 'auto'
  auth: True
  format_type: 'json'
```
![Application Chart](https://raw.githubusercontent.com/johnnyprc/playaround-git/master/Capture.PNG)