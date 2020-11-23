# wcrawl
This is a hobby project to implement a web crawler in Python.

## Software
The default test system uses MongoDB and RabbitMQ. Both of which need to be installed to run. The code is written with abstractions so these can be changed out. I would like to write azure based implentations using CosmosDB and Service Bus.

## Testing
I am trying out the idea of writing tests using Jupyter. Run the script run-jupyter.bat and then run the test notebooks under test. I would like to look into writing jupyter inline magic which gives test assertion and reporting support.

## Configuration
The test code reads configuration from var/conf which is ignored by git, since the configuration could have secrets. See conf/test-sample.json. Fill in the appropriate values and place in var/conf.