# sg-ancient-poem
Faculty of Arts and Social Science - Chinese Studies - website


## Instructions to run - localhost


A. Set up python3 virtual environment:

Mac:

```
$ python3 -m venv venv

$ virtualenv venv
```

Linux
```
source venv/bin/activate
```


Windows

```
$ venv\Scripts\activate

(venv) $ pip install flask
```

B. Install the packages:

```
pip install -r requirements.txt
```


C. run the backend:
```bash

python3 application.py

```

D. Go to http://localhost:5000


## Technology Used

Frontend: HTML 5, CSS, Javascript

Backend: Python Flask

Cloud Deploy: AWS Elastic Beanstalk

Database: AWS RDS (for database), AWS Route53 (for hostname) 


## AWS Related

### A. AWS Credentials

Account: chsll@nus.edu.sg
Password:  <ask prof>


### B. AWS Elastic Beanstalk

 - Read: https://aws.amazon.com/elasticbeanstalk/
 - Continuous Deployment Command
 
```
eb init
eb deploy 
```

If eb setup is already there in the localhost or no new branch created, can just type:
```
eb deploy 
```

Noted: need to commit first, and then run the command, the command will sync the latest commit to the AWS remote host.

### C. AWS RDS Credentials

database name: poemDB
database password: <ask prof>


## D. MySQL Client

```
mysql -h sg-jiutishi-db.ciuqsne5nixf.ap-southeast-1.rds.amazonaws.com -u admin -p
```

## Recommended Database Management tool
MySQL Workbench, Navicat Premium




## AWS TO-DO

Secure practice: Make it https: Use AWS Cloudfront to make all the traffic https


