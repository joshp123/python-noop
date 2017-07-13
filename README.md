# python-noop
Turns a module into a no-op for you. You probably shouldn't do this.


## Why?

Sometimes modules do bad things (pickle). You might want to disable them but you can't (because stuff depends on it). The "solution"? Monkey patch it at run-time to do nothing at all!

## How?

```python
>>> import base64
>>> import noop
>>> noop.noop_module(base64)
>>> base64.b64encode('beep boop')
>>>
```
## Installation:

```
pip install no-op
```
