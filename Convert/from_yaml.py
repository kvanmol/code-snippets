def yaml2dict(yaml_file: str) -> dict:
    """ Reads .YAML file and converts it to a python dictionary. """
    import yaml

    with open(yaml_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        
        except yaml.YAMLError as e:
            print(e)
