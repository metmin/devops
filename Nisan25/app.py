from flask import Flask, request
import json
import requests


host_ip = '192.168.135.112:8091'
host_username = 'Administrator'
host_password = 'password'


def pools_default():
    response = requests.get(
        f'http://{host_ip}/pools/default', auth=(host_username, host_password))

    return response.json()


app = Flask(__name__)


@app.route('/')
def available_commands():
    commands = {
        'available_commands': ['/add_node',
                               '/rebalance',
                               '/pools',
                               '/pools/node_list',
                               '/pools/nodes_info',
                               ]
    }
    commands_string = "Available Commands <hr>"
    for command in commands['available_commands']:
        commands_string += command + "<br>"

    return commands_string


@app.route('/add_node')
def add_node():

    if not request.args.get('ip') or not request.args.get('username') or not request.args.get('password') or not request.args.get('services'):
        message = "Missing Parameters <hr> Required Parameters: <br><br>"
        message += "ip <br> username <br> password <br> services"
        return message

    data = {
        'hostname': request.args.get('ip'),
        'user': request.args.get('username'),
        'password': request.args.get('password'),
        'services': request.args.get('services')
    }

    response = requests.post(f'http://{host_ip}/controller/addNode',
                             data=data, auth=(host_username, host_password))

    return response.content


@app.route('/rebalance')
def rebalance():

    nodes_info = pools_default()
    node_list = ""
    for node in nodes_info['nodes']:
        node_list += node['otpNode'] + ","
    node_list = node_list[:-1]

    data = {'knownNodes': f'{node_list}'}
    response = requests.post(f'http://{host_ip}/controller/rebalance',
                             data=data, auth=(host_username, host_password))

    return "Rebalance Başlatıldı."


@app.route('/pools')
def pools():

    response = requests.get(
        f'http://{host_ip}/pools/default', auth=(host_username, host_password))

    response_json = response.json()

    return str(response_json)


@app.route('/pools/node_list')
def node_list():

    response = requests.get(
        f'http://{host_ip}/pools/default', auth=(host_username, host_password))

    response_json = response.json()

    node_list = ""
    for node in response_json['nodes']:
        node_list += node['otpNode'] + "<br>"

    return node_list


@app.route('/pools/nodes_info')
def node_info():
    response = requests.get(
        f'http://{host_ip}/pools/default', auth=(host_username, host_password))

    response_json = response.json()

    nodes_info = "["
    for node in response_json['nodes']:
        nodes_info += str(json.dumps(node)) + ","
    nodes_info = nodes_info[:-1] + "]"

    return nodes_info
