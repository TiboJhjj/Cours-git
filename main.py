import requests

def get_cat_image():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.status_code == 200:
        image_url = response.json()[0]['url']
        image_data = requests.get(image_url).content
        with open('cat-image.jpg', 'wb') as file:
            file.write(image_data)
        with open('README.md', 'w') as mdfile:
            mdfile.write(f"![Cat Image]({image_url})\n")
        print("Cat image saved and Markdown updated")
    else:
        print("Failed to get cat image")

if __name__ == "__main__":
    get_cat_image()
