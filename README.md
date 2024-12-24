# zabbix-edac

# Zabbix Template

Import `EDAC_template.yaml` into Zabbix in the templates section.

# User Parameters

Put the `userparam.conf` file into `/etc/zabbix/zabbix-agentd.d/` or `/etc/zabbix/zabbix_agent2.d/` depending on your Zabbix agent version and restart the Zabbix agent.

# Script

Put the `edac.py` into `/etc/zabbix/scripts/edac.py` and make it executable.

