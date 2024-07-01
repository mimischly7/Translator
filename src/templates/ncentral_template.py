jinja_template = \
    '''
    
This is customer/client name **{{ cust_struct.customer_name }}** and id {{ cust_struct.customer_id }}, located in
{{ cust_struct.city }}. This customer has a total of {{ meta.num_devices }} devices. Below follows detailed information.

{% macro format_device(dev_struct) %}
  - **Device**: 
    Device ID: {{ dev_struct.device_id}}
    Agent Version: {{ dev_struct.agent_version }}
    Description: {{ dev_struct.description }}
    Device Class: {{ dev_struct.device_class }}
    Device Class Label: {{ dev_struct.device_class_label }}
    Discovered Name: {{ dev_struct.discovered_name }}
    Interface Version: {{ dev_struct.discovered_name }}
    **Device Statistics**:
    {% for dev_stat in dev_struct.dev_stat_structs %}
      - Appliance ID: {{ dev_stat.appliance_id }}
        Appliance Name: {{ dev_stat.appliance_name }}
        Created On: {{ dev_stat.created_on }}
        Device Name: {{ dev_stat.device_name }}
        Device URI: {{ dev_stat.device_uri }}
        Is Managed Task: {{ dev_stat.is_managed_task }}
        Last Data ID: {{ dev_stat.last_data_id }}
        Last Scan Time: {{ dev_stat.last_scan_time }}
        Last Update: {{ dev_stat.last_update }}
        Module Name: {{ dev_stat.module_name }}
        Service ID: {{ dev_stat.service_id }}
        Service Item ID: {{ dev_stat.service_item_id }}
        State Status: {{ dev_stat.state_status }}
        Task ID: {{ dev_stat.task_id }}
        Task Ident: {{ dev_stat.task_ident }}
        Task Note: {{ dev_stat.task_note }}
        Time to Stale: {{ dev_stat.time_to_stale }}
        Transition Time: {{ dev_stat.transition_time }}
    {% endfor %}
{% endmacro %}

Customer Information:
- Customer Name: {{ cust_struct.customer_name }}
- Customer ID: {{ cust_struct.customer_id }}
- City: {{ cust_struct.city }}
- Contact Department: {{ cust_struct.contact_department }}
- Contact Email: {{ cust_struct.contact_email }}
- Contact Ext: {{ cust_struct.contact_ext }}
- Contact First Name: {{ cust_struct.contact_firstname }}
- Contact Last Name: {{ cust_struct.contact_lastname }}
- Contact Phone Number: {{ cust_struct.contact_phone_number }}
- Contact Title: {{ cust_struct.contact_title }}
- Country: {{ cust_struct.country }}
- Devices:
{% for dev_struct in cust_struct.dev_structs %}
  {{ format_device(dev_struct) }}
{% endfor %}
'''
