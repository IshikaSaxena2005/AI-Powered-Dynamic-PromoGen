from PIL import Image, ImageDraw, ImageFont

def generate_banner(product_images, offer, color_palette, theme):
    # Create a banner size (width, height)
    banner_width = 800
    banner_height = 400
    banner = Image.new("RGB", (banner_width, banner_height), (255, 255, 255))  # White background

    # Draw the banner
    draw = ImageDraw.Draw(banner)

    # Set the background color based on the input
    bg_color = color_palette  # (R, G, B)
    draw.rectangle([0, 0, banner_width, banner_height], fill=bg_color)

    # Load product image
    try:
        product_image = Image.open(product_images[0])
        product_image.thumbnail((200, 200))  # Resize image
        banner.paste(product_image, (50, (banner_height - product_image.height) // 2))  # Center vertically
    except Exception as e:
        print(f"Error loading product image: {e}")

    # Set font styles
    try:
        # Load a TTF font
        font_offer = ImageFont.truetype("arial.ttf", 36)
        font_theme = ImageFont.truetype("arial.ttf", 24)

        # Draw offer text
        draw.text((300, 50), offer, fill=(255, 255, 255), font=font_offer)  # White text
        # Draw theme text
        draw.text((300, 150), theme, fill=(255, 255, 255), font=font_theme)  # White text
    except IOError:
        print("Font file not found, using default font.")
        draw.text((300, 50), offer, fill=(255, 255, 255))  # Default font
        draw.text((300, 150), theme, fill=(255, 255, 255))  # Default font

    # Save the banner
    banner_output_path = "output/banner.png"
    banner.save(banner_output_path)
    return banner_output_path
