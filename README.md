# CI-CD

## Environment setup

Install jenkins using docker follow the link:
https://dev.to/andresfmoya/install-jenkins-using-docker-compose-4cab  

Install python to your jenkins container.
Open docker container in terminal:  
![image](https://user-images.githubusercontent.com/67369891/201064644-a6930118-4020-4e62-80e7-5f048e11de0c.png)
type 
```
$ apt update
$ apt install python3
$ python3
$ quit()
```

Define pipeline in SCM:
https://www.jenkins.io/doc/book/pipeline/getting-started/#defining-a-pipeline-in-scm  

- click new item  

![image](https://user-images.githubusercontent.com/67369891/201055959-d9bcbd33-0fe2-4645-be4a-b23a7a9de367.png)  

- add name:  

![image](https://user-images.githubusercontent.com/67369891/201056371-32ada2f2-396c-405a-90c9-51b704e542d4.png)  

- in configuration of the pipeline choose Pipeline script from SCM:
![image](https://user-images.githubusercontent.com/67369891/201057041-ab783ccb-b4df-445b-8d67-46c275c8987f.png)  

provide link to git repository, branc to use and name of jenkins file  

![image](https://user-images.githubusercontent.com/67369891/201057433-f06edfa6-ac8c-4d6e-b07e-3fce656c13f5.png)
![image](https://user-images.githubusercontent.com/67369891/201058043-5bf8d9b8-7dff-4f4f-b267-8ad4ec160558.png)


## Packages you need:
- pymssql 2.2.5
- pytest 7.2.0
- pytest-html-reporter 0.2.9
They are listed in the requirements.txt file

## Useful hints 
### SQL Server
- to create a new user with password make sure to configure SQL Server Database Engine to start using SQL Server and Windows Authentication mode
https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/change-server-authentication-mode?view=sql-server-ver15
- to connect to SQL Server database make sure connection through TCP/IP is enabled
![img.png](img.png)
- to provide the correct port run the following query in  SQL Server Management Studio :  
```
DECLARE @portNumber NVARCHAR(10);

EXEC xp_instance_regread

     @rootkey = 'HKEY_LOCAL_MACHINE',

     @key = 'Software\Microsoft\Microsoft SQL Server\MSSQLServer\SuperSocketNetLib\Tcp\IpAll',

     @value_name = 'TcpDynamicPorts',

     @value = @portNumber OUTPUT;

SELECT [Port Number] = @portNumber;

GO
```
### Jenkins pipeline
to debug pipeline run there is no need to edit jenkins file in the repository  

You can go to builds, click on the last buils and choose replay to edit   

![image](https://user-images.githubusercontent.com/67369891/201061183-aaafc43b-9cbe-4d1d-80f6-a77b5772c5d3.png)  

And rerun the same build with changes in jenkins file  

![image](https://user-images.githubusercontent.com/67369891/201061388-83bbfe75-ff9e-44ff-8e56-4af876cc9f6d.png)

## Report

to create the report, run 
```$ pytest . --html-report=./report```
in terminal

use git bash

## Execution

to run test print in terminal :
```
python -m pytest .
```
