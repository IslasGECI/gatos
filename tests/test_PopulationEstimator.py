from gatos.PopulationEstimator import PopulationEstimator


def test_init():
    catch = [1, 2]
    effort = [100, 200]
    file_name = "nombre_archivo"
    Estimator = PopulationEstimator(effort, catch, file_name)
    assert Estimator.esfuerzo == effort
    assert Estimator.capturas == catch
    assert Estimator._nombre_archivo == file_name
