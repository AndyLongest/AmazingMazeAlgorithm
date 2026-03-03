from maze.algorithms.aldous_broder import AldousBroderAlgorithm
from maze.algorithms.backtracker import RecursiveBacktrackerAlgorithm
from maze.algorithms.base import MazeAlgorithm
from maze.algorithms.eller import EllerAlgorithm
from maze.algorithms.kruskal import RandomizedKruskalAlgorithm
from maze.algorithms.prim import RandomizedPrimAlgorithm
from maze.algorithms.sidewinder import SidewinderAlgorithm


ALGORITHM_CLASSES: dict[str, type[MazeAlgorithm]] = {
	RecursiveBacktrackerAlgorithm.name: RecursiveBacktrackerAlgorithm,
	RandomizedPrimAlgorithm.name: RandomizedPrimAlgorithm,
	RandomizedKruskalAlgorithm.name: RandomizedKruskalAlgorithm,
	AldousBroderAlgorithm.name: AldousBroderAlgorithm,
	SidewinderAlgorithm.name: SidewinderAlgorithm,
	EllerAlgorithm.name: EllerAlgorithm,
}


def create_algorithm(name: str) -> MazeAlgorithm:
	algorithm_class = ALGORITHM_CLASSES.get(name)
	if algorithm_class is None:
		raise ValueError(
			f"Unsupported algorithm: {name}. Available: {', '.join(sorted(ALGORITHM_CLASSES))}"
		)
	return algorithm_class()


def available_algorithms() -> list[str]:
	return sorted(ALGORITHM_CLASSES.keys())
