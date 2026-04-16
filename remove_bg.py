from PIL import Image

def remove_background(input_path, output_path, tolerance=50):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    # Assume top-left pixel is the background color
    bg_color = data[0]
    
    for item in data:
        # Check if pixel is close to background color
        if (abs(item[0] - 255) < tolerance and 
            abs(item[1] - 255) < tolerance and 
            abs(item[2] - 255) < tolerance):
            # Change to transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Saved transparent logo to {output_path}")

input_img = r"C:\Users\hable\Desktop\Pagina serysa\WhatsApp Image 2026-02-20 at 4.30.34 PM.jpeg"
output_img = r"C:\Users\hable\Desktop\Pagina serysa\logo_transparent.png"
remove_background(input_img, output_img)
