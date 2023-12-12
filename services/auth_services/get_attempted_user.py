from project.models.user_model import User
def getuser(username):
    user = User.query.filter_by(username=username).one_or_none()
    return user