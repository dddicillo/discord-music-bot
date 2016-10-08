# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Network Setup
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.hostname = "dev.discord-music-bot"
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.ignore_private_ip = true
  config.hostmanager.include_offline = false

  cached_addresses = {}
  config.hostmanager.ip_resolver = proc do |vm, resolving_vm|
    if cached_addresses[vm.name].nil?
      if hostname = (vm.ssh_info && vm.ssh_info[:host])
        vm.communicate.execute("/sbin/ifconfig eth1 | grep 'inet addr' | tail -n 1 | egrep -o '[0-9\.]+' | head -n 1 2>&1") do |type, contents|
          cached_addresses[vm.name] = contents.split("\n").first[/(\d+\.\d+\.\d+\.\d+)/, 1]
        end
      end
    end
    cached_addresses[vm.name]
  end

  # Provisioning Script
  config.vm.provision "shell", path: "bootstrap.sh"

  # Shared Directory
  config.vm.synced_folder ".", "/vagrant"
end
