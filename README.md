AWS Instance Information
========================


Summary
-------
awsi script can help search for a server in aws and connect to it.

It relise on you having boto installed and aws profiles set up containing your key and secret for each aws account.  
it has its own config file which list the profiles to use and the regions to search.

It will loop through every region and account until it finds a server that either matches the aws instanceId, the IP address or the Name tag.


Configuration
-------------
In you home directory create a folder called '.awsi'  
In this folder create a config file called 'config.cfg'

The contents of the file should look like the following.

[main]  
profiles: default,work,work2
regions: eu-west-1,eu-central-1,us-east-1,us-west-2,us-west-1


Usage
-----
usage awsi [i-12345|54.32.10.01|Live Web Server 01]


Todo
----
* Script will only find the first server matching the criteria, need to allow the user to 'keep searching' 
for example if multiple servers have the same name tag
* Validate region is real before openening connecton
* ~~Allow configuration by conf file, regions and profiles~~
* ~~Allow interupt~~