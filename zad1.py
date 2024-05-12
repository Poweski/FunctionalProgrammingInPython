acronym = lambda lst: ''.join(map(lambda x: x[0], lst))

median = lambda nums: sorted(nums)[len(nums) // 2] if len(nums) % 2 != 0 else sum(sorted(nums)[len(nums) // 2 - 1:len(nums) // 2 + 1]) / 2

sqrt_newton = (
    lambda f: lambda x, epsilon: f(f, x / 2, x, epsilon)
)(
    lambda self, y, x, epsilon: y if abs(y ** 2 - x) < epsilon else self(self, y - (y**2-x)/(2*y), x, epsilon)
)

make_alpha_dict = lambda text: {char: [word for word in text.split() if char in word] for char in set(text) if char.isalpha()}

flatten = lambda lst: [elem for sub_lst in lst for elem in (flatten(sub_lst) if isinstance(sub_lst, (list, tuple)) else [sub_lst])]


if __name__ == "__main__":
    print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))
    print(median([1, 1, 19, 2, 3, 4, 4, 5]))
    print(sqrt_newton(3, epsilon=0.1))
    print(make_alpha_dict("on i ona"))
    print(flatten([1, [2, 3], [[4, 5], 6]]))
