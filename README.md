# wcrawl
This is a hobby project to implement a web crawler in Python. It is mostly an excuse to write backend code in Python and to try a few other technologies I haven't yet such as RabbitMQ and Mongodb.

## Software
The default test system uses MongoDB and RabbitMQ. Both of which need to be installed to run. The code is written with abstractions so these can be changed out. I would like to write azure based implentations using CosmosDB and Service Bus.

## Testing
I am trying out the idea of writing tests using Jupyter. Instead of python scripts there are Jupyter notebooks which contain tests. There is a custom inline cell magic component which can run test methods using Python's unittest library from cells.

## Configuration
The test code reads configuration from var/conf which is ignored by git, since the configuration could have secrets. See conf/test-sample.json. Fill in the appropriate values and place in var/conf.