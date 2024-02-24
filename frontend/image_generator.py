from randimage import get_random_image
import matplotlib
import requests

courses_requests = requests.get("http://127.0.0.1:4000/api/courses")
courses_json = courses_requests.json()


def generate_group_image(group_name: str):
    img_size = (80, 250)
    img = get_random_image(img_size)
    matplotlib.image.imsave(f"./pictures/{group_name}.png", img)


for course in courses_json["courses"]:
    generate_group_image(course["_id"])
