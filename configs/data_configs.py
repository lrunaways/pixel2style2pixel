from configs import transforms_config
from configs.paths_config import dataset_paths


DATASETS = {
	'ffhq_encode': {
		'transforms': transforms_config.EncodeTransforms,
		'train_source_root': dataset_paths['ffhq'],
		'train_target_root': dataset_paths['ffhq'],
		'test_source_root': dataset_paths['celeba_test'],
		'test_target_root': dataset_paths['celeba_test'],
	},
	'panel_to_pixel': {
		'transforms': transforms_config.EncodeTransforms,
		'train_source_root': dataset_paths['panel'],
		'train_target_root': dataset_paths['panel'],
		'test_source_root': dataset_paths['pixel'],
		'test_target_root': dataset_paths['pixel'],
	},
	'pixel_to_panel': {
		'transforms': transforms_config.EncodeTransforms,
		'train_source_root': dataset_paths['pixel'],
		'train_target_root': dataset_paths['pixel'],
		'test_source_root': dataset_paths['panel'],
		'test_target_root': dataset_paths['panel'],
	},
}
