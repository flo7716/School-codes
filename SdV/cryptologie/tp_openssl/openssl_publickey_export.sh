#!/bin/bash
openssl rsa -in private.pem -pubout -out public.pem
cat public.pem