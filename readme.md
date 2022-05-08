# Fetch Take Home - Backend

The prompt was to write backend code to add, spend and check the balance of points in a user's account. The program is similar to a credit card that offers cash back or points for using the card at partner establishments.

I used an object oriented solution with classes for each functionality. These classes can be used throughout the server for multiple end points.


**CONTENTS**

- [Tech Stack](#tech-stack)
- [Object Oriented Solution](#object-oriented-solution)
- [Installation](#installation)
- [About the Developer](#about-the-developer)

## Tech Stack

**Backend:** Python3, Flask\

## OBJECT ORIENTED SOLUTION

### TRANSACTION

This class takes in json data and puts it into a python dictionary. The add function takes that dictionary data and adds it to a new python dictionary that then gets sorted by date (timestamp). Add function returns this new sorted dictionary.

### SPEND

This class takes in json data and puts it into a python dictionary. The spend function takes that dictionary data and compares it to the sorted dictionary. I used a combination of a while loop and if statements to decrease the points total as described in the prompt. Spend function returns the updated dictionary sorted by date.

## BALANCE

This class takes in json data and puts it into a python dictionary. The check balance function creates an empty dictionary and fills it with the requested data from the global variable called sorted points. The check balance function then returns this new dictionary that only has the requested data points.


## Installation

#### Requirements:

- Python 3.7.3

To have this app running on your local computer, please follow the steps below:

Clone repository:

```
$ git clone https://github.com/jessicalynn1/fetch-takehome.git
```

Create and activate a virtual environment:

```
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
```

Install dependencies:

```
(env) $ pip3 install -r requirements.txt
```

Start backend server:

```
(env) $ python3 server.py
```

Navigate to `localhost:5000/` to look under the hood!

## About the Developer

Jessica Faylor is a software engineer in the Greater San Diego Area, and previously worked in various fields, including finance, accounting and administration. She's looking for remote full time employment as a full stack engineer. In her off time she loves cooking, baking, and spending time with family.

Let's connect!

<p><a href="https://www.linkedin.com/in/jessica-faylor-0377b35/">
  <img
    alt="LinkedIn"
    src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"
  />
</a>
</p>