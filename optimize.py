from PIL import Image
import os

def resize_images(input_dir, output_dir):
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	for filename in os.listdir(input_dir):
		if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
			try:
				with Image.open(os.path.join(input_dir, filename)) as img:
					if img.mode != "RGB":
						img = img.convert("RGB")
					img.thumbnail((500, 400))
					img.save(os.path.join(output_dir, filename.split('.')[0] + '.jpg'), "JPEG", quality=80)
					print(f"{filename} resized and saved successfully.")
			except Exception as e:
				print(f"Error processing {filename}: {e}")

input_directory = "src/assets/imgs/works_src"
output_directory = "src/assets/imgs/works"

resize_images(input_directory, output_directory)
