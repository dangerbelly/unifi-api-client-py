#A python port of the php unifi-api-client
#http://tom-henderson.github.io/2015/05/12/unifi-python.html
import requests
import json


class Client():

    def __init__(self):

        self.base_url = 'https://localhost:8443'

        self.site_default = 'default'

        self.s = requests.Session()

        self.s.headers.update({'Accept': 'application/json, text/plain, */*',
                 'Accept-Encoding': 'gzip, deflate,br',
                 'Connection': 'keep-alive',
                 'Content-Length': '93',
                 'Content-Type': 'application/json;charset=utf-8',
                 'Host': 'localhost:8443',
                 'User-Agent': 'python-requests/2.4.3 CPython/3.4.0'
                 })

        #data = {"username":"captainunderpants","password":"funny-farm-frank","remember":"false","strict":"true"}
        #url = 'https://localhost:8443/api/login'
        #self.s.post(url, json=data, verify=False)

        return None

    #API routes
    def login(self):
        endpoint = '/api/login'
        url = self.base_url + endpoint
        data = {"username":"captainunderpants","password":"funny-farm-frank","remember":"false","strict":"true"}
        r = self.s.post(url, json=data, verify=False)
        return r


#    def authorize_guest(self, site, mac, minutes, up = None, down = None, mbytes = None, ap_mac = None):
#        endpoint = '/api/s/' + site + '/cmd/stamgr'
#        url = self.base_url + endpoint
#        data = {"cmd":"authorize-guest","mac":mac,"minutes":minutes}
#        r = self.s.get(url, json=data)
#        return r

#    def unauthorize_guest():
#        endpoint = '/api/s/' + SITE + '/cmd/stamgr'
#        data = {"cmd":"unauthorize-guest","mac":MAC}

#    def reconnect_sta():
#        endpoint = '/api/s/' + SITE + '/cmd/stamgr'
#        data = {"cmd":"kick-sta","mac":MAC}

#    def block_sta():
#        endpoint = '/api/s/' + SITE + '/cmd/stamgr'
#        data = {"cmd":"block-sta","mac":MAC}

#    def unblock_sta():
#        endpoint = '/api/s/' + SITE + '/cmd/stamgr'
#        data = {"cmd":"block-sta","mac":MAC}

#    def set_sta_note(USER_ID, NOTE):
#        endpoint = '/api/s' + SITE + '/upd/user/' + USER_ID
#        data = {"note:NOTE"}

#    def set_sta_note(USER_ID, NAME):
#        endpoint = '/api/s' + SITE + '/upd/user/' + USER_ID
#        data = {"note:NAME"}

    # 5 minute site stats method
    def stat_5minutes_sites(self, site, start=0, end=0):
        endpoint = '/api/s/' + site + '/stat/report/5minutes.site'
        url = self.base_url + endpoint
        attrs = ["bytes", "wan-tx_bytes","wan-rx_bytes","wlan_bytes","num_sta","lan-num_sta","wlan-num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        r = self.s.get(url, json=data)
        return r

    # Hourly site stats method
    def stat_hourly_sites(self, site, start=0, end=0):
        endpoint = '/api/s/' + site + '/stat/report/hourly.site'
        url = self.base_url + endpoint
        attrs = ["bytes", "wan-tx_bytes","wan-rx_bytes","wlan_bytes","num_sta","lan-num_sta","wlan-num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        r = self.s.get(url, json=data)
        return r

    # Daily site stats method

    def stat_daily_site(self, site, start=0, end=0):
        endpoint = '/api/s/' + site + '/stat/report/daily.site'
        url = self.base_url + endpoint
        attrs = ["bytes", "wan-tx_bytes","wan-rx_bytes","wlan_bytes","num_sta","lan-num_sta","wlan-num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        r = self.s.get(url, json=data)
        return r 

    def stat_5minutes_aps(self, site, start, end, mac):
        endpoint = '/api/s/' + site + '/stat/report/5minutes.ap'
        url = self.base_url + endpoint
        attrs = ["bytes", "num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        r = self.s.get(url, json=data)
        return r

    def stat_hourly_aps(self, site, start, end, mac):
        endpoint = '/api/s/' + site + '/stat/report/hourly.ap'
        url = self.base_url + endpoint
        attrs = ["bytes", "num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        r = self.s.get(url, json=data)
        return r

    def stat_daily_aps(self, site, start, end, mac):
        endpoint = '/api/s/' + site + '/stat/report/daily.ap'
        url = self.base_url + endpoint
        attrs = ["bytes", "num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        r = self.s.get(url, json=data)
        return r

    def stat_sessions(self, site, start, end, mac, type='all'):
        endpoint = '/api/s' + site + '/stat/session'
        url = self.base_url + endpoint
        data = {"start":start, "end":end, "mac":mac}
        r = self.s.get(url, json=data)
        return r

    def stat_sta_sessions_latest(self, site ,mac,limit):
        endpoint = '/api/s' + site + '/stat/session'
        url = self.base_url + endpoint
        data = {"mac":mac,"_limit":limit,"_sort":sort,"-assoc_time":time}
        r = self.s.get(url, json=data)
        return r

    def stat_auths(self, site, start,end):
        endpoint = '/api/s/' + site + '/stat/authorization'
        url = self.base_url + endpoint
        data = {"start":start, "end":end}
        r = self.s.get(url, json=data)
        return r

    # List all clients ever connected to the site

    def stat_allusers(self, site, hours):
        endpoint = '/api/s/' + site + '/stat/alluser'
        url = self.base_url + endpoint
        data = {"type":"all","conn":"all","within":hours}
        r = self.s.get(url, json=data)
        return r

    # List guest devices

    def list_guests(self, site, within = 8760):
        endpoint = '/api/s/' + site + '/stat/guest'
        url = self.base_url + endpoint
        data = {"within":within}
        r = self.s.get(url, json=data)
        return r

    def list_clients(self, site, client_mac):
        endpoint = '/api/s/' + site + '/stat/sta' + client_mac
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def stat_client(self, site, client_mac):
        endpoint = '/api/s/' + site + '/stat/user' + client_mac
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def list_usergroups(self, site):
        endpoint = '/api/s/' + site + '/list/usergroup'
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def set_usergroup(self, site, user_id, group_id):
        endpoint = '/api/s/' + site + '/upd/user/' + user_id
        url = self.base_url + endpoint
        data = {"usergroup_id":group_id}
        r = self.s.get(url, json=data)
        return r

    # Update user group

    def edit_usergroup(self, site, group_id,site_id,group_name,group_dn = -1,group_up = -1):
        endpoint = '/api/s/' + site + '/rest/usergroup' + group_id 
        url = self.base_url + endpoint
        data = {"_id":group_id, "name":group_name, "qos_rate_max_down":group_dn, "qos_rate_max_up":group_up,"site_id":site_id}
        r = self.s.get(url, json=data)
        return r

    def create_usergroup(self, site, group_name,grouop_dn = -1,group_up = -1):
        endpoint = '/api/s/' + site + '/rest/usergroup' + group_id 
        url = self.base_url + endpoint
        data = {"_id":group_id, "name":group_name, "qos_rate_max_down":group_dn, "qos_rate_max_up":group_up,"site_id":site_id}
        r = self.s.get(url, json=data)
        return r

    def delete_usergroup(self, site, group_id):
        request_type = 'DELETE'
        endpoint = '/api/s/' + site + '/rest/usergroup/' + group_id
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def list_health(self, site):
        endpoint = '/api/s/' + site + '/stat/health'
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r


    def list_dashboard(self, site, five_minutes = 'false'):
        url_suffix = '?scale=5minutes'
        endpoint = '/api/s/' + site + '/stat/dashboard' + url_suffix
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def list_users(self, site):
        endpoint = '/api/s/' + site + '/list/user'
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def list_devices(self, site, device_mac):
        endpoint = '/api/s/' + site + '/stat/device' + device_mac
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def list_tags(self, site):
        endpoint = '/api/s/' + site + '/rest/tag'
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def list_rogueaps(self, site):
        endpoint = '/api/s/' + site + '/rest/rogueknown'
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def list_sites(self):
        endpoint = '/api/self/sites'
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def stat_site(self):
        endpoint = '/api/stat/sites'
        url = self.base_url + endpoint
        r = self.s.get(url)
        return r

    def create_site(self, site, desc):
        endpoint = '/api/s/' + site + '/cmd/sitemgr'
        data = {"cmd":"add-site","desc":desc}
        url = self.base_url + endpoint
        r = self.s.post(url, json=data)
        return r

    def delete_site(SITE_ID):
        endpoint = '/api/s/' + SITE + '/cmd/sitemgr'
        data = {"site":SITE_ID, "cmd":"delete-site"}

    def list_admins():
        endpoint = '/api/s/' + SITE + '/cmd/sitemgr'
        url = self.base_url + endpoint
        data = {"cmd":"get-admins"}
        r = self.s.post(url, json=data)
        return r

    def list_wlan_groups():
        endpoint = '/api/s/' + SITE + '/list/wlangroup'

    def stat_sysinfo():
        endpoint = '/api/s/' + SITE + '/stat/sysinfo'

    def stat_status():
        endpoint = '/status'

    def list_self():
        endpoint = '/api/s/' + SITE + '/self'

    def stat_voucher(CREATE_TIME):
        endpoint = '/api/s/' + SITE + '/stat/voucher'

    def stat_payment(WITHIN):
        url_suffix = '?within=' + WITHIN
        endpoint = '/api/s/' + SITE + '/stat/payment' + url_suffix

    def create_hotspotop(NAME, PASSWORD, NOTE=''):
        endpoint = '/api/s/' + SITE + '/rest/hotspot'
        data = {"name":NAME,"x_password":PASSWORD}

    def list_hotspotop():
        endpoint = '/api/s/' + SITE + '/rest/hotspotop'

#Fix arguments
    def create_voucher():
        endpoint = '/api/s' + SITE + '/cmd/hotspot'
        data = {"cmd":"create-voucher", "expire":MINUTES, "n":COUNT, "quota":QUOTA}

    def revoke_voucher(VOUCHER_ID):
        endpoint = '/api/s/' + SITE + '/cmd/hotspot'
        data = {"_id":VOUCHER_ID,"cmd":"delete-voucher"}

    def extend_guest_validiy(GUEST_ID):
        endpoint = '/api/s/' + SITE + '/cmd/hotspot'
        data = {"_id":GUEST_ID, "cmd":"extend"}

    def list_portforward_stats():
        endpoint = '/api/s/' + SITE + '/stat/portforward'

    def list_dpi_stats():
        endpoint = '/api/s/' + SITE + '/stat/dpi'

    def list_current_channels():
        endpoint = '/api/s/' + SITE + '/stat/current-channel'

    def list_portforwarding():
        endpoint = '/api/s/' + SITE + '/list/portforward'

    def list_dynamicdns():
        endpoint = '/api/s/' + SITE + '/list/dynamicdns'

    def list_portconf():
        endpoint = '/api/s/' + SITE + '/list/portconf'

    def list_extension():
        endpoint = '/api/s/' + SITE + '/list/extension'

    def list_settings():
        endpoint = '/api/s/' + SITE + '/get/setting'

    def adopt_device(MAC):
        endpoint = '/api/s/' + SITE + '/cmd/devmgr'
        data = {"mac":MAC,"cmd":"adopt"}

    def restart_ap(MAC):
        endpoint = '/api/s/' + SITE + '/cmd/devmgr'
        data = {"mac":MAC,"cmd":"restart"}

    def disable_ap(AP_ID, DISABLE):
        request_type = 'PUT'
        endpoint = '/api/s/' + SITE + '/rest/device' + AP_ID
        data = {"disable":DISABLE}

    # LED overrided mode can be 'on', 'off', 'default'

    def led_override(DEVICE_ID, OVERRIDE_MODE):
         request_type = 'PUT'
         endpoint = '/api/s/' + SITE + '/rest/device/' + DEVICE_ID
         data = {"led_override":OVERRID_MODE}

    def locate_ap(MAC, ENABLE):
        CMD = ['set-locate','unset-locate']
        endpoint = '/api/s/' + SITE + '/cmd/devmgr/'
        data = {"cmd":CMD, "mac":MAC}

    def site_leds(ENABLE):
        endpoint = '/api/s/' + SITE + '/set/setting/mgmt'
        data = {"led_enabled":ENABLE}

    def set_ap_radiosettings(AP_ID, RADIO, CHANNEL, HT, TX_POWER_MODE, TX_POWER):
        endpoint = '/api/s/' + SITE + '/upd/device' + AP_ID
#        data = {"radio_table":["radio":RADIO,"channel":CHANNEL,"ht":HT,"tx_power_mode":TX_POWER_MODE, "tx_power":TX_POWER]}

    #unsure about how this endpoint functions

    def set_ap_wlangroup(WLANTYPE_ID, DEVICE_ID, WLANGROUP_ID):
        endpoint = '/api/s/' + SITE + '/upd/device/' + DEVICE_ID
        WLANTYPE_ID = ['ng', 'na']
        data = {"wlan_overrides":[], "wlangroup_id": WLANTYPE_ID.WLANGROUP_ID}

# Set_guest login settings

#    options = [PORTAL_ENABLED, PORTAL_CUSTOMIZED, REDIRECD_ENABLED, REDIRECT_URL, X_PASSWORD, EXPIRE_NUMBER, EXPIRE_UNIT, SITE_ID]

    def set_guestlogin_settings():
        endpoint = '/api/s/' + SITE + '/set/setting/guest_access'
        data = {
                "portal_enabled":PORTAL_ENABLED,
                "portal_customized":PORTAL_CUSTOMIZED,
                "redirect_enabled":REDIRECT_ENABLED,
                "redirect_url":REDIRECT_URL,
                "x_password":X_PASSWORD,
                "expire_number":EXPIRE_NUMBER,
                "expire_unit":EXPIRE_UNIT,
                "site_id":SITE_ID
                }

    def rename_ap(AP_ID, APNAME):
        endpoint = '/api/s/' + SITE + '/upd/device' + AP_ID
        data = {"name":APNAME}

    def move_device(MAC,SITE_ID):
        endpoint = '/api/s/' + SITE  + '/cmd/sitemgr'
        data = {"site":SITE_ID, "mac":MAC, "cmd":"move-device"}

    def delete_device(MAC):
        endpoint = '/api/s/' + SITE + '/cmd/sitemgr'
        data = {"mac":MAC,"cmd":"delete-device"}

    def list_network_conf(self, site):
        endpoint = '/api/s/' + site + '/rest/networkconf'
        url = self.base_url + endpoint
        #url = 'https://localhost:8443/api/s/default/rest/networkconf'
        r = self.s.get(url)
        return r

    #To get the format of the network settings run a list_networkconf()
    #Do not include the _id property when creating a network
    #The controller will create and id for the new network

    def create_network(NETWORK_SETTINGS):
        request_type = 'POST'
        endpoint = '/api/s/' + SITE + '/rest/networkconf'
        data = NETWORK_SETTINGS

    #Update network settings

    def set_networksettings_base(NETWORK_ID, NETWORK_SETTINGS):
        request_type = 'PUT'
        endpoint = '/api/s/' + SITE + '/rest/networkconf/' + NETWORK_ID
        data = NETWORK_SETTINGS

    def delete_network(NEWORK_ID):
        request_type = 'DELETE'
        endpoint = '/api/s/' + SITE + '/rest/networkconf' + NETWORK_ID

    def list_wlanconf(WLAN_ID):
        endpoint = '/api/s/' + SITE + '/rest/wlanconf' + WLAN_ID

    #Create a WLAN

#    paramters = [NAME,'none',
#                 X_PASSPHRASE,'none',
#                 USERGROUP_ID = 'none',
#                 WLANGROUP_ID = 'none',
#                 ENABLED = 'true',
#                 HIDE_SSID = 'false',
#                 IS_GUEST = 'false',
#                 SECURITY = 'open',
#                 WPA_MODE = 'wpa2',
#                 WPA_ENC = 'ccmp',
#                 VLAN_ENABLED = 'false',
#                 VLAN,
#                 UAPSD_ENABLED = 'false',
#                 SCHEDULE_ENABLED = 'false',
#                 SCHEDULE]

    def create_vlan(parameters):
        endpoint = '/api/s' + SITE + '/add/wlanconf'
        data = {
                "name":NAME,
                "x_passphrase": X_PASSPHRASE,
                "usergroup_id":USERGROUP_ID,
                "wlangroup_id":WLANGROUP_ID,
                "enabled":ENABLED,
                "hide_ssid":HIDE_SSID,
                "is_guest":IS_GUEST,
                "secuirty":SECURITY,
                "wpa_mode":WPA_MODE,
                "wpa_enc":WPA_ENC,
                "vlan_enable":VLAN_ENABLED,
                "uapsd_enabled":UAPS_ENABLED,
                "schedule_enabled":SCHEDULE_ENABLED,
                "schedule":schedule
                }

    def set_wlansettings_base(WLAN_ID, WLAN_SETTINGS):
        request_type = 'PUT'
        endpoint = '/api/s/' + SITE + '/rest/wlanconf' + WLAN_ID
        data = WLAN_SETTINGS

    #Not sure the 2 following methods work with no endpoint

    def set_wlansettings(WLAN_ID, X_PASSPHRASE):
        request_type = 'PUT'
        endpoint = '/api/s/' + SITE + '/rest/wlanconf' + WLAN_ID
        data = WLAN_SETTINGS

#    def disable_wlan(WLAN_ID, DISABLE):


    def delete_wlan(WLAN_ID):
        request_type = 'DELETE'
        endpoint = '/api/s/' + SITE + '/rest/wlanconf' + WLAN_ID
        data = WLAN_SETTINGS

#    def set_wlan_mac_filter(WLAN_ID, MAC_FILTER_POLICY, MAC_FILTER_ENABLED, MACS):

    def list_events(HISTORYHOURS = 720, START = 0, LIMIT = 3000):
        endpoint = '/api/s/' + SITE + '/stat/event'
        data = {"_sort":"-time", "within":HISTORYHOURS, "type":null,"_start":START,"_limit":LIMIT}

    def list_alarms():
        url_suffix = "?archived=false"
        endpoint = '/api/s/' + SITE + '/cnt/alarm' + url_suffix

    def archive_alarm(ALARM_ID):
        endpoint = '/api/s' + SITE + '/cmd/evtmgr'
        data = {"_id":ALARM_ID,"cmd":"archive-alarm"}

    def upgrade_device(DEVICE_MAC):
        endpoint = '/api/s/' + SITE + '/cmd/devmgr/upgrade'
        data = {"mac":DEVICE_MAC}

    # Make sure to santize the url here

    def upgrade_device_external(FIRMWARE_URL, DEVICE_MAC):
        endpoint = '/api/s/' + SITE + '/cmd/devmgr/upgrade-external'
        data = {"url":FIRMWARE_URL,"mac":DEVICE_MAC}

    def power_cycle_switch_port(SWITCH_MAC, PORT_IDX):
        endpoint = '/api/s/' + SITE + '/cmd/devmgr'
        data = {"mac":SWITCH_MAC,"port_idx":PORT_IDX,"cmd":"power-cycle"}

    def spectrum_scan(AP_MAC):
        endpoint = '/api/s/' + SITE + '/cmd/devmgr'
        data = {"cmd":"spectrm-scan","mac":AP_MAC}

    def spectrum_scan_state(AP_MAC):
        endpoint = '/api/s/' + SITE + '/stat/spectrum-scan'

    # DEVICE_SETTINGS is an array with the device settings in it

    def set_device_settings_base(DEVICE_ID, DEVICE_SETTINGS):
        request_type = 'PUT'
        endpoint = '/api/s/' + SITE + '/rest/device/' + DEVICE_ID

    def list_radius_profiles():
        endpoint = '/api/s/' + SITE + '/rest/radiusprofile'

    def list_radius_accounts():
        endpoint = '/api/s/' + SITE + '/rest/account'

    #TODO ALL OF RADIUS API

    #ALIASES OF DEPRECATED FUNCTIONS
