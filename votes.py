from pprint import pprint as print
from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client
from pyswagger.utils import jp_compose

# load Swagger resource file into App object
app = App._create_('https://commonsvotes-api.parliament.uk/swagger/docs/v1')

# init swagger client
client = Client()

req, resp = app.op['Divisions', 'Divisions_SearchDivisions'](format="json")
resp = client.request((req, resp))
votes = resp.data
latest_vote_summary = votes[0]

votes_summary = [(vote['DivisionId'], vote['Number'], vote['Title']) for vote in votes]
print(votes_summary)

division_id = latest_vote_summary['DivisionId']
division_id = 959
req, resp = app.op['Divisions', 'Divisions_GetDivisionById'](format="json", divisionId=division_id)
resp = client.request((req, resp))
latest_vote_detail = resp.data

member_id = 4493

del latest_vote_detail['Noes']
del latest_vote_detail['Ayes']
del latest_vote_detail['NoVoteRecorded']
del latest_vote_detail['AyeTellers']
del latest_vote_detail['NoTellers']
print(latest_vote_detail)
