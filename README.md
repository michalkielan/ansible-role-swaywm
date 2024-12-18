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

<table>
  <tr>
    <th>Variable</th>
    <th>Type</th>
    <th>Default Value</th>
    <th>Description</th>
  </tr>
  <tr>
  <td><code>swaywm_sysconfdir</code></td>
  <td>String</td>
  <td><code>/etc</code></td>
  <td>System configuration directory.</td>
  </tr>
  <tr>
  <td><code>swaywm_font</code></td>
  <td>Dict</td>
    <td>
    <a href="https://github.com/michalkielan/ansible-role-swaywm/blob/master/defaults/main.yml">defaults/main.yml</a>
    </td>
    <td>Sets font to use for the title bars.</td>
  </tr>
  <tr>
    <td><code>swaywm_logo_key</code></td>
    <td>String</td>
    <td><code>Mod4</code></td>
    <td>Specify modifier key.</td>
  </tr>
  <tr>
    <td><code>swaywm_dir_keys</code></td>
    <td>Dict</td>
    <td>
    n/a
    </td>
    <td>Direction keys.</td>
  </tr>
  <tr>
    <td><code>swaywm_term</code></td>
    <td>String</td>
    <td><code>foot</code></td>
    <td>Default terminal.</td>
  </tr>
  <tr>
    <td><code>swaywm_menu</code></td>
    <td>String</td>
    <td><code>wmenu-run</code></td>
    <td>Default application launcher.</td>
  </tr>
  <tr>
    <td><code>swaywm_extra_variables</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of user defined variables, e.g.:
         <pre><code>swaywm_extra_variables:
  - name: "var1"
    value: "value1"
  - name: "var2"
    value: "value2"
</code></pre>
    </td>
  </tr>
   <tr>
    <td><code>swaywm_for_window</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of <code>for_window</code> commands, e.g.:
         <pre><code>swaywm_for_window:
  - class: "app_id='floating_shell'"
    criteria: "floating enable"
</code></pre>
    </td>
  </tr><tr>
    <td><code>swaywm_client</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of <code>client</code> commands, e.g.:
         <pre><code>swaywm_client:
  - name: focused
    border: &lt;color&gt;
    background: &lt;color&gt;
    text: &lt;color&gt;
    indicator: &lt;color&gt; # optional
    child_border: &lt;color&gt; # optional
</code></pre>
    </td>
  </tr>
  <tr>
    <td><code>swaywm_outputs</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of output configurations, e.g.:
         <pre><code>swaywm_outputs:
  - name: "*"
    options: "bg 'wallpaper.png' fill"
</code></pre>
    </td>
  </tr>
  <tr>
    <td><code>swaywm_inputs</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of input configurations, e.g.:
         <pre><code>swaywm_inputs:
  - name: "type:touchpad"
    options:
      - name: "Disable when typing"
        key: dwt
        value: "enabled"
      - name: "Enable tap"
        key: tap
        value: "enabled"
</code></pre>
    </td>
  </tr>
  <tr>
    <td><code>swaywm_keybindings_basics</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of basics key bindings, e.g.:
         <pre><code>swaywm_keybindings_basics:
  - name: "Start a terminal"
    key: "$mod+Return"
    exec: "exec $term"
</code></pre>
    </td>
  </tr>
  <tr>
    <td><code>swaywm_keybindings_utilities</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of utilities key bindings, e.g.:
         <pre><code>swaywm_keybindings_utilities:
  - name: "Audio mute"
    key: XF86AudioMute
    locked: true # optional
    exec: "&lt;mute command&gt;"
</code></pre>
    </td>
  </tr>
  <tr>
    <td><code>swaywm_keybindings_extra</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of extra key bindings, e.g.:
         <pre><code>swaywm_keybindings_extra:
  - name: "&lt;name&gt;"
    key: &lt;shortcut&gt;
    locked: false # optional
    exec: "&lt;command&gt;"
</code></pre>
    </td>
  </tr>
  <tr>
  <td>swaywm_bar</td>
  <td>Dict</td>
  <td>
...
  </td>
  <td>Bar configuration</td>
  </tr>
  <tr>
    <td><code>swaywm_autostart_apps</code></td>
    <td>List</td>
    <td><code>[]</code></td>
    <td>List of autostart apps, e.g.:
         <pre><code>swaywm_autostart_apps:
  - name: &lt;app name&gt;
    exec_always: false # optional
    exec: &lt;exe path&gt;
</code></pre>
    </td>
  </tr>
</table>

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
