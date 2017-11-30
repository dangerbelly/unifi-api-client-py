#A python class to interacting with the Unifi Controller API

import requests
import json


class Client:
    """__init__ creates a session attr. All of the methods in this class
        are performed on this session"""
    def __init__(self, base_url='https://localhost:8443', default_site='default'):

        self.base_url = base_url
        self.default_site = default_site

        self.s = requests.Session()
        self.s.headers.update({'Accept': 'application/json, text/plain, */*',
                 'Accept-Encoding': 'gzip, deflate,br',
                 'Connection': 'keep-alive',
                 'Content-Type': 'application/json;charset=utf-8',
                 'Host': 'localhost:8443',
                 'User-Agent': 'python-requests/2.4.3 CPython/3.4.0'
                 })
q
        return None

    #GET methods
    def login(self, username="captainunderpants", password="funny-farm-frank",verify=True):
        """Set session cookie and csrf_token attribute"""
        endpoint = '/api/login'
        url = self.base_url + endpoint
        data = {"username":username,"password":password,"remember":"false","strict":"true"}
        response = self.s.post(url, json=data, verify=verify)
        self.csrf_token = response.cookies['csrf_token']
        return response

    # 5 minute site stats method
    def stat_5minutes_sites(self, site=None, start=0, end=0):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/report/5minutes.site'
        url = self.base_url + endpoint
        attrs = ["bytes", "wan-tx_bytes","wan-rx_bytes","wlan_bytes","num_sta","lan-num_sta","wlan-num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        return self.s.get(url, json=data)

    # Hourly site stats method
    def stat_hourly_sites(self, site=None, start=0, end=0):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/report/hourly.site'
        url = self.base_url + endpoint
        attrs = ["bytes", "wan-tx_bytes","wan-rx_bytes","wlan_bytes","num_sta","lan-num_sta","wlan-num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        return self.s.get(url, json=data)


    # Daily site stats method
    def stat_daily_site(self, site=None, start=0, end=0):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/report/daily.site'
        url = self.base_url + endpoint
        attrs = ["bytes", "wan-tx_bytes","wan-rx_bytes","wlan_bytes","num_sta","lan-num_sta","wlan-num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        return self.s.get(url, json=data)

    def stat_5minutes_aps(self, site=None, start, end, mac):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/report/5minutes.ap'
        url = self.base_url + endpoint
        attrs = ["bytes", "num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        return self.s.get(url, json=data)

    def stat_hourly_aps(self, site=None, start, end, mac):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/report/hourly.ap'
        url = self.base_url + endpoint
        attrs = ["bytes", "num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        return self.s.get(url, json=data)

    def stat_daily_aps(self, site=None, start, end, mac):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/report/daily.ap'
        url = self.base_url + endpoint
        attrs = ["bytes", "num_sta","time"]
        data = {"attrs":attrs, "start":start, "end":end}
        return self.s.get(url, json=data)


    def stat_sessions(self, site=None, start, end, mac, type='all'):
        if not site:
            site = self.default_site
        endpoint = '/api/s' + site + '/stat/session'
        url = self.base_url + endpoint
        data = {"start":start, "end":end, "mac":mac}
        return self.s.get(url, json=data)

    def stat_sta_sessions_latest(self, site=None ,mac,limit):
        if not site:
            site = self.default_site
        endpoint = '/api/s' + site + '/stat/session'
        url = self.base_url + endpoint
        data = {"mac":mac,"_limit":limit,"_sort":sort,"-assoc_time":time}
        return self.s.get(url, json=data)

    def stat_auths(self, site=None, start,end):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/authorization'
        url = self.base_url + endpoint
        data = {"start":start, "end":end}
        return = self.s.get(url, json=data)

    # List all clients ever connected to the site
    def stat_allusers(self, site=None, hours):
        endpoint = '/api/s/' + site + '/stat/alluser'
        url = self.base_url + endpoint
        data = {"type":"all","conn":"all","within":hours}
        return self.s.get(url, json=data)

    # List guest devices
    def list_guests(self, site=None, within = 8760):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/guest'
        url = self.base_url + endpoint
        data = {"within":within}
        return self.s.get(url, json=data)

    def list_clients(self, site=None, client_mac):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/sta' + client_mac
        url = self.base_url + endpoint
        return self.s.get(url)

    def stat_client(self, site=None, client_mac):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/user' + client_mac
        url = self.base_url + endpoint
        return self.s.get(url)

    def list_usergroups(self, site=None):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/list/usergroup'
        url = self.base_url + endpoint
        return self.s.get(url)

    def set_usergroup(self, site=None, user_id, group_id):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/upd/user/' + user_id
        url = self.base_url + endpoint
        data = {"usergroup_id":group_id}
        return self.s.get(url, json=data)

    # Update user group
    def edit_usergroup(self, site=None, group_id,site_id,group_name,group_dn = -1,group_up = -1):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/rest/usergroup' + group_id
        url = self.base_url + endpoint
        data = {"_id":group_id, "name":group_name, "qos_rate_max_down":group_dn, "qos_rate_max_up":group_up,"site_id":site_id}
        return self.s.get(url, json=data)

    def create_usergroup(self, site=None, group_name,grouop_dn = -1,group_up = -1):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/rest/usergroup' + group_id
        url = self.base_url + endpoint
        data = {"_id":group_id, "name":group_name, "qos_rate_max_down":group_dn, "qos_rate_max_up":group_up,"site_id":site_id}
        return self.s.get(url, json=data)

    def delete_usergroup(self, site=None, group_id):
        if not site:
            site = self.default_site
        request_type = 'DELETE'
        endpoint = '/api/s/' + site + '/rest/usergroup/' + group_id
        url = self.base_url + endpoint
        return self.s.get(url)

    def list_health(self, site=None):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/health'
        url = self.base_url + endpoint
        return self.s.get(url)


    def list_dashboard(self, site=None, five_minutes = 'false'):
        if not site:
            site = self.default_site
        url_suffix = '?scale=5minutes'
        endpoint = '/api/s/' + site + '/stat/dashboard' + url_suffix
        url = self.base_url + endpoint
        return self.s.get(url)

    def list_users(self, site=None):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/list/user'
        url = self.base_url + endpoint
        return self.s.get(url)

    def list_devices(self, site=None, device_mac):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/stat/device' + device_mac
        url = self.base_url + endpoint
        return self.s.get(url)

    def list_tags(self, site=None):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/rest/tag'
        url = self.base_url + endpoint
        return self.s.get(url)

    def list_rogueaps(self, site=None):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/rest/rogueknown'
        url = self.base_url + endpoint
        return self.s.get(url)

    def list_sites(self):
        endpoint = '/api/self/sites'
        url = self.base_url + endpoint
        return self.s.get(url)

    def stat_site(self):
        endpoint = '/api/stat/sites'
        url = self.base_url + endpoint
        return self.s.get(url)

    def create_site(self, site=None, desc):
        if not site:
            site = self.default_site
        endpoint = '/api/s/' + site + '/cmd/sitemgr'
        data = {"cmd":"add-site","desc":desc}
        url = self.base_url + endpoint
        refereself.base_url + '/manage/site/' + site + '/dashboard'
        headers = {'X-Csrf-Token':self.csrf_token,'referer':referer}
        return self.s.post(url, json=data, headers=headers)
