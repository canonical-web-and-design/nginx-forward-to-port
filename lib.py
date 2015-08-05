# System
import argparse
import sys
from jinja2 import Environment, FileSystemLoader
from os import symlink
from os.path import join

# Modules
from sh import service

templates_directory = 'templates'
forwarder_template = 'forward-to-port.conf'
nginx_sites_available = '/etc/nginx/sites-available'
nginx_sites_enabled = '/etc/nginx/sites-enabled'

def get_forwarding_options():
    """
    Get command-line arguments for use in the forward.py script
    - hostname
    - port
    """

    parser = argparse.ArgumentParser(
        description=(
            'Create a new nginx virtualhost '
            'to forward a subdomain to a specific port'
        )
    )
    parser.add_argument(
        '-d',
        '--hostname',
        help='The hostname to forward',
        required=True
    )
    parser.add_argument(
        '-l',
        '--listen',
        help='Where to listen for connections (usually "80")',
        required=True
    )
    parser.add_argument(
        '-p',
        '--port',
        help='The target port to forward to',
        required=True
    )
    arguments = parser.parse_args()

    return (arguments.hostname, arguments.listen, arguments.port)


def create_nginx_config(hostname, listen, port):
    """
    Parse the nginx config jinja2 template
    with the passed in arguments
    to produce a new config
    """

    jinja2_environment = Environment(loader=FileSystemLoader(templates_directory))
    config_template = jinja2_environment.get_template(forwarder_template)

    return config_template.render(hostname=hostname, listen=listen, port=port)

def save_nginx_site_config(nginx_config, hostname):
    """
    Given some nginx config
    save it into a "sites-available" file for nginx
    """

    config_filename = '{}.conf'.format(hostname)
    available_filepath = join(nginx_sites_available, config_filename)

    with open(available_filepath, 'w') as config_file:
        config_file.write(nginx_config)

def enable_nginx_site_config(hostname):
    """
    Enable the nginx site config for a specific file
    """

    config_filename = '{}.conf'.format(hostname)
    available_filepath = join(nginx_sites_available, config_filename)
    enabled_filepath = join(nginx_sites_enabled, config_filename)

    symlink(available_filepath, enabled_filepath)
