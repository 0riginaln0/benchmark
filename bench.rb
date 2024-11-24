def image_ramp_green(n)
  img = []
  f = 255.0 / (n - 1)
  (0...n).each do |i|
    img << {
      red: 0,
      green: (i * f).floor,
      blue: 0,
      alpha: 255
    }
  end
  img
end

def image_to_gray(img, n)
  (0...n).each do |i|
    y = (0.3 * img[i][:red] + 0.59 * img[i][:green] + 0.11 * img[i][:blue]).floor
    img[i][:red] = y
    img[i][:green] = y
    img[i][:blue] = y
  end
end

N = 400 * 400
img = image_ramp_green(N)

1000.times do
  image_to_gray(img, N)
end
