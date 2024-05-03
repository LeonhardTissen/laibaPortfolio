from PIL import Image
import os

def resize_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Traverse input directory recursively
    for root, dirs, files in os.walk(input_dir):
        # Determine relative path inside input directory
        relative_root = os.path.relpath(root, input_dir)
        # Construct corresponding output directory path
        output_subdir = os.path.join(output_dir, relative_root)

        # Create the corresponding output subdirectory if it doesn't exist
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        # Process each file in the current directory
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                try:
                    input_path = os.path.join(root, filename)
                    output_path = os.path.join(output_subdir, filename.split('.')[0] + '.jpg')

                    with Image.open(input_path) as img:
                        if img.mode != "RGB":
                            img = img.convert("RGB")
                        img.thumbnail((500, 400))
                        img.save(output_path, "JPEG", quality=80)

                    print(f"{filename} resized and saved successfully.")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

# Example usage:
input_directory = "src/assets/imgs/works_src"
output_directory = "src/assets/imgs/works"

resize_images(input_directory, output_directory)
