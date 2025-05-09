from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os
import random
import colorsys

def create_gradient_background(size, start_color, end_color):
    """Create a gradient background"""
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    
    for y in range(size[1]):
        r = start_color[0] + (end_color[0] - start_color[0]) * y / size[1]
        g = start_color[1] + (end_color[1] - start_color[1]) * y / size[1]
        b = start_color[2] + (end_color[2] - start_color[2]) * y / size[1]
        draw.line([(0, y), (size[0], y)], fill=(int(r), int(g), int(b)))
    
    return image

def add_noise(image, intensity=10):
    """Add noise to the image"""
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            r += random.randint(-intensity, intensity)
            g += random.randint(-intensity, intensity)
            b += random.randint(-intensity, intensity)
            pixels[i, j] = (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))
    return image

def create_placeholder_image(filename, size, text, bg_color=(74, 144, 226), text_color=(255, 255, 255)):
    """Create a placeholder image with gradient background and effects"""
    # Create gradient background
    end_color = tuple(max(0, min(255, c + random.randint(-30, 30))) for c in bg_color)
    image = create_gradient_background(size, bg_color, end_color)
    
    # Add noise
    image = add_noise(image, intensity=5)
    
    # Apply blur effect
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)
    
    # Create drawing context
    draw = ImageDraw.Draw(image)
    
    # Try to load a font
    try:
        font_size = min(size[0]//10, size[1]//10)
        font = ImageFont.truetype("Arial", size=font_size)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Add text shadow
    shadow_offset = 2
    draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(0, 0, 0, 128))
    
    # Draw main text
    draw.text((x, y), text, font=font, fill=text_color)
    
    # Add decorative elements
    if 'reel' in text.lower():
        # Add circular border
        border_width = 5
        draw.ellipse([border_width, border_width, size[0]-border_width, size[1]-border_width], 
                    outline=text_color, width=border_width)
    
    # Save the image
    image.save(filename, quality=95)

def create_pattern_image(filename, size):
    """Create a pattern image for the newsletter section"""
    image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Draw diagonal lines
    for i in range(0, size[0] + size[1], 10):
        draw.line([(i, 0), (0, i)], fill=(74, 144, 226, 50), width=1)
    
    # Add some dots
    for _ in range(50):
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])
        draw.ellipse([x-2, y-2, x+2, y+2], fill=(44, 62, 80))
    
    image.save(filename)

def main():
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # Generate product images with different colors
    create_placeholder_image('images/classic-reel.jpg', (800, 800), 'Classic Reel',
                           bg_color=(74, 144, 226), text_color=(255, 255, 255))
    create_placeholder_image('images/custom-reel.jpg', (800, 800), 'Custom Reel',
                           bg_color=(44, 62, 80), text_color=(255, 255, 255))
    create_placeholder_image('images/premium-reel.jpg', (800, 800), 'Premium Reel',
                           bg_color=(231, 76, 60), text_color=(255, 255, 255))
    
    # Generate customer testimonial images
    create_placeholder_image('images/customer1.jpg', (400, 400), 'Customer 1',
                           bg_color=(52, 152, 219), text_color=(255, 255, 255))
    create_placeholder_image('images/customer2.jpg', (400, 400), 'Customer 2',
                           bg_color=(155, 89, 182), text_color=(255, 255, 255))
    
    # Generate Instagram feed images with different colors
    colors = [
        (46, 204, 113),  # Green
        (52, 152, 219),  # Blue
        (155, 89, 182),  # Purple
        (231, 76, 60)    # Red
    ]
    
    for i, color in enumerate(colors, 1):
        create_placeholder_image(f'images/instagram{i}.jpg', (400, 400), f'Instagram {i}',
                               bg_color=color, text_color=(255, 255, 255))
    
    # Generate hero background
    create_placeholder_image('images/hero-bg.jpg', (1920, 1080), 'Hero Background',
                           bg_color=(44, 62, 80), text_color=(255, 255, 255))
    
    # Generate pattern for newsletter section
    create_pattern_image('images/pattern.png', (100, 100))

if __name__ == '__main__':
    main() 