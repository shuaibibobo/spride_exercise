# action=lambda s:"s>1" if s>1 else "s=1" if s==1 else "s<1"
# print(action(int(input("请输入："))))
import requests
url="https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&" \
    "aid=6383&channel=channel_pc_web&aweme_id=7131674680703946020&" \
    "cursor=60&count=20&item_type=0&insert_ids=&" \
    "rcFT=AACqe-xzw" \
    "&version_code=170400&version_name=17.4.0&" \
    "cookie_enabled=true&screen_width=1920&" \
    "screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&" \
    "browser_version=104.0.0.0&browser_online=true&engine_name=Blink&engine_version=104.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&" \
    "device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&" \
    "webid=7092638864935011840&" \
    "msToken=bVC9qJRNwp3WYqXL4NKlp5ztcre-E5IRk2IEicTYqik4df5Fvqszh3FlP-8Jd1YWNnsUbkOeZ03ZIW0dwqvhSGoc112l5Et2V57qogRAADWyZ5hgKML5UVM0mqJQGI179Q==&" \
    "X-Bogus=DFSzswVutmsANxXhS6Hl1GUClLHT&" \
    "_signature=_02B4Z6wo00001qksn7gAAIDDgqbEfJ.6qa6pLJsAAMi-J8rII7mQf7vg6l4.WMDZuyJpTgWrCP8Y-Z.69YoCw6q-yMNmAIeNka0KNZCqh68snmPj-JGVFWvunkcVb1XfxHxrPJ16AqvTo19qe3"
headers={
    "sec-ch-ua-platform":"Windows",
    "sec-ch-ua":"Chromium" "v=104,Not A;Brand;v=99,Google Chrome;v=104",
    "Host":"www.douyin.com",
    "Connection":"keep-alive",
    "Accept":"application/json, text/plain, */*",
    "sec-ch-ua-mobile":"?0",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://www.douyin.com/",

    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cookie":"ttwid=1%7CFZ-WfJMxt6Chu1_Fg0spTmwamgA6FjCEU7_a7xkLho0%7C1651383685%7Caa7900ca18a22dcc51cd26c4c8b59ea3299c17d3213693d33c2b1ac06dde77ee; n_mh=K4txIDIowLxIk2MOK6WJpzmhCAtKs6iyHEG0Afqczcs; MONITOR_WEB_ID=f96461bc-88a8-41ba-98b2-b2e1dfa57458; s_v_web_id=verify_l5gx8g0d_edWcOI6z_cd1V_4dK4_AYcY_9BrfmWNpDfwZ; passport_csrf_token=ae4490ff29cb355c167b726e17894507; passport_csrf_token_default=ae4490ff29cb355c167b726e17894507; d_ticket=7f367b6994bca684e7084130c4591cdcc518f; passport_auth_status=14f53813b52bea014c0b9e86040db116%2C; passport_auth_status_ss=14f53813b52bea014c0b9e86040db116%2C; sso_auth_status=7af12db552901698cc0e784cbf729cdc; sso_auth_status_ss=7af12db552901698cc0e784cbf729cdc; sso_uid_tt=f4f6e8feea16d0917f7a26a39dbc17c5; sso_uid_tt_ss=f4f6e8feea16d0917f7a26a39dbc17c5; toutiao_sso_user=b103f6a9c42704cc8ebe546de790f66c; toutiao_sso_user_ss=b103f6a9c42704cc8ebe546de790f66c; sid_ucp_sso_v1=1.0.0-KGE3NmIyODk2NGM3MmUyMTA0OGNkMTZiYmUzYTIxZjU3YzNlN2MxOTkKHAiCrtnqLhCHwMaWBhjvMSAOMM3mrLcFOAJA8QcaAmxxIiBiMTAzZjZhOWM0MjcwNGNjOGViZTU0NmRlNzkwZjY2Yw; ssid_ucp_sso_v1=1.0.0-KGE3NmIyODk2NGM3MmUyMTA0OGNkMTZiYmUzYTIxZjU3YzNlN2MxOTkKHAiCrtnqLhCHwMaWBhjvMSAOMM3mrLcFOAJA8QcaAmxxIiBiMTAzZjZhOWM0MjcwNGNjOGViZTU0NmRlNzkwZjY2Yw; sid_guard=b103f6a9c42704cc8ebe546de790f66c%7C1657905159%7C5184000%7CTue%2C+13-Sep-2022+17%3A12%3A39+GMT; uid_tt=f4f6e8feea16d0917f7a26a39dbc17c5; uid_tt_ss=f4f6e8feea16d0917f7a26a39dbc17c5; sid_tt=b103f6a9c42704cc8ebe546de790f66c; sessionid=b103f6a9c42704cc8ebe546de790f66c; sessionid_ss=b103f6a9c42704cc8ebe546de790f66c; sid_ucp_v1=1.0.0-KDI2OGMyNjhkNDkyNTk2NjIyYTkxYzJkMDliNDBlMmJiMDBjYmI1YTcKHAiCrtnqLhCHwMaWBhjvMSAOMM3mrLcFOAJA8QcaAmxmIiBiMTAzZjZhOWM0MjcwNGNjOGViZTU0NmRlNzkwZjY2Yw; ssid_ucp_v1=1.0.0-KDI2OGMyNjhkNDkyNTk2NjIyYTkxYzJkMDliNDBlMmJiMDBjYmI1YTcKHAiCrtnqLhCHwMaWBhjvMSAOMM3mrLcFOAJA8QcaAmxmIiBiMTAzZjZhOWM0MjcwNGNjOGViZTU0NmRlNzkwZjY2Yw; __ac_signature=_02B4Z6wo00f01oA-.owAAIDDq7SlSUMQ-tKAHvoAAMLe3fZBUzN9ehgKSok7GqnlLwfjP-LcPGqDfbNEUvHGr9B4228GAcM9Tv2xljM.wzFWB96Xp8xO0omvb3PnXsHMuLBulneY82I4yBlJ23; strategyABtestKey=1660444529.086; download_guide=%221%2F20220814%22; THEME_STAY_TIME=%22299524%22; IS_HIDE_THEME_CHANGE=%221%22; _tea_utm_cache_2018=undefined; _tea_utm_cache_1243=undefined; odin_tt=6506e594880b691f489541949333088eb7cb1f769cf8c020345ed6f39e182bb6101aaa4e5d92693b66468a9126cd0bad5298c332533120b898c6466cdce26140; douyin.com; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA5WkHrndUhV8lfmpIRskYX9Ztgy7KsQm5a6LlaOZcbyA%2F1660492800000%2F0%2F0%2F1660493062880%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA5WkHrndUhV8lfmpIRskYX9Ztgy7KsQm5a6LlaOZcbyA%2F1660492800000%2F0%2F1660492462881%2F0%22; msToken=XRhp6Nvdgs_kVeGUMJjyNBxykcjfIbVeao5Ym-gJWzevFDc0aTsi-cAaHk2Q3d4HbDWUDvYF3NYxWbOrYvn2lbXJdRBjiwQNUPfoF1_1zbTeYN_WkkdhDPVEknVpeYc9mg==; home_can_add_dy_2_desktop=%221%22; tt_scid=xQ7PtDYTsWE9FHUju61GvAsOwdWm9NvJ.Hq2B9nfPxxXS4aqnbJT497wW0bHg95H6752; msToken=bVC9qJRNwp3WYqXL4NKlp5ztcre-E5IRk2IEicTYqik4df5Fvqszh3FlP-8Jd1YWNnsUbkOeZ03ZIW0dwqvhSGoc112l5Et2V57qogRAADWyZ5hgKML5UVM0mqJQGI179Q==",

}
response=requests.get(url=url,headers=headers)

# -*-coding:utf8-*-





print(response.content.decode("utf-8"))

