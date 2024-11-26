#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

typedef struct
{
  uint8_t red;
  uint8_t green;
  uint8_t blue;
  uint8_t alpha;
} Pixel;

Pixel *image_ramp_green(int n)
{
  Pixel *img = (Pixel *)malloc(n * sizeof(Pixel));
  float f = 255.0f / (n - 1);
  for (int i = 0; i < n; i++)
  {
    img[i].red = 0;
    img[i].green = (int)(i * f);
    img[i].blue = 0;
    img[i].alpha = 255;
  }
  return img;
}

void image_to_gray(Pixel *img, int n)
{
  for (int i = 0; i < n; i++)
  {
    int y = (int)(0.3f * img[i].red + 0.59f * img[i].green + 0.11f * img[i].blue);
    img[i].red = y;
    img[i].green = y;
    img[i].blue = y;
  }
}

int main()
{
  int N = 400 * 400;
  Pixel *img = image_ramp_green(N);
  for (int j = 0; j < 1000; j++)
  {
    image_to_gray(img, N);
  }

  free(img);
  return 0;
}
