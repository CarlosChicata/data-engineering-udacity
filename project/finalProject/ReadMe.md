# Capstone : Basic Analytics workflow for delivery shipment startup
----------
## Context

The "Envialo!" is a peruvian startup is dedicated to delivery shipment between clients (company-users type). They are 3 year in production and have 3 branch in Perú (arequipa, lima and cuzco). They need to improve their process and recently create a analytics team. They wants to be the most important startup in this area in Perú.

You are newly hired in a delivery shipments startup like data engineering!. You open this area in your work and you have any task from analytics team to improve their jobs.

The analytics team work using manual processes to generate reports about performance of agents, branches and company in different time ranges; they separate bad data from good data to generate reports using specified requirements. In case of bad data, analytics team must need to analyze it later but now they need to storage in specified JSON format.

## General Purpose
You will create two things:
 1. A data warehouse to manage reports of analytics team.
 2. a data lake will store a bad datas.

## Specified Objects and requirements
the following sections explain more details about how you need to implement this tasks:

## Reports
The analytics team need following reports:


### Branches Report
Check performance of branch of 'Envialo!' each month. This report need following columns:

| Column name  | Description |
|--------------|---------------|
| Branch Name         | Name of branch |
| City                | Name of city |
| Country             | Name of Country |
| Number roadmap      | Number of total roadmap |
| Working chazki      | Number of chazki work in roadmap |


### Agent Report
Check performance of their agents affiliated each month. This report need following columns:

| Column name  | Description |
|--------------|---------------|
| Agent ID                      | ID of agent in system |
| Complete Name                 | Full name with lastname of agent |
| Completed roadmap             | Number of completed roadmap |
| Assigned roadmap              | Number of assigned roadmap |
| Disconnected Day              | Number of day doesn't connected |
| Average percentage of roadmap | Average percentage of roadmap per month |

### Top delivery Report
Which is the company that sends the most orders per month and quarter in the year. This report need following columns: 

| Column name  | Description |
|--------------|---------------|
| Name enterprise          | Name of enterprise |
| Counting of shipment     | Number of shipments sent from enterprise |
| Correct format shipments | Number of validated shipments don't need correct it |
| Wrong format shipments   | Number of invalidated shipments need correct it |

## Bad data
The format of bad datas is JSON format. the structure is:

| Column name  | Description |
|--------------|---------------|
| JSON string       | String of json with all raw data |
| reason error      | Reason why this data is wrong |
| stage of pipeline | Name of stage when error alert inside pipeline | 
| datetime alert    | Date when error occurred  |
| is fix            | Determinate if this row is fix |
| Dependencies      | List status & context of previous stage when error occurred | 

## Notes about the project

* The data is generated for this project; so they are faked. they do not belong to any company or public domain.

-----------
## Models of datawarehouse


## Diagram of arquitecture of project


## Set up of platform


## How to run this project
