"""DB model for policy."""
from google.appengine.ext import ndb


class PolicyModel(ndb.Model):
    """Class that represents a tags and their associated schedule."""
    Name = ndb.StringProperty(indexed=True, required=True)
    Tags = ndb.JsonProperty(repeated=True)
    Projects = ndb.JsonProperty(repeated=True)
    Schedule = ndb.StringProperty(indexed=True, required=True, repeated=False)
    DisplayName = ndb.StringProperty(indexed=False, required=False)
