# sg-ancient-poem
Faculty of Arts and Social Science - Chinese Studies - website

# IDE Recommended to use Visual Studio Code

To open terminal
1. click Terminal 
2. New Terminal 

navigate to the folder containing the source code

use `ls` to list directories (folders and files)
use `cd` (change directory) to navigate to the folder containing the source code 

```
PS C:\Users\Li Xin\Desktop> cd .\sg-ancient-poem\
PS C:\Users\Li Xin\Desktop\sg-ancient-poem>
```
You can press tab which autocompletes the directory

use `cd ..` to go back up one level to the previous directory. Note the space between `cd` and `..`

```
PS C:\Users\Li Xin\Desktop\sg-ancient-poem> cd ..
```
power shell commands: https://devblogs.microsoft.com/scripting/table-of-basic-powershell-commands/

# Instructions to git 

1. install git
2. use the terminal to navigate to the folder containing the source code
3. run `git init` to initialize the folder as a git project
```
PS C:\Users\Li Xin\Desktop\test> git init
Initialized empty Git repository in C:/Users/Li Xin/Desktop/test/.git/
```

To retrieve the latest changes, run `git pull https://github.com/lxin42140/sg-ancient-poem-copy`
This will merge the changes on git with your local folder

To commit your changes
1. use `git status` to view the current status of changes, files removed or added
2. use `git add` to add the changes. You can use `git add -a` to add all the changes at once
3. use `git commit your\changes\made -m "Changes made"` to commit your change along with a message. The message is required. Run `git commit -a -m "New changes"` to commit all changes together instead of one by one
4. use `git push https://github.com/lxin42140/sg-ancient-poem-copy` to push your changes to the online repo

Commit before you push.

Link to common commands: https://dzone.com/articles/top-20-git-commands-with-examples

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

Frontend: Jinja Template, HTML 5, CSS, Javascript

Frontend Template: [Colorlib Theme - Juli](https://colorlib.com/wp/template/juli/) < License Purchased >

Backend: Python Flask

Cloud Deploy: AWS Elastic Beanstalk

Database: AWS RDS (for database), AWS Route53 (for hostname) 


## AWS Related

### A. AWS Credentials

- 


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
If changes are not updated, try viewing the page under incognito mode.

### C. AWS RDS Credentials

- 

## D. MySQL Client

```
mysql -h sg-jiutishi-db.ciuqsne5nixf.ap-southeast-1.rds.amazonaws.com -u admin -p
```

## Recommended Database Management tool
MySQL Workbench, Navicat Premium

To sort chinese characters in utf8mb4 without collators, convert characters to gb18030(official character set for PRC supporting traditional and simplified chinese) during sorting. 

```
ORDER BY CONVERT(fullName USING gb18030) asc;
```
 
## Project structure

static folder contains CSS files, images, pdf etc

template folder contains HTML templates used. The unused folder can be disregarded
 1. Base-slider html contains the template for the navigation bar. This is reused for all pages. 
 2. slider-poem-list is reused to display the list of poems, videos and files.
 3. shirenjianjie html is used for shirenjianjie topic only
 4. poem-content html is used to display one poem
 5. paper-content html is used to display the pdf file
 6. homepage html contains data for home page. No database operations here.
 
## Useful Website

## 1) Tools
 - [Online Photo Editor](https://pixlr.com/x/)
 - [Online Video Editor](https://www.kapwing.com/)
 - [Online convert text in picture to text](https://ocr.wdku.net/)
 - [毛笔字在线生成, 黄庭坚书法字体](http://www.diyiziti.com/maobizi)

## 2) References 
 - [AWS Route 53](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)
 - [AWS Domain Registeration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html#getting-started-find-domain-name)
 - [Flask DB guide](https://www.cnblogs.com/ssjz12/p/10181615.html)
 - [Flask Tutorial](http://www.pythondoc.com/flask-mega-tutorial/)
 - [AWS RDS NOTES](https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80)
