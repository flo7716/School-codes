#installation de vagrant et virtualbox sur Windows 11
#téléchargement de vagrant
winget.exe install --id HashiCorp.Vagrant -e

#téléchargement de virtualbox
winget.exe install --id Oracle.VirtualBox -e

#vérification des installations
vagrant --version
VBoxManage --version

#fin du script