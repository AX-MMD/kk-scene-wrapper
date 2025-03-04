import os
import pytest
from kk_scene_wrapper import SceneData

# Define the expected parameters for each file
test_files = [
    {
        "path": "test_timeline-animefolders-sfx.png",
        "timeline_status": True,
        "image_type": "animation",
        "sfx_status": True,
        "duration": 8.05,
    },
    {
        "path": "test_timeline-animefolders.png",
        "timeline_status": True,
        "image_type": "animation",
        "sfx_status": False,
        "duration": 8.05,
    },
    {
        "path": "test_timeline-full-with-noduration.png",
        "timeline_status": True,
        "image_type": "animation",
        "sfx_status": False,
        "duration": 0.0,
    },
    {
        "path": "test_timeline-only-2-pos-interpolables.png",
        "timeline_status": True,
        "image_type": "dynamic",
        "sfx_status": False,
        "duration": 8.05,
    },
    {
        "path": "test_timeline-only-2-keyframes.png",
        "timeline_status": True,
        "image_type": "dynamic",
        "sfx_status": False,
        "duration": 8.05,
    },
    {
        "path": "test_timeline-no-pos-rot-keyframes.png",
        "timeline_status": True,
        "image_type": "dynamic",
        "sfx_status": False,
        "duration": 8.05,
    },
    {
        "path": "test_timeline-noanimefolders.png",
        "timeline_status": True,
        "image_type": "animation",
        "sfx_status": False,
        "duration": 8.05,
    },
    {
        "path": "test_timeline-noduration.png",
        "timeline_status": False,
        "image_type": "static",
        "sfx_status": False,
        "duration": 0.0,
    },
    {
        "path": "test_timeline-nokeyframes.png",
        "timeline_status": False,
        "image_type": "static",
        "sfx_status": False,
        "duration": 0.0,
    },
    # Add more file parameters here
]


TEST_DATA_PATH = os.path.join("tests/data")


# Test not a scene data with parametrized test_not_scene_data.png and test_not_scene_data.md by catching the SceneData.ContentError
@pytest.mark.parametrize("file_params", ["test_not_scene_data.png", "test_not_scene_data.md"])
def test_not_scene_data(file_params):
    file_path = os.path.join(TEST_DATA_PATH, file_params)
    with pytest.raises(SceneData.ContentError):
        SceneData(file_path)


@pytest.mark.parametrize("file_params", test_files)
def test_scene_data_attr(file_params):
    file_path = os.path.join(TEST_DATA_PATH, file_params["path"])
    sd = SceneData(file_path)

    assert sd.duration == file_params["duration"], f"{sd.duration} != {file_params['duration']}: {file_path}"
    assert sd.content, f"{sd.content} is empty: {file_path}"
    assert sd.content_str, f"{sd.content_str} is empty: {file_path}"


@pytest.mark.parametrize("file_params", test_files)
def test_scene_data_timeline(file_params):
    file_path = os.path.join("tests/data", file_params["path"])
    sd = SceneData(file_path)

    image_type, sfx_status, duration = sd.get_timeline_info()
    assert sd.has_timeline() == file_params["timeline_status"], f"{sd.has_timeline()} != {file_params['timeline_status']}: {file_params['path']}"
    assert image_type == file_params["image_type"], f"{image_type} != {file_params['image_type']}: {file_params['path']}"
    assert sfx_status == file_params["sfx_status"], f"{sfx_status} != {file_params['sfx_status']}: {file_params['path']}"
    assert duration == file_params["duration"], f"{duration} != {file_params['duration']}: {file_params['path']}"
