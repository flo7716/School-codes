$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.7.1-windows-x86_64.zip -OutFile elastic-agent-8.7.1-windows-x86_64.zip
Expand-Archive .elastic-agent-8.7.1-windows-x86_64.zip -DestinationPath .
cd elastic-agent-8.7.1-windows-x86_64
.\elastic-agent.exe install