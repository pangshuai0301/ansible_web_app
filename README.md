This project is a demo of ansible playbook to manage a simple web app

##### Feature
- [x] deploy the simple web app with a full-deploy ansible playbook
- [x] update/rollback the version via update ansible playbook
##### Usage
- full-deploy
  1. edit the ```full-deploy/hosts``` file 
  2. edit the hosts column of the ```full-deploy/playbook.yml``` file
  3. exec ansible-playbook -i hosts playbook.yml -v
  4. wait for seconds and enjoy it
- update
  1. it will show a help log when you exec ```update/version_control.sh`` with no args
  2. read the help and exec, for example: 
     sh version_control.sh update or sh version_control.sh rollback c1cb862a2c758
  3. it will do the actions for [webservers-v0.1] you write in the ```update/hosts``` file by default
##### TODO
- [ ] use a Dynamic Inventory
- [ ] other...
