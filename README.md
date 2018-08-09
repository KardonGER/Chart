# Chart
This is my first Project and it's very specific to my Raspberry Pi filestructur, at the moment. 

Workflow:
1.       start the speed.sh shellscript
1.2.     speed.sh starts makecsv.py
1.2.1.   makecsv.py starts speedtest.py
1.2.2.   makecsv.py is editing the resultdata of speedtest.py
1.2.3.   makecsv.py is creating the file.csv from resultdata
1.3.     speed.sh starts chart.py
1.3.1.   chart.py is using pandas and plotly to create index.html
1.4.     speed.sh is copying the index.html to /var/www/html to use it with lighttpd

