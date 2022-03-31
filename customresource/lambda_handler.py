from crhelper import CfnResource

helper = CfnResource()





@helper.create
def create(event,context):
   helper.Data["message"] = "Stack Created"

@helper.delete
def delete(event,context):
    helper.Data["message"] = "Stack Deleted"

def handler(event,context):
    helper(event,context)
