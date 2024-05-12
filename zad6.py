import inspect
import logging
from datetime import datetime
from functools import wraps
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def log(level=logging.DEBUG):
    def decorator(func_or_class):
        logger = logging.getLogger(func_or_class.__module__)
        logger.setLevel(level)

        if inspect.isfunction(func_or_class):
            @wraps(func_or_class)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                dt_object = datetime.fromtimestamp(start_time)
                start = dt_object.strftime("%Y-%m-%d %H:%M:%S,%f")

                result = func_or_class(*args, **kwargs)
                end_time = time.time()
                elapsed_time = end_time - start_time

                logger.log(level,f"Function {func_or_class.__name__} called with args: {args}, kwargs: {kwargs}, "
                                 f"at {start}, returned: {result}, execution time: {elapsed_time} seconds")
                return result
            return wrapper

        elif inspect.isclass(func_or_class):
            class_name = func_or_class.__name__

            @wraps(func_or_class)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                dt_object = datetime.fromtimestamp(start_time)
                start = dt_object.strftime("%Y-%m-%d %H:%M:%S,%f")

                obj = func_or_class(*args, **kwargs)
                logger.log(level, f"Class {class_name} instantiated at {start} with args: {args}, "
                                  f"kwargs: {kwargs}")
                return obj

            return wrapper
        raise TypeError("Unsupported type for decoration")
    return decorator


@log(level=logging.INFO)
def example_function(x, y):
    return x + y


@log(level=logging.DEBUG)
class ExampleClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    result = example_function(3, 4)
    obj = ExampleClass(5, 6)

    print("Result of example_function:", result)
    print("Object of ExampleClass created with x =", obj.x, "and y =", obj.y)
