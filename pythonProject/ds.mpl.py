# Download the helper library from https://www.twilio.com/docs/python/install
import os
from secondtwi.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC949ff01b8bf33c99d655f948c45d6a6c"
auth_token = "40d7d4878926928f8b473c3dc313f06d"
verify_sid = os.environ["YOUR_VERIFY_SID"]
verified_number = "+919514486659"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)