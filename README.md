***Archived***

*This codebase is no longer maintained or used.*

---

Forward to port (for nginx)
===

A script to create config files to forward hostnames to specific ports
in nginx.

Example usage
---

To forward port `80` of `my-subdomain.example.com` to the local port `2222`:

``` bash
sudo pip install -r requirements.txt  # Install all requirements, system-wide
sudo ./nginx-forward.py -d my-subdomain.example.com -l 80 -p 2222
```
