
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


class RoundFloatManul(object):
    """Documentation for RoundFloatManul
    """
    def __init__(self, val):
        assert isinstance(val, float), "Value must be a float"
        self.value = round(val, 2)

