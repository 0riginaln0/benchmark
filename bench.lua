local function image_ramp_green(n)
  local img = {}
  local f = 255 / (n - 1)
  for i = 1, n do
    img[i] = {
      red = 0,
      green = math.floor((i - 1) * f),
      blue = 0,
      alpha = 255
    }
  end
  return img
end

local function image_to_gray(img, n)
  for i = 1, n do
    local y = math.floor(0.3 * img[i].red + 0.59 * img[i].green + 0.11 * img[i].blue)
    img[i].red = y
    img[i].green = y
    img[i].blue = y
  end
end

local N = 300 * 300
local img = image_ramp_green(N)
for _ = 1, 1000 do
  image_to_gray(img, N)
end
