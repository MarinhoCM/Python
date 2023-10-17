def add_name(object: dict, name: str, value: int) -> object:
    obj: dict = {}
    obj.update(object)
    obj.update({str(name):(value)})
    return obj
