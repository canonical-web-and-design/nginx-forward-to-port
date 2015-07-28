Subdomain forwarder for nginx
===

A script to create config files to forward hostnames to specific ports
in nginx.

Example usage
---

To forward "my-subdomain.example.com" from local port 80 to the local port "2222":

``` bash
sudo ./forward.py -d my-subdomain.example.com -l 80 -p 2222
```
