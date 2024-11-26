import math


def image_ramp_green(n):
    img = []
    f = 255 / (n - 1)
    for i in range(n):
        img.append({"red": 0, "green": math.floor((i) * f), "blue": 0, "alpha": 255})
    return img


def image_to_gray(img, n):
    for i in range(n):
        y = math.floor(
            0.3 * img[i]["red"] + 0.59 * img[i]["green"] + 0.11 * img[i]["blue"]
        )
        img[i]["red"] = y
        img[i]["green"] = y
        img[i]["blue"] = y


N = 100 * 100
img = image_ramp_green(N)
for _ in range(1000):
    image_to_gray(img, N)
