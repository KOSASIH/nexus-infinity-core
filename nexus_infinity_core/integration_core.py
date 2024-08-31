class IntegrationCore:
    """
    Integration Core for module communication and data exchange.

    Attributes:
    -----------
    modules : dict
        Registered modules and their APIs.
    """

    def __init__(self):
        self.modules = {}

    def register_module(self, module_name, module_api):
        """
        Register a module and its API.

        Parameters:
        -----------
        module_name : str
            Name of the module.
        module_api : object
            API of the module.

        Returns:
        -------
        None
        """
        self.modules[module_name] = module_api

    def route_data(self, module_name, data):
        """
        Route data to a registered module.

        Parameters:
        -----------
        module_name : str
            Name of the module.
        data : object
            Data to be routed.

        Returns:
        -------
        result : object
            Result of the data routing operation.
        """
        module_api = self.modules.get(module_name)
        if module_api:
            return module_api.process_data(data)
        else:
            raise ValueError(f"Module '{module_name}' not registered")

    def orchestrate_api(self, module_names, api_calls):
        """
        Orchestrate API calls between registered modules.

        Parameters:
        -----------
        module_names : list
            List of module names.
        api_calls : list
            List of API calls to be made.

        Returns:
        -------
        results : list
            Results of the API calls.
        """
        results = []
        for module_name, api_call in zip(module_names, api_calls):
            module_api = self.modules.get(module_name)
            if module_api:
                result = module_api.make_api_call(api_call)
                results.append(result)
            else:
                raise ValueError(f"Module '{module_name}' not registered")
        return results
