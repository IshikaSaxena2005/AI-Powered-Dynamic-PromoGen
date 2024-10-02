from flask import Flask, render_template, request, jsonify
from utils.generate_content import generate_banner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    product_images = data.get('product_images', [])
    offer = data.get('offer', '')
    color_palette = data.get('color_palette', '')
    theme = data.get('theme', '')

    # Generate banner
    try:
        banner_path = generate_banner(product_images, offer, color_palette, theme)
        return jsonify({'banner_path': banner_path})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
