#!/bin/sh -e

if [ ! $(id -u) -eq 0 ]; then
	echo "must run as root"
	exit 1
fi

mount -o remount,size=16G /run

mount -o remount,size=16G /tmp


command -v zram-init && zram-init $((16*1024))
