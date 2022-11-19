
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("hemavathi200214@gmail.com")
to_email = To("sripriyadevi2002@gmail.com")
subject = "ibm project sendgrid checking "
content = Content("text/plain", "chekcing ")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)