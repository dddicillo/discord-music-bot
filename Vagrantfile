# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  # Network Setup
  config.vm.network "private_network", ip: "192.168.33.10"

  # Provisioning Script
  config.vm.provision "shell", path: "bootstrap.sh"

  # Shared Directory
  config.vm.synced_folder ".", "/vagrant"
end
