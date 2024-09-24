from flask import Blueprint,jsonify
from controllers.search import search_video_url_by_title,search_videos_info_by_title


search_views = Blueprint('search_views', __name__, template_folder='../templates')

# Route for health check
@search_views.route('/search/title/<query>', methods=['GET'])
def get_video_url(query):
    result = search_video_url_by_title(query)
    return jsonify(result)


@search_views.route('/search/title/<query>/<numResults>', methods=['GET'])
def get_multiple_video_urls(query,numResults):
    result = search_videos_info_by_title(query,int(numResults))
    return jsonify(result)