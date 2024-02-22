from interfaces.i_algorithm import IAlgorithm


class AlgorithmFactory:
    @staticmethod
    def create_algorithm(name, **kwargs):
        if name == 'random_forest':
            from algorithms.random_forest import RandomForestAlgorithm
            return RandomForestAlgorithm(**kwargs)
        # Add other algorithms as needed
        else:
            raise ValueError(f"No known algorithm with the name '{name}'")
