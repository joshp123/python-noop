import inspect


def noop_module(module):
    for thing in module.__dir__():
        if inspect.isclass(getattr(module, thing)):
            # set classes to object in case of inheritance
            setattr(module, thing, object)
        else:
            setattr(module, thing, lambda *args, **kwargs: None)
