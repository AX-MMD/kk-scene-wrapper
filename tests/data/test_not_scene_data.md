### USAGE ##############################################################
___
```python
from kk_scene_wrapper import SceneData

path = "/path/to/scene-file"
sd = SceneData(path)

timeline_binary = sd.get_timeline_xml
timeline = sd.get_timeline_xml_tree()
(
  timeline_status: str,    
  image_type: Optional[str]
  sfx_status: bool,
  duration: int
) = sd.get_timeline_info()
```
