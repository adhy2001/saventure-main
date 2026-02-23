from PIL import Image
from collections import Counter

def get_dominant_color(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
        img = img.resize((50, 50))  # Resize for speed
        pixels = list(img.getdata())
        # Filter out transparent pixels
        pixels = [p for p in pixels if p[3] > 128]
        if not pixels:
            return None
        # Count most common colors
        counts = Counter(pixels)
        most_common = counts.most_common(1)[0][0]
        return "#{:02x}{:02x}{:02x}".format(most_common[0], most_common[1], most_common[2])
    except Exception as e:
        return str(e)

print(get_dominant_color("c:/Users/Adhi/sample-loud--feature-v1/images/Logo1 copy.png"))
