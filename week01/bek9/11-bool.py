# truthy
truthy = [
	"python",
	[1, 2],
	2
]

while truthy:
	print(bool(truthy.pop()))

# falsy
falsy = [
	"",
	[],
	(),
	{},
	set([]),
	0,
	None
]

while falsy:
	print(bool(falsy.pop()))