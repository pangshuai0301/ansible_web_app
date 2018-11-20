#!/bin/bash

ACTION=$1

case "${ACTION}" in
update)
        VERSION="master"
	;;
rollback)
	VERSION="$2"
	;;
*)
	echo "Usage: $0 {update|rollback} [version]"
        exit 1
	;;
esac

sed -i -e /version:\ /d -e /dest/a"\ \ \ \ version:\ ${VERSION}" roles/git/tasks/main.yml

ansible-playbook -i hosts  playbook.yml -v
