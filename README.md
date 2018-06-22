# streams-drill-demo
Quick demo using python streams producer.
This will request data from weather.gov json API for a single weather station (KEQY - Monroe, NC) and produce to a MapR Streams stream named '/demo-stream' with a single topic 'topic1'.

Note - Some real world testing shows that your python execution environment must match where you're installing the MapR client.  Replace 'pip install' with the appropriate 'pip#' command.

1. Requires your environment have the Streams Python client installed.
    * follow instructions here: https://maprdocs.mapr.com/60/MapR_Streams/MapRStreamsPythonExample.html
    * Or - run the included 'install_kafka_client.sh' 
    
    `bash install_kafka_client.sh`

    * May also need Python requests library and gcc:
    
    `sudo pip install requests`
    
    `sudo apt-get install gcc`

2. You still need to edit .bashrc to set LD_LIBRARY_PATH.  Add the following to the end of .bashrc:
  
    `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/mapr/lib`

3.  Set up the stream and topic. Run the setup script
  
    `bash setup_stream.sh`

4.  Run 'read_stream.py' in a separate shell to watch the messages:
  
    `python read_stream.py`

5.  Execute the producer 'weather_producer.py'
  
    `python weather_producer.py`
