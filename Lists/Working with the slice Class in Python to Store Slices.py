tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

#print(tags[1:4:2]) #(start, stop, step) explicit

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])


#One of the biggest reasons why you'd ever use this slice class over using just this explicit version slice(1, 4, 2) is whenever you want to define
#  your ranges and your steps and those kinds of elements and you want to store them in a variable and then simply call them later on and or also
#  another opportunity where this would be a very good fit is if you're maybe calling this on different datasets.