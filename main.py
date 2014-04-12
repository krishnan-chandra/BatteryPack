__author__ = 'Krishnan Chandra'

import argparse
from subprocess import call
import json


def create_project(framework, name):
    create_function = {
        'django': make_django_project,
        'node_js': make_node_js_project,
        'flask': make_flask_project,
        'rails': make_rails_project
    }.get(framework, None)
    if create_function is None:
        print 'Framework you chose is not supported'
    create_function(name)


def make_project(name, project_loc):
    env_name = name + 'Env'
    call(['cp', '-R', project_loc, name])


def make_flask_project(name):
    make_project(name, 'flask/examples/blueprintexample')


def make_django_project(name):
    make_project(name, 'django/')


def make_rails_project(name):
    make_project(name, 'rails/')


def make_node_js_project(name):
    make_project(name, 'nodejs/')

def parse_config_file(fname):
    with open(fname) as f:
        config_dict = json.loads(f.read())
        return config_dict


def main():
    parser = argparse.ArgumentParser(description='Parse options for projects')
    parser.add_argument('config', type=str, help='The path to the JSON config file containing project config information', metavar='framework')
    args = parser.parse_args()


if __name__ == "__main__":
    main()
