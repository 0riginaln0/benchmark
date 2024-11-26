(defn image-ramp-green [n]
  (let [f (/ 255 (- n 1))]
    (map (fn [i]
           @{:red 0
             :green (math/floor (* f i))
             :blue 0
             :alpha 255})
         (range n))))

(defn image-to-gray [img n]
  (for i 0 n
    (let [img-i (img i)
          y (math/floor (+ (* 0.3 (get img-i :red))
                           (* 0.59 (get img-i :green))
                           (* 0.11 (get img-i :blue))))]
      (set (img-i :red) y)
      (set (img-i :green) y)
      (set (img-i :blue) y))))

(def N (* 400 400))
(def img (image-ramp-green N))

(for _ 0 1000
  (image-to-gray img N))
