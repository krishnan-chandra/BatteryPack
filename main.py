__author__ = 'Krishnan Chandra'

import argparse
from subprocess import call


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
    make_project(name, ' ')


def make_rails_project(name):
    make_project(name, ' ')


def make_node_js_project(name):
    make_project(name, ' ')


def main():
    parser = argparse.ArgumentParser(description='Parse options for projects')
    parser.add_argument('framework', choices=('flask', 'rails', 'nodejs'), type=str,
                        help='The framework you want to use for this project.', metavar='framework')
    parser.add_argument('name', type=str, help='The name of your project.', metavar='name')
    args = parser.parse_args()
    create_project(args.framework, args.name)


if __name__ == "__main__":
    main()
