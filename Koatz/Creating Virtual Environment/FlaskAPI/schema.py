from apiflask.schemas import Schema
from apiflask import fields

class TaskOutputSchema(Schema):
    id = fields.Integer()
    content = fields.String()
    date_added = fields.DateTime()
    is_completed = fields.Boolean()
    
class TaskCreateSchema(Schema):
    content = fields.String(required=True)
    
class TaskUpdateSchema(Schema):
    content = fields.String(required=True)
    is_completed = fields.Boolean(required=True)
    