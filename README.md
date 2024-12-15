[![tests](https://github.com/michalkielan/ansible-role-swaywm/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/michalkielan/ansible-role-swaywm/actions/workflows/tests.yml)

ansible-role-swaywm
===================

An Ansible role to generate and deploy a customized Sway configuration. This role supports a wide range of configuration options from the Sway manual, which are exposed as variables for easier customization and management of your Sway setup.

Requirements
------------

Sway: This role is designed for use with the Sway window manager. Ensure that Sway is installed on your system.

Role Variables
--------------

See [defaults/main.yml](https://github.com/michalkielan/ansible-role-swaywm/blob/master/defaults/main.yml) and [tests/*.yml](https://github.com/michalkielan/ansible-role-swaywm/tree/master/tests) for the full set of default variables.

Dependencies
------------

None.

Example Playbook
----------------

The following example demonstrates a minimal playbook that deploys a default Sway configuration. The deployed config will be the same as the default one from `/etc/sway/config` unless overridden by specific variables.

```yml
----
- name: Deploy Sway configuration
  hosts: localhost
  vars:
    swaywm_users:
      - username: "{{ ansible_user_id }}"
        home: "{{ ansible_env.HOME | default('/home/{{ ansible_user_id }}') }}"

  roles:
    - ansible-role-swaywm
```

License
-------

[BSD](https://github.com/michalkielan/ansible-role-swaywm/blob/master/LICENSE)

Author Information
------------------

Michal Kielan, michalkielan@protonmail.com
