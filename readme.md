# Benchmark of several lanugages

- Ruby (ruby 3.3.6)
- Python (CPython 3.12.0, PyPy 7.3.9 with GCC 11.3.0)
- Lua (Lua 5.1.5, LuaJIT 2.1.1, LuaJIT 2.1.1 with C struct)
- JavaScript (Node v20.18.0)
- Java (OpenJDK 23.0.1)
- Go (go1.23.2)
- C (gcc 11.4.0)

| Relative performance                          |C (gcc 11.4.0)  |Lua (LuaJIT 2.1.1 with C struct)|Go (go1.23.2)    |Java (OpenJDK 23.0.1)|JavaScript (Node v20.18.0)|Lua (LuaJIT 2.1.1)|Python (PyPy 7.3.9)|Lua (Lua 5.1.5)    |Python (CPython 3.12.0)|Ruby               |
|--------------------------------|----------------|--------------------------------|-----------------|---------------------|--------------------------|------------------|-------------------|-------------------|-----------------------|-------------------|
|C (gcc 11.4.0)                  |1               |0.852216748768473               |0.600694444444444|0.284072249589491    |0.149395509499136         |0.0597375690607735|0.00818624899446363|0.00730481780179876|0.00314843124408532    |0.00306661467011735|
|Lua (LuaJIT 2.1.1 with C struct)|1.17341040462428|1                               |0.704861111111111|0.333333333333333    |0.175302245250432         |0.0700966850828729|0.00960582974494866|0.00857154921251531|0.00369440198005387    |0.00359839756088914|
|Go (go1.23.2)                   |1.66473988439306|1.41871921182266                |1                |0.472906403940887    |0.248704663212435         |0.0994475138121547|0.0136279752046562 |0.0121606215428789 |0.0052413190652981     |0.00510511575140922|
|Java (OpenJDK 23.0.1)           |3.52023121387283|3                               |2.11458333333333 |1                    |0.525906735751295         |0.210290055248619 |0.028817489234846  |0.0257146476375459 |0.0110832059401616     |0.0107951926826674 |
|JavaScript (Node v20.18.0)      |6.69364161849711|5.70443349753695                |4.02083333333333 |1.90147783251232     |1                         |0.399861878453039 |0.0547958169687219 |0.0488958324536587 |0.0210744704083861     |0.0205268195837913 |
|Lua (LuaJIT 2.1.1)              |16.7398843930636|14.2660098522168                |10.0555555555556 |4.75533661740558     |2.50086355785838          |1                 |0.137036861780154  |0.122281805514504  |0.0527043750454976     |0.0513347750558372 |
|Python (PyPy 7.3.9)             |122.156069364162|104.103448275862                |73.3784722222222 |34.7011494252873     |18.2495682210708          |7.29730662983426  |1                  |0.892327830089093  |0.38459998544078       |0.374605594356011  |
|Lua (Lua 5.1.5)                 |136.895953757225|116.665024630542                |82.2326388888889 |38.888341543514      |20.4516407599309          |8.17783149171271  |1.12066436379123   |1                  |0.431007497998107      |0.419807140071613  |
|Python (CPython 3.12.0)         |317.618497109827|270.679802955665                |190.791666666667 |90.2266009852217     |47.4507772020725          |18.9737569060774  |2.60010410258837   |2.32014525186843   |1                      |0.974013542737618  |
|Ruby                            |326.092485549133|277.901477832512                |195.881944444445 |92.6338259441708     |48.7167530224525          |19.4799723756906  |2.66947428192874   |2.38204619347211   |1.02667976996433       |1                  |


![Absolute benchmark results](AbsoluteBenchmarkResults.png)
![Relative benchmark results](RelativeBenchmarkResults.png)
![Scoped Absolute benchmark results](AbsoluteBenchmarkResultsNoLosers.png)
![Scoped Relative benchmark results](RelativeBenchmarkResultsNoLosers.png)

## `Ruby`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time ruby bench.rb

real    0m56,414s
user    0m56,363s
sys     0m0,047s
```

## `Python (CPython 3.12.0)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time python bench.py 

real    0m54,948s
user    0m54,925s
sys     0m0,021s
```

## `Lua (Lua 5.1.5)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time lua bench.lua

real    0m23,683s
user    0m23,660s
sys     0m0,021s
```

## `Python (PyPy 7.3.9)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time pypy3 bench.py

real    0m21,133s
user    0m20,888s
sys     0m0,242s
```

## `Lua (LuaJIT 2.1.1)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time luajit bench.lua

real    0m2,896s
user    0m2,873s
sys     0m0,023s
```

## `JavaScript (Node v20.18.0)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time node bench.js 

real    0m1,158s
user    0m1,142s
sys     0m0,033s
```

## `Java (OpenJDK 23.0.1)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ javac bench.java
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time java bench

real    0m0,609s
user    0m0,610s
sys     0m0,028s
```

## `Go (go1.23.2)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ go build -o gobench bench.go
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time ./gobench

real    0m0,288s
user    0m0,282s
sys     0m0,008s
```

## `Lua (LuaJIT 2.1.1 with C struct)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time luajit bench_ffi.lua

real    0m0,203s
user    0m0,200s
sys     0m0,003s
```

## `C (gcc 11.4.0)`
```shell
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ gcc -march=native -O2 -o gccbench bench.c
ryzh@ryzh-MaiBook-M:~/Downloads/Languages/lua/projects/ffi$ time ./gccbench

real    0m0,173s
user    0m0,167s
sys     0m0,005s
```

