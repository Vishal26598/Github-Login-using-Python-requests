import requests, lxml.html
s = requests.session()

### Here, we're getting the login page and then grabbing hidden form
### fields.  We're probably also getting several session cookies too.
login = s.get('https://www.swiggy.com/bangalore/restaurants')
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
print(form)

## Now that we have the hidden form fields, let's add in our
## username and password.
form['login'] = 'vishalmiglani05@gmail.com'
form['password'] = 'Vishal@1998'
form['commit'] = 'Sign in'
response = s.post('https://github.com/session', data=form)

### How can we tell that we logged in?  Well, these worked for me:
# response.url
if 'Vishal26598/home' in response.text :
    print(response.text)
