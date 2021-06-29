from gatos.PopulationEstimator import PopulationEstimator


class Test_PopulationEstimator():
    def setup(self):
        effort = [100, 200]
        catch = [1, 2]
        file_name = "nombre_archivo"
        self.Estimator = PopulationEstimator(effort, catch, file_name)

    def test_init(self):
        expected_effort = [100, 200]
        expected_catch = [1, 2]
        expected_file_name = "nombre_archivo"
        assert self.Estimator.esfuerzo == expected_effort
        assert self.Estimator.capturas == expected_catch
        assert self.Estimator._nombre_archivo == expected_file_name
        assert self.Estimator.tamanios_poblacion is None

    def test_run(self):
        self.Estimator.run(iteraciones = 100, n_datos_descartados = 3)
        
