Role Name
=========

A role to install and configure logstash instances.

Requirements
------------

N/A

Role Variables
--------------

### Required settings:
  - **ls_main_pipeline_src_dir**: Local directory that contains the pipeline .conf files. Always append a `/` to the end of the directory name so that rsync will sync the file contents and not the parent directory. (Example: `logstash_conf.d/`)

### Defaults:
  - **ls_version**: Version of logstash to install. (Default: `7.5.2`)
  - **el_java_package**: Name of java package on Enterprise Linux. (Default: `java-11-openjdk-devel`)
  - **debian_java_package**: Name of java package for Debian. (Default: `openjdk-11-jre-headless`)
  - **ls_service_enable**: Boolean to enable logstash service at startup. (Default: `true`)
  - **ls_node_name**: Name of logstash node. (Default: `{{ ansible_hostname }}`)
  - **ls_user**: User logstash files are owned by. (Default: `logstash`)
  - **ls_group**: Group logstash files are owned by. (Default: `logstash`)
  - **ls_apt_repo_url**: Debian repo url. (Default: `https://artifacts.elastic.co/packages/7.x/apt`)
  - **ls_debian_required_pkgs**: Required packages to install on Debian hosts. (Default: `gpg, apt-utils`)
  - **ls_default_dir_permissions**: Default permission set. (Default: `u=rwX,g=rX,o-rwx`)
  - **ls_conf_dir**: Logstash root configuration parent directory. (Default: `/etc/logstash`)
  - **ls_conf_dir_permissions**: Configuration directory custom permission set. (Default: `{{ ls_default_dir_permissions }}`)
  - **ls_conf_file_permissions**: Specific permission for `{{ ls_conf_dir }}/logstash.yml` (Default: `u=rw,g=r,o-rw`)
  - **ls_conf_file_template**: Template used to build logstash.yml. This probably shouldn't be changed unless you know what you are doing. (Default: `logstash.yml.j2`)
  - **ls_path_logs_permissions**: Specific permission set for logstash log files. (Default: `u=rwX,g=rX,o=rX`)
  - **ls_main_pipeline_dest_dir**: Directory to place the default pipeline file(s). (Default: `{{ ls_conf_dir }}/conf.d`)



### logstash.yml configuration
All of these settings are directly entered as their logstash.yml equilivent. The vaules below are their defaults. For example: ls_conf_file is entered into conf.file.

  - **ls_conf_file**: `{{ ls_conf_dir }}/logstash.yml`
  - **ls_path_data**: `/var/lib/logstash`
  - **ls_path_config**: `{{ ls_main_pipeline_dest_dir }}/*.conf`
  - **ls_config_reload_automatic**: `false`
  - **ls_config_reload_interval**: `3s`
  - **ls_config_support_escapes**: `false`
  - **ls_queue_type**: `memory`
  - **ls_queue_type**: `undefined`
  - **ls_path_queue**: `undefined`
  - **ls_queue_max_events**: `undefined`
  - **ls_queue_max_bytes**: `undefined`
  - **ls_queue_checkpoint_acks**: `undefined`
  - **ls_queue_checkpoint_writes**: `undefined`
  - **ls_queue_checkpoint_interval**: `undefined`
  - **dead_letter_queue_enable**: `undefined`
  - **ls_dead_letter_queue_max_bytes**: `undefined`
  - **ls_path_dead_letter_queue**: `undefined`
  - **ls_http_host**: `undefined`
  - **ls_http_port**: `undefined`
  - **ls_log_level**: `info`
  - **ls_path_logs**: `/var/log/logstash`

Any extra configuration beyond what can be accomplished above should be included in a map called
`ls_extra_settings`. An example of this is shown in the example playbook below.

Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - lksnyder0.logstash
      vars:
        ls_node_name: node
        ls_main_pipeline_src_dir: "default_config/"
        ls_extra_settings:
          xpack.management.elasticsearch.username: logstash_admin_user 
          xpack.management.elasticsearch.password: t0p.s3cr3t

License
-------

BSD

Author Information
------------------

N/A
