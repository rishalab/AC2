# from ..file_map_engine.engine import parse
import os
import ast
from os import path
from pprint import pprint
import json
import ast
from flask import Flask, render_template
import sys
from file_map_engine.engine import get_calls
from file_map_engine.call_dir import dir_walk
import networkx as nx
import matplotlib.pyplot as plt
from test import make_ast

app = Flask(__name__)

@app.route('/')
def hello_world():
    script_dir = os.getcwd()
    # test_path = 'test/file.py'

    # test_path = 'test'
    new_dir = os.getcwd() + '\\test'
    tree = dir_walk(new_dir)

    # print(tree)


    # This if for engine of parsing.

    ########################################################################################

    new_calls_tree = {}

    for k in tree.keys():
        print(k, "\n-------------")
        for i in tree[k]:
            if i['type'] == 'file':
                if i['value'].split('.')[-1] == 'py':
                    print(i['value'])
                    code = open(i['value'], 'r', encoding='utf-8').read()
                    make_ast(code)
                    print("successful")
                    # temp_tree ,temp_mod = get_calls(i['value'])
                    # print(temp_mod)
    
    ########################################################################################
            


    return render_template('index.html', tree = tree)
    # return "hello_world"

if __name__ == '__main__':



    app.run(debug = True)

    
# call_list, imp_dict = get_calls(test_path)
# print(call_list)
# print(imp_dict)


    
