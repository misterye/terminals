#!/bin/sh
sudo mount -o rw,uid=www-data,gid=www-data,umask=007 /dev/sda1 /var/usbdisk
