# Chart
This is my first Project and it's very specific to my Raspberry Pi filestructur, at the moment. 

Workflow:
1.  start the speed.sh shellscript
2.  speed.sh starts makecsv.py
3.  makecsv.py starts speedtest.py
4.  makecsv.py is editing the resultdata of speedtest.py
5.  makecsv.py is creating the file.csv from resultdata
6.  speed.sh starts chart.py
7.  chart.py is using pandas and plotly to create index.html
8.  speed.sh is copying the index.html to /var/www/html to use it with lighttpd

