#!/usr/bin/env python

# Local
from lib import (
    get_forwarding_options,
    create_nginx_config,
    save_nginx_site_config,
    enable_nginx_site_config
)

# Retrieve script arguments
(hostname, listen, port) = get_forwarding_options()

# Parse the template with the hostname and port
nginx_config = create_nginx_config(hostname, listen, port)

# Save into /etc/nginx/sites-available
save_nginx_site_config(nginx_config, hostname)

# Symlink into /etc/nginx/site-enabled
enable_nginx_site_config(hostname)
