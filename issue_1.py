
"""
First way of doing a wrapper of a class A
Here, when we have an instance of Wrapper(A()), and we want to access an attribute of Wrapper(A()).wrapped_a, the
auto-completion is not available because PyCharm don't know that Wrapper have the same behaviour as A.

A solution can be to make Wrapper a child class of A, but there is another issue (cf issue_2.py)
"""
class A:
    def __init__(self):
        self.attribute = 5


class Wrapper:

    def __init__(self, wrapped_a):
        self.wrapped_a = wrapped_a

    def __getattr__(self, name):
        """Returns an attribute with ``name``, unless ``name`` starts with an underscore."""
        if name.startswith("_"):
            raise AttributeError(f"accessing private attribute '{name}' is prohibited")
        return getattr(self.wrapped_a, name)

    def function(self):
        print("My attribute is ", self.attribute)  # TODO: Problem here: no auto-completion for self.att...


if __name__ == "__name__":
    wrapper = Wrapper(A())
