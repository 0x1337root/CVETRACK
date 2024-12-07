from datetime import date
import requests, re, webbrowser

browser = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
webbrowser.get(browser)
params = {'pubStartDate':str(date.today()) + 'T00:00:00.000', 'pubEndDate':str(date.today()) + 'T23:59:59.999'}
url = 'https://services.nvd.nist.gov/rest/json/cves/2.0/'
response = requests.get(url, params=params)
cve_list = re.findall('id"\s*:\s*"([^"]+)', response.text)

for i in range(0, len(cve_list)):
    cve_url = 'https://nvd.nist.gov/vuln/detail/' + str(cve_list[i])
    webbrowser.open(cve_url)