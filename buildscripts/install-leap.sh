#!/bin/sh

echo "==============================================="
echo "preparing leap"
echo "==============================================="

echo "deb http://debian.mirror.iphh.net/debian wheezy-backports main" > /etc/apt/sources.list.d/backports.list
apt-get update
apt-get -y install puppet rsync ruby-hiera-puppet git ruby1.9.1-dev rake jq
apt-get clean

echo "==============================================="
echo "installing leap"
echo "==============================================="
#gem install leap_cli
cd /tmp
git clone -b develop https://leap.se/git/leap_cli.git
cd leap_cli
git checkout bf6c804a7ed36043d6f43c1e38172b11ed50160a
rake build
rake install
mkdir /home/leap
cd /home/leap
git clone -b develop https://github.com/pixelated-project/leap_platform.git
cd /home/leap/leap_platform
git submodule sync
git submodule update --init
