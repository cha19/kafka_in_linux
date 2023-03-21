# kafka_in_linux
This repo is all about the kafka install in linux

setting up the consumer and producer 



Steps to install the kafka in linux

- search for the kafka download page and get the url
- using wget download the tarball eg: wget https://downloads.apache.org/kafka/3.4.0/kafka-3.4.0-src.tgz
- extract the tarball using the tar -xvf will get a folder
- In the folder you will have folder, find for the config folder and edit the server.properties and zookeeper-server-start.sh 
- In server.properties change the #advertised.listeners=PLAINTEXT://['localhost',<IP_ADDRESS>]:9092 and change the zookeeper.connect=['localhost',<IP_ADDRESS>]:2181

- after the change, save the changes and then start the zookeeper first using the following command 
- $ bin/zookeeper-server-start.sh conifg/zookeeper.properties

- now start the kafka specifying JMX port which is helpful in kafka manager(kafka GUI) 
- JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties
- default port for the zookeeper is 2181, for apache kafka is 9092

- to perform operations we can use the sh file in the bin folder to clear all the records in kafka

- how to install kafka manager/ Cluster manager for Apache kafka(AKA KAFKA GUI)
- to install kafka manager we required java 11 installed on the machine first
- clone the code for the https://github.com/yahoo/CMAK
- after cloning the code, change directory in the folder and perform ./sbt clean dist(cross check the sbt executable file in the code)
- .... this may take some time.......
- after sbt command you can now see a target folder has been created in the CMAK 
- $ cd target/universal
- you will find a cmak-3.0.0.7.zip file 
- you need to unzip the file, using $ unzip cmak-3.0.0.7.zip
- after unzipping $ cd cmak-3.0.0.7/conf
- you will find the application.conf file we need to make some changes in that file
- make some changes in file at  first occur => cmak.zkhosts="localhost:2181"

- after the changes in the kafka manager we will run the cmak
- $ bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080

- the cmak is running on the localhost -> http://localhost:8080 (as specified above)
- add the cluster, zookeeper running ip with port number in cluster zookeeper hosts localhost:2181
- enable jmx polling, poll consumer information 


