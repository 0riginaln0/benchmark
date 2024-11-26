import java.util.ArrayList;
import java.util.List;

class Pixel {
    int red;
    int green;
    int blue;
    int alpha;

    Pixel(int red, int green, int blue, int alpha) {
        this.red = red;
        this.green = green;
        this.blue = blue;
        this.alpha = alpha;
    }
}

public class bench {

    public static int floor(double value) {
        return (int) Math.floor(value);
    }

    public static List<Pixel> imageRampGreen(int n) {
        List<Pixel> img = new ArrayList<>();
        double f = 255.0 / (n - 1);
        for (int i = 0; i < n; i++) {
            img.add(new Pixel(0, floor(i * f), 0, 255));
        }
        return img;
    }

    public static void imageToGray(List<Pixel> img, int n) {
        for (int i = 0; i < n; i++) {
            Pixel pixel = img.get(i);
            int y = floor(0.3 * pixel.red + 0.59 * pixel.green + 0.11 * pixel.blue);
            pixel.red = y;
            pixel.green = y;
            pixel.blue = y;
        }
    }

    public static void main(String[] args) {
        int N = 400 * 400;
        List<Pixel> img = imageRampGreen(N);
        for (int j = 0; j < 1000; j++) {
            imageToGray(img, N);
        }
    }
}
