from flask import Blueprint
from controllers.health import health_check


health_views = Blueprint('health_views', __name__, template_folder='../templates')

# Route for health check
@health_views.route('/health', methods=['GET'])
def health():
    return health_check()