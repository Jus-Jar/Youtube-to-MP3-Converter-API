from flask import Blueprint,jsonify,send_file
from controllers.video import download_video, clear_cache_folder
from controllers.search import search_video_url_by_title


video_views = Blueprint('video_views', __name__, template_folder='../templates')

@video_views.route('/audio/<query>', methods=['GET'])
def get_audio_urls(query):
    #clear cache folder
    clear_cache_folder()

    #retrieve mp3 file
    videoObject = search_video_url_by_title(query)
    videoPath = download_video(videoObject)

    if videoPath:
        try:
            # Return the MP3 file as a response
            return send_file(videoPath, as_attachment=True, download_name=f'{videoObject["videoTitle"]}.mp3', mimetype='audio/mpeg')
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "File could not be generated"}), 500