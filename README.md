# JUVINI
## A Comprehensive tool for EDA


- **[Introduction](#introduction)** 
- **[Requirement](#requirement)**
- **[Assumption](#assumption)**
- **[Usage](#usage)**
- **[Examples](#examples)**
- **[Best Practices](#best-practices)**

## Introduction

Over the years , I have seen people struggling to set up a right environment to run data science tasks. Usually it is built over multiple servers given by the IT team where the data science team works with available packages or go over to IT team requesting a new package, or the data science team uses their personal laptops to test and configure new packages which sometimes become too difficult to scale as data increases.

Data Science is an evolving field and it is never advisable to restrict data scientists to limited resources. Over my entire career , I have worked mainly as big data engineer and data scientist. I have also worked for some time as a DBA and an IT admin. There is a lot of problems lying around when it comes to communication from IT team and Data science team. Being a Data Scientist, I know our requirements and also the restrictions faced by an industry IT team trying to be compliant with security.

This article is focused to resolve few of such issues by setting up a lab environment where data scientists can install , update or even tear down the system trying to build new technology as well as IT team not having to worry about too much maintenance and system failures. You might have already guessed it right by now. If not, let me tell you that the solution is “jupyterhub using docker containers”.

The idea of this article is to give a small lab environment where data scientists can login using credentials configured by the lab environment . After login , the user will be given a docker container that consists of all required data science tools pre-built. The user has complete freedom to install any libraries they require and even can tear down the packages. As soon as the user logs out , the container is terminated. It is like a use and throw mechanism. User has options to persist their work if required and also share their work to other users. The reason why I do not recommend the traditional sudo spawner mechanism is because it is difficult to manage virtual environment where one user can install a library without affecting other user’s library requirement. I find it easier and reliable to use docker containers rather than virtual conda environments.


## Requirement

1. Create an environment for multiple users to login and run data science tasks
2. Freedom for each user to install libraries without affecting other users
3. Work will be terminated after use, but should have provision to persist files if required
4. Different Authentication module support. Here we have tested it for LDAP AD
5. Ability to map windows drive into the lab environment using cifs
6. Should use https rather than http
7. Should contain all packages for anaconda3 library and additional utility tools
8. Ability to scale up if required
9. Ability to maintain major chunk of lab environment by non-root user.


## Assumption

1. The instruction is for people to setup lab from scratch
2. Have root privilege to install and setup users
3. Machine is accessible via browser to connect to jupyterhub web URL
4. file-system has enough space to handle data. Minimum 50GB and 12 CPU
5. ports 12000–12010 , 11100 to 11110 are open via firewall.

## Usage
1. Create a user and group called `labuser` and assign a specific `uid` and `guid` , say 2100. The number 2100 is important because going further docker containers will also be using same uid and guid to ensure the files persisted are accessible from host and vice versa
2. `groupadd -g 2100 labuser`
3. `useradd -u 2100 -d /home/labuser -ms /bin/bash -g labuser -p “$(openssl passwd -1 labuser123)” labuser` Feel free to change the password from *labuser123* to any password.

## Examples
1. Create a user and group called `labuser` and assign a specific `uid` and `guid` , say 2100. The number 2100 is important because going further docker containers will also be using same uid and guid to ensure the files persisted are accessible from host and vice versa
2. `groupadd -g 2100 labuser`
3. `useradd -u 2100 -d /home/labuser -ms /bin/bash -g labuser -p “$(openssl passwd -1 labuser123)” labuser` Feel free to change the password from *labuser123* to any password.

## Best Practices
1. Create a user and group called `labuser` and assign a specific `uid` and `guid` , say 2100. The number 2100 is important because going further docker containers will also be using same uid and guid to ensure the files persisted are accessible from host and vice versa
2. `groupadd -g 2100 labuser`
3. `useradd -u 2100 -d /home/labuser -ms /bin/bash -g labuser -p “$(openssl passwd -1 labuser123)” labuser` Feel free to change the password from *labuser123* to any password.
