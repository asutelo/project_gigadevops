#!/bin/bash
# usage: sudo ./rules.sh proxy|backend
ROLE=$1
PROXY_IP=192.168.0.121
BACKEND_IP=192.168.0.122

iptables -F
iptables -P INPUT DROP

iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p icmp -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

case "$ROLE" in
  proxy)
    iptables -A INPUT -p tcp --dport 5000 -j ACCEPT ;;
  backend)
    iptables -A INPUT -p tcp -s $PROXY_IP --dport 8080 -j ACCEPT ;;
  *) echo "usage: $0 proxy|backend"; exit 1 ;;
esac
