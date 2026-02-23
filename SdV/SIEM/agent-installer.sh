#!/bin/bash

curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.7.1-linux-x86_64.tar.gz
tar xzvf elastic-agent-8.7.1-linux-x86_64.tar.gz
cd elastic-agent-8.7.1-linux-x86_64
sudo ./elastic-agent install