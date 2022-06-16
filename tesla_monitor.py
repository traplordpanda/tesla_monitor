import requests
import json
import time

class Tesla:
    def __init__(self):
        self.hits = list()
    
    def mon(self, discord_hook):
        self.webhook = discord_hook
        url = 'https://www.tesla.com/inventory/api/v1/inventory-results'
        qparams = {"query":{"model":"m3",
                            "condition":"new",
                            "options":{},
                            "arrangeby":"Relevance",
                            "order":"desc",
                            "market":"US",
                            "language":"en",
                            "super_region":
                            "north america",
                            "lng":-76.495,
                            "lat":39.1244,
                            "zip":"21122",
                            "range":200,
                            "region":"CA"},
                    "offset":0,"count":50,"outsideOffset":0,"outsideSearch":False}
        params = {"query":json.dumps(qparams)}
        headers = {
        'authority': 'www.tesla.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'ip_info={"ip":"71.244.237.162","location":{"latitude":39.1244,"longitude":-76.495},"region":{"longName":"Maryland","regionCode":"MD"},"city":"Pasadena","country":"United States","countryCode":"US","postalCode":"21122"}; m3_burst_sess=0%7CDcbW1eHvnx1takiQa1zo1hU8%2BJgXuYGngY8rinoFhwIgl9RboRz29zX0N80QT5%2Fi5jXYimr%2Bgr6zdENbFr98MRoZv0cjdcnVt0LyDyKL0x7sOT6eBmfHB0RDm3NikujOWKJ2%2B2ifWjUrsFEBZI4vs6ZmexsCXXwC7MlGOjbYvDn2rYfp3B4O39nQrFF%2BJ114QJNOmXHe0AkDCtfiFNadL092yEnHlVYrOHHWIvgIBcq2VDtbEcuvAma6PzVcZMvTz6EaE72Qy5qtPmdpYXRMZIQmcuNCmhsLEDXnkrjp%2FF9VR9eQRzcI3SLHB45FHNWcPNvAve%2B51DUF0jyRKJlPuZNmczkE%2FPv0Us9yq3C2GCB%2FYt3KI0kktGQDU7%2BhPhOlZjUzoZOyP0GspvJGYziQZiHNag%2BwEskXVjpT3yktVaG1QwFHa26%2Bm24l7pahYjesRbaZxBhANfkcDYveHwqm7g%3D%3D%7Cf4d14516b1cb8d72f3db137c43471966e978b1b7; NO_CACHE=Y; bm_sz=00CAACB1C7AE03867D1317CE495A2980~YAAQl2jcF29I6lN/AQAAhiqqeg86TdzsKmOdefJy5jiC1iSuYldZyUhvzstWCOUXPdRE2kGOnpwb28CN204ATC1NbglLM/hKTouTVTE+ULgwule+LB6OindNxjDceGyh7l3VERMFigRepjfNWRlE56FJ3V3KJIwdFfv3mYv2KHprCMdiBHYBVbk+8XdEr1GpZDioxWBpgODdUAQzpQ9/+fsoO9EsEg/dSokObquZDRRruF0v+K9S40/nYXPFvLbb5qVG8LbzfHbYx9maRBvsM9vbflCBCPpWjFV3ByGN2s8JzA==~4277555~4470593; oxpOriUrl=https%3A%2F%2Fwww.tesla.com%2Fteslaaccount%3Fredirect%3Dno; tesla_logged_in=Y; teslaSSORefreshToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR3bjV2bmNQUHhYNmprc2w5SUYyNnF4VVFfdyJ9.eyJpc3MiOiJodHRwczovL2F1dGgudGVzbGEuY29tIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnRlc2xhLmNvbS9vYXV0aDIvdjEvdG9rZW4iLCJpYXQiOjE2NDcwMzA1OTksImRhdGEiOnsic3ViIjoiMGVkMGQyMGUtNTk4OS00MDNhLWEzZDQtMTBhZTc1NTU2NDI3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwib3BlbmlkIiwib3VfY29kZSIsImVtYWlsIl0sImF6cCI6Im93bmVyc2hpcCIsImFtciI6WyJwd2QiXSwiYXV0aF90aW1lIjoxNjQ3MDMwNTk4fX0.XftNvaXl3miRtJB-_6zes1UE1RhHLua72cGFAss4XuF0J8p4gXM_gWD2NP1_jCYpUwIKuOfEfvH7SlRH_xr4UQz21pbqL8l4u9TKH2PyRnu_FphKLICKDMePHB7HSJtcoQpJCN3GXJ0xHIPy6e-GOfGxsaqj916_-kk_aY3_9_OL3KmqS6Eo5nRXCO3XH0VbgipBOQEaaUVvDtLYf_MpDeWi4_EYRRj1jID-GhCahYx0kSe3ECjERnO5U0YeYZJ1WExISbg0-MwNn2IOoicTI9ayE9P4CZ6BdkdlFHqIcFOMineKvbIpQIC_L2eRYFmW04dui6dmCbRAIRZgYdBejA; auth_session=caee6e9fbf; SSESSae26250c2355985f5d6661d51bf7b5cd=-wcPCJwpEmCSMdZPfqfsFRUBi9kvRf8kgtjcMKMf6hU; q_mail=kdaub.tf2%40gmail.com; q_first_name=Kyle; q_last_name=AuBuchon; products=m3; q_phone=6189748702; TeslaUser=%7B%22username%22%3A%22kdaub.tf2%40gmail.com%22%2C%22email%22%3A%22kdaub.tf2%40gmail.com%22%2C%22first_name%22%3A%22%22%2C%22last_name%22%3A%22%22%7D; has_js=1; buy_flow_locale=en_US; _abck=3DC34C6354CE573535EB9CDC0B3EE516~0~YAAQl2jcF/ml6lN/AQAA8uWsegfsumfGtwtnwsKU2HorvonqqGL+nYdR91x2TB/BU5w7/FUoQrElJwqcG4bK+a2dVTdVsmxdMhTjbXWCBGgh6TF57qeXgRsd1n6LLkPgex5YJe0fOPJFMTTL3vXH9neyLR/jcLGYYNFTTlG6IkAWiRvpX9ESGpLe4aUJGQjmrc2ifQihEahq897wG8FtS/59fcO6A8cMMHZRJC3xv5+AbChtIbI3ER7VXraONLvLUreS4SIQib8DFGikidDuFEVpAkEUo3vABBhkiPD/HA20h9UBWd+BAXHl3wnggrrEHDu61YYuLAfRGOM7OjDwTik0Gy4kaLQHT2KBDJyPNKt/UHFMS+chik9h3WSlc0EgN3yO5KEPe/VE19tnSz8KApE7XmQ=~-1~||-1||~-1; authTeslaWebToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMDM5MDQzODUiLCJhY2NvdW50SWQiOiIwN2VkMmFiNS05YTNkLTExZWEtYWQ5NC0wMDUwNTY5YWE0MDYiLCJmZWRlcmF0aW9uSWQiOiIwZWQwZDIwZS01OTg5LTQwM2EtYTNkNC0xMGFlNzU1NTY0MjciLCJtZmFFbmFibGVkIjpmYWxzZSwidXNlckNvdW50cnlDb2RlIjoiVVMiLCJlbWFpbCI6ImtkYXViLnRmMkBnbWFpbC5jb20iLCJpYXQiOjE2NDcwMzIwMjMsImV4cCI6MTY0NzAzMjE0M30.CtqaumGBcCcno-KG67RT8vrDqTAHjy7YacAeX0LDFm0; ak_bmsc=8CD639092327F7488A4F8BB2422A8AA9~000000000000000000000000000000~YAAQl2jcF05p+lN/AQAAhXY9ew/FZ+p6xWn6MTO+KV2M99CwdqaT1PIY+h+ScV+LKIEqx9/RaHWDma4SeqtIfyzXJX/Lwu+fQP2U1V7tqm365u8yVX4rp9SfaJEJxq974ZEQTZa3p/LsQ4DyTPVnvq5hCwXJHUOpB1FwHasgsJJo13Wh7RU/A2VxREr4bZlZp7YcelGTR8IZrwM9CFaJiTaWToRUInoItuiA/fTredO2xB7sbO5vuxtmxswuCe0nmuKC3h0nidYvmfDQFyZ/XvChLkX/PI+N/N8ZbGDmI7tLL1idKjClR/1nwcCAbrISZzQXXTCXfZdNh2m1g+EQ+IDbSRiFB7AbWRXw709+El9JW6WL97jRhd3Tmuv+Zx3zrV/rWc2DlUFsVA==; bm_sv=E2262B82CC2D2B9022E7C10A98A1CDB2~RBgCh4GAXB6u9pfbVbDyMV6oV3jCeFEPKYZkfxy9/+kyTV0IeYI+yVLWI8q0v5KgH4tIMScz+CMcE+nFlBhawD9OXK/Hhx4fajOlZBH/nCGu0RRHg1+dCWXH2CFv++pRWjf0UugLJq68Bh+Vx8OEWFongnprN8xEeN//nwQGiZo=; ak_bmsc=7317B1CB56404C9B621505644599C2EB~000000000000000000000000000000~YAAQiWjcF/vTRm1/AQAATQ1Cew+t/ZJfbMZ5IzNMzYex0KPT9+Yga2zrbUVdL52+cQoFs70keCoXbRCUHN1bAgNXMS0EdvJAak4UTvUCTVU6s5zoWVgXyRSMpR1E/LBv/PXcbpKQN1OhwzBoGRVFjvoXC+HhQEBjV2nuXFOyZfjuR58ecGuKBfhb16+H2QZ3a2JvsNaelaFVL8Jre4rX4JOwxv3Z8dFkwuTcvMOYEkUTjUG7pq2E8nihZwKVDcBAcQDOwPB9/k39o0zdoeBnjLYLqFhaGvl+f2+gFztiHFNLRlYBOzT59oMA6Qyoea/aBZAF2g9KAGJ1yQv+4vNNyZ/vhaX4LkQQ/D3RHZoyb9jGl9YkpTvdhOSfyek=; bm_sv=E2262B82CC2D2B9022E7C10A98A1CDB2~RBgCh4GAXB6u9pfbVbDyMV6oV3jCeFEPKYZkfxy9/+kyTV0IeYI+yVLWI8q0v5KgH4tIMScz+CMcE+nFlBhawD9OXK/Hhx4fajOlZBH/nCF0tqAKSw7/bqEILxX/5yx1o7Y+SiNwRNDKDQh39z55f9de++e2D4xtFUuh+jOQBTk=',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://www.tesla.com/inventory/new/m3?arrangeby=relevance&zip=21122&range=200',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4919.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers, params=params)
        if response.ok:
            self.data = response.json()
            t = time.localtime()
            cur_t = time.strftime("%H:%M", t)
            out = f'{cur_t} - {response} - {self.data}'
            
            if int(self.data.get('total_matches_found')) > 0:
                self.results = self.data.get('results')
                for i in self.results:
                    vin = i.get('VIN')
                    if vin not in self.hits:
                        c_url = f'https://www.tesla.com/m3/order/{vin}?token=&titleStatus=new&redirect=no#overview'
                        print(c_url)
                        self.webhook_alert(c_url)
                    self.hits.append(vin)
        else:
            print(response, response.text)

    def webhook_alert(self, url):
        webhook = ''
        webhook_content = {"username": "Tesla monitor",
                            "avatar_url": "https://en.wikipedia.org/wiki/Army_%26_Air_Force_Exchange_Service#/media/File:AAFES_Redesigned_Logo_2011-vector.svg",
                            "content":'',
                            "embeds":
                            [{
                                "color": 15258703,
                                "title": "instock",
                                "url": url,
                                "description": url,
                            }]
                            }
        payload = json.dumps(webhook_content)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.webhook, headers=headers, data=payload)

discord_hook = 'https://discord.com/api/webhooks/{}/{}'
tesla = Tesla(discord_hook)
while True:
    tesla.mon()
    time.sleep(5)