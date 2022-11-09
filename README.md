# Hello PyTest task

## Environment setup

Install  
- python  3.11.0
- pip  21.3.1

## Packages you need:
- pymssql 2.2.5
- pytest 7.2.0
- pytest-html-reporter 0.2.9

## Useful hints
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