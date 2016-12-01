from twilio import rest
    # put your own credentials here
ACCOUNT_SID = 'ACaf288c67068f2eb80fe060d4367395a1'
AUTH_TOKEN = 'f1a98957b586147107830b655e31811b'

client = rest.TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to = '+19704585188',
    from_ = '+16502032341',
    body = 'first text from my computer, haha',
)