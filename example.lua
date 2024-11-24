local ffi = require("ffi")


print('OS', ffi.os)
print('Arch', ffi.arch)
print('Little-endian', ffi.abi('le'))

ffi.cdef [[
int printf(const char *fmt, ...);

typedef struct point_t {
  int x;
  int y;
} point_t;
]]

ffi.C.printf("Hello %s!\n", "world")

local obj = ffi.new('point_t', 10, 20)
---@diagnostic disable-next-line: undefined-field
print('x: ' .. obj.x .. '\ny: ' .. obj.y)

ffi.metatype('point_t', {
  __index = {
    print = function(self)
      local fstr = 'X: %d, Y: %d'
      print(fstr:format(self.x, self.y))
    end
  }
})

---@diagnostic disable-next-line: undefined-field
obj:print()

local function test()
  print(2)
  print(3)
  print(5)
end
test()
