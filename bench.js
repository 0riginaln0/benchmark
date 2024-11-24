function imageRampGreen (n) {
  const img = []
  const f = 255 / (n - 1)
  for (let i = 0; i < n; i++) {
    img.push({
      red: 0,
      green: Math.floor(i * f),
      blue: 0,
      alpha: 255
    })
  }
  return img
}

function imageToGray (img, n) {
  for (let i = 0; i < n; i++) {
    const y = Math.floor(
      0.3 * img[i].red + 0.59 * img[i].green + 0.11 * img[i].blue
    )
    img[i].red = y
    img[i].green = y
    img[i].blue = y
  }
}

const N = 400 * 400
const img = imageRampGreen(N)
for (let j = 0; j < 1000; j++) {
  imageToGray(img, N)
}
