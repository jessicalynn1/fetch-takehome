from flask import (Flask, request, session, jsonify)

import json

app = Flask(__name__, static_url_path='/static') 
app.secret_key = "dev"


user_points = []
sorted_points = sorted(user_points, key=lambda x: x['timestamp'])


class Transaction:
    """Payers, points, and timestamp"""
       
    def __init__(self, data):
        self.__dict__ = json.loads(data)

    def add(self):
        for x in self.__dict__:
            user_points.append(x)
        
        return sorted_points


class Spend:
    """Points spent"""
       
    def __init__(self, data):
        self.__dict__ = json.loads(data)

    def spend(self):
        while sorted_points and self.__dict__['points'] > 0:
            for x in sorted_points:
                if x['points'] >= self.__dict__['points']:
                    x['points'] - self.__dict__['points']
                    self.__dict__['points'] = 0
                if x['points'] <= self.__dict__['points']:
                    self.__dict__['points'] - x['points']
                    x['points'] = 0
            
            return sorted_points


class Balance:
    """Points balance"""

    def __init__(self, data):
        self.__dict__ = json.loads(data)

    def check_balance(self):
        balance_dict = {}

        for x in sorted_points:
            balance_dict[x['payer']] = x['points']

        return balance_dict
        