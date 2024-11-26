package main

import (
	"math"
)

type Pixel struct {
	Red   uint8
	Green uint8
	Blue  uint8
	Alpha uint8
}

func imageRampGreen(n int) []Pixel {
	img := make([]Pixel, n)
	f := 255.0 / float64(n-1)
	for i := 0; i < n; i++ {
		img[i] = Pixel{
			Red:   0,
			Green: uint8(math.Floor(float64(i) * f)),
			Blue:  0,
			Alpha: 255,
		}
	}
	return img
}

func imageToGray(img []Pixel, n int) {
	for i := 0; i < n; i++ {
		y := uint8(math.Floor(0.3*float64(img[i].Red) + 0.59*float64(img[i].Green) + 0.11*float64(img[i].Blue)))
		img[i].Red = y
		img[i].Green = y
		img[i].Blue = y
	}
}

func main() {
	N := 400 * 400
	img := imageRampGreen(N)
	for j := 0; j < 1000; j++ {
		imageToGray(img, N)
	}
}
