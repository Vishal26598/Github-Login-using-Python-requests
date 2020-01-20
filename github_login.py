import requests, lxml.html
s = requests.session()


login = s.get('https://github.com/login')
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
print(form)


form['login'] = 'vxxxxxxxxxni05@gmail.com'
form['password'] = 'Vixxxxxxx8'
form['commit'] = 'Sign in'
response = s.post('https://github.com/session', data=form)


if 'Vishal26598/home' in response.text :
    print(response.text)
