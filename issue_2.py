"""

Here we made the Wrapper class be a subclass of A, but PyCharm want us so call A __init__ function. Which we don't
want because A has already been initialised, and it is useless (and can in some case be time-consuming) to do it again.

"""

class A:
    def __init__(self):
        self.attribute = 5


class Wrapper(A):

    def __init__(self, wrapped_a):  # TODO: Issue: Call to __init__ of super class is missed
        self.wrapped_a = wrapped_a

    def __getattr__(self, name):
        """Returns an attribute with ``name``, unless ``name`` starts with an underscore."""
        if name.startswith("_"):
            raise AttributeError(f"accessing private attribute '{name}' is prohibited")
        return getattr(self.wrapped_a, name)

    def function(self):
        print("My attribute is ", self.attribute)


if __name__ == "__name__":
    wrapper = Wrapper(A())
